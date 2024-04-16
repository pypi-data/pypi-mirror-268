# SPDX-FileCopyrightText: Copyright DB InfraGO AG
# SPDX-License-Identifier: Apache-2.0
"""Classes that allow access to diagrams in the model."""
from __future__ import annotations

import abc
import base64
import collections.abc as cabc
import importlib.metadata as imm
import io
import logging
import os
import traceback
import typing as t
import uuid

import markupsafe

import capellambse
from capellambse import aird, diagram, helpers, svg

from . import common as c
from . import modeltypes

if t.TYPE_CHECKING:
    from lxml import etree

LEGACY_DIAGRAM_IDS = bool(os.getenv("CAPELLAMBSE_LEGACY_DIAGRAM_IDS"))
"""Report the representation ID as diagram UUID instead of the descriptor.

This mostly matches the behavior of capellambse pre 0.5.52, except that
the correct (new) IDs are used for lookups in the diagram cache.

This is a temporary stop-gap measure to aid in the migration of code
that relied on the old IDs. Do not write new code that expects this
variable to be set, as it will eventually be removed again in a future
release.
"""


@t.runtime_checkable
class DiagramFormat(t.Protocol):
    filename_extension: str

    @classmethod
    def convert(cls, dg: diagram.Diagram) -> t.Any: ...

    @classmethod
    def from_cache(cls, cache: bytes) -> t.Any: ...


@t.runtime_checkable
class PrettyDiagramFormat(DiagramFormat, t.Protocol):
    @classmethod
    def convert_pretty(cls, dg: diagram.Diagram) -> t.Any: ...


DiagramConverter = t.Union[
    t.Callable[[diagram.Diagram], t.Any],
    DiagramFormat,
]

LOGGER = logging.getLogger(__name__)
REPR_DRAW: bool | None = None


class UnknownOutputFormat(ValueError):
    """An unknown output format was requested for the diagram."""


class AbstractDiagram(metaclass=abc.ABCMeta):
    """Abstract superclass of model diagrams."""

    uuid: str
    """Unique ID of this diagram."""
    name: str
    """Human-readable name for this diagram."""
    target: c.GenericElement
    """This diagram's "target".

    The target of a diagram is usually:

    *   The model element which is the direct parent of all visible
        nodes **OR**
    *   The only top-level element in the diagram **OR**
    *   The element which is considered to be the "element of interest".
    """
    filters: cabc.MutableSet[str]
    """The filters that are activated for this diagram."""

    if t.TYPE_CHECKING:

        @property
        def _allow_render(self) -> bool: ...

    else:
        _allow_render: bool = True
        """Allow this diagram to be rendered by the internal rendering engine.

        If this property is set to False, and a diagram cache was
        specified for the model, this diagram can only be loaded from
        the cache, and will never be rendered. Has no effect if there
        was no diagram cache specified.

        :meta public:
        """
    _model: capellambse.MelodyModel
    _render: diagram.Diagram
    _error: BaseException
    _last_render_params: dict[str, t.Any] = {}
    """Additional rendering parameters for the cached rendered diagram.

    Rendering options for :class:`aird.Diagram`s. Handing over
    parameters that differ to these will force a fresh rendering of the
    diagram, flushing the cached diagram.

    The following parameters are currently supported:

        - ``sorted_exchangedItems`` (*bool*): Enable ExchangeItem
          sorting when rendering diagrams with active ExchangeItems
          filter (``show.exchange.items.filter``).
    """

    def __init__(self, model: capellambse.MelodyModel) -> None:
        self._model = model
        self._last_render_params = {}

    def __dir__(self) -> list[str]:
        return dir(type(self)) + [
            f"as_{i.name}"
            for i in imm.entry_points()["capellambse.diagram.formats"]
        ]

    def __getattr__(self, attr: str) -> t.Any:
        if attr.startswith("as_"):
            fmt = attr[len("as_") :]
            try:
                return self.render(fmt)
            except UnknownOutputFormat:
                raise
            except Exception as err:  # pylint: disable=broad-except
                if hasattr(self, "_error") and err is self._error:
                    err_img = self._render
                else:
                    err_img = self.__create_error_image("render", err)
                assert err_img is not None
                converter = _find_format_converter(fmt)
                if isinstance(converter, DiagramFormat):
                    return converter.convert(err_img)
                else:
                    return converter(err_img)
        return getattr(super(), attr)

    def __repr__(self) -> str:
        global REPR_DRAW
        if REPR_DRAW is None:
            REPR_DRAW = TerminalGraphicsFormat.is_supported()

        if not REPR_DRAW:
            return self._short_repr_()

        try:
            escapes = self.render("termgraphics")
        except Exception:
            LOGGER.exception("Cannot render diagram as PNG for display")
            return self._short_repr_()

        return self._short_repr_() + "\n" + escapes.decode("ascii")

    def _short_repr_(self) -> str:
        return f"<Diagram {self.name!r}>"

    def __html__(self) -> markupsafe.Markup:
        return (
            markupsafe.Markup("<figure>")
            + markupsafe.Markup(self.render("svg"))
            + markupsafe.Markup("<figcaption>")
            + self.name
            + markupsafe.Markup("</figcaption></figure>")
        )

    def _short_html_(self) -> markupsafe.Markup:
        return markupsafe.Markup(
            f"<b>{markupsafe.Markup.escape(self.name)}</b> "
            f"(uuid: {markupsafe.Markup.escape(self.uuid)})"
        )

    def _repr_mimebundle_(
        self,
        include: cabc.Container[str] | None = None,
        exclude: cabc.Container[str] | None = None,
        **_kw,
    ) -> tuple[dict[str, t.Any], dict[t.Any, t.Any]] | dict[str, t.Any] | None:
        if include is None:
            include = helpers.EverythingContainer()
        if exclude is None:
            exclude = ()

        formats: dict[str, DiagramConverter] = {}
        for _, conv in _iter_format_converters():
            mime = getattr(conv, "mimetype", None)
            if not mime or mime not in include or mime in exclude:
                continue

            formats[mime] = conv
        if not formats:
            return None

        bundle: dict[str, t.Any] = {}
        for mime, conv in formats.items():
            try:
                bundle[mime] = self.__load_cache(conv)
            except KeyError:
                pass

        if bundle:
            return bundle

        render = self.__render_fresh({})
        for mime, conv in formats.items():
            try:
                if isinstance(conv, DiagramFormat):
                    bundle[mime] = conv.convert(render)
                else:
                    bundle[mime] = conv(render)
            except Exception:
                LOGGER.exception("Failed converting diagram with %r", conv)
        if not bundle:
            LOGGER.error("Failed converting diagram for MIME bundle")
            bundle["text/plain"] = repr(self)
        return bundle

    @property
    def nodes(self) -> c.MixedElementList:
        """Return a list of all nodes visible in this diagram."""
        allids = {e.uuid for e in self.render(None) if not e.hidden}
        elems = []
        for elemid in allids:
            assert elemid is not None
            try:
                elem = self._model.by_uuid(elemid)
            except KeyError:
                continue

            elems.append(elem._element)
        return c.MixedElementList(self._model, elems, c.GenericElement)

    @t.overload
    def render(self, fmt: None, /, **params) -> diagram.Diagram: ...

    @t.overload
    def render(
        self, fmt: str, /, *, pretty_print: bool = ..., **params
    ) -> t.Any: ...

    def render(
        self,
        fmt: str | None,
        /,
        *,
        pretty_print: bool = False,
        **params,
    ) -> t.Any:
        """Render the diagram in the given format.

        Parameters
        ----------
        fmt
            The output format to use.

            If ``None``, the :class:`~capellambse.diagram.Diagram` is returned
            without format conversion.
        pretty_print
            Whether to pretty-print the output. Only applies to
            text-based formats. Ignored if the output format converter
            does not support pretty-printing.
        params
            Additional render parameters. Which parameters are
            supported depends on the specific type of diagram.
        """
        if fmt is not None:
            conv = _find_format_converter(fmt)
        else:

            def conv(i: diagram.Diagram) -> diagram.Diagram:
                return i

        if fmt is not None and self._model.diagram_cache is not None:
            try:
                return self.__load_cache(conv)
            except KeyError:
                pass

            if not self._allow_render:
                raise RuntimeError(f"Diagram not in cache: {self.name}")

        render = self.__render_fresh(params)
        if pretty_print and isinstance(conv, PrettyDiagramFormat):
            return conv.convert_pretty(render)
        elif isinstance(conv, DiagramFormat):
            return conv.convert(render)
        else:
            return conv(render)

    def save(
        self,
        file: str | os.PathLike | t.IO[bytes] | None,
        fmt: str,
        /,
        *,
        pretty_print: bool = False,
        **params,
    ) -> None:
        """Render the diagram and write it to a file.

        Parameters
        ----------
        file
            The file to write the diagram to. Can be a filename, or a
            file-like object in binary mode.

            Text-based formats that render to a :class:`str` will always
            be encoded as UTF-8.

            If None is passed, and the selected format has a known
            filename extension, a filename will be generated from the
            diagram's name and the extension.
        fmt
            The output format to use.
        pretty_print
            Whether to pretty-print the output. Only applies to
            text-based formats. Ignored if the output format converter
            does not support pretty-printing.
        params
            Additional render parameters to pass to the :meth:`render`
            call.
        """
        if file is None:
            conv = _find_format_converter(fmt)
            if ext := getattr(conv, "filename_extension", None):
                file = f"{self.name} ({self.uuid}){ext}"
            else:
                raise ValueError(
                    f"No known extension for format {fmt!r},"
                    " specify a file name explicitly"
                )
        data = self.render(fmt, pretty_print=pretty_print, **params)
        if isinstance(data, str):
            data = data.encode("utf-8")
        elif not isinstance(data, bytes):
            raise TypeError(
                f"Cannot write format {fmt!r} to file:"
                f" expected str or bytes, got {type(data).__name__}"
            )
        if hasattr(file, "write"):
            file.write(data)
        else:
            with open(file, "wb") as f:
                f.write(data)

    @abc.abstractmethod
    def _create_diagram(self, params: dict[str, t.Any]) -> diagram.Diagram:
        """Perform the actual rendering of the diagram.

        This method is called by :meth:`.render` to perform the actual
        rendering of the diagram. It is passed the parameters that were
        passed to :meth:`.render` as a dictionary.

        Subclasses override this method to implement their rendering
        logic. Do not call this method directly, use :meth:`.render`
        instead - it will take care of caching and properly converting
        the render output.

        :meta public:
        """

    def __create_error_image(
        self, stage: str, error: Exception
    ) -> diagram.Diagram:
        err_name = (
            "An error occured while rendering diagram\n"
            f"{self.name!r}\n"
            f"(in stage {stage!r})"
        )
        err_msg = (
            "Please report this error to your tools and methods team,"
            " and attach the following information:"
        )
        err_trace = "".join(
            traceback.format_exception(None, error, error.__traceback__)
        )

        diag = diagram.Diagram("An error occured! :(")
        err_box = diagram.Box(
            (200, 0),
            (350, 0),
            label=err_name,
            uuid="error",
            styleclass="Note",
            styleoverrides={
                "fill": diagram.RGB(255, 0, 0),
                "text_fill": diagram.RGB(255, 255, 255),
            },
        )
        diag.add_element(err_box, extend_viewport=False)
        info_box = diagram.Box(
            (200, err_box.pos.y + err_box.size.y + 10),
            (350, 0),
            label=err_msg,
            uuid="info",
            styleclass="Note",
        )
        diag.add_element(info_box, extend_viewport=False)
        trace_box = diagram.Box(
            (0, info_box.pos.y + info_box.size.y + 10),
            (750, 0),
            label=err_trace,
            uuid="trace",
            styleclass="Note",
        )
        diag.add_element(trace_box, extend_viewport=False)
        diag.calculate_viewport()
        return diag

    def __load_cache(self, converter: DiagramConverter):
        cache_handler = self._model.diagram_cache
        cachedir = getattr(self._model, "_diagram_cache_subdir", None)
        if cache_handler is None or cachedir is None:
            raise KeyError(self.uuid)

        if not isinstance(converter, DiagramFormat):
            raise KeyError(self.uuid)

        try:
            ext = converter.filename_extension
            with cache_handler.open(cachedir / (self.uuid + ext)) as f:
                cache = f.read()
        except FileNotFoundError:
            LOGGER.debug("Diagram not in cache: %s (%s)", self.uuid, self.name)
            raise KeyError(self.uuid) from None

        return converter.from_cache(cache)

    def __render_fresh(self, params: dict[str, t.Any]) -> diagram.Diagram:
        # pylint: disable=broad-except
        if not hasattr(self, "_render") or self._last_render_params != params:
            self.invalidate_cache()
            try:
                self._render = self._create_diagram(params)
            except Exception as err:
                self._error = err
                self._render = self.__create_error_image("parse", self._error)

        if hasattr(self, "_error"):
            raise self._error
        return self._render

    def invalidate_cache(self) -> None:
        """Reset internal diagram cache."""
        try:
            del self._render
        except AttributeError:
            pass

        try:
            del self._error
        except AttributeError:
            pass


@c.xtype_handler(None, "viewpoint:DRepresentationDescriptor")
class Diagram(AbstractDiagram):
    """Provides access to a single diagram."""

    uuid: str = c.properties.AttributeProperty(  # type: ignore[assignment]
        "uid", writable=False
    )

    __real_uuid = c.properties.AttributeProperty("uid", writable=False)
    if LEGACY_DIAGRAM_IDS:

        @property  # type: ignore[no-redef]
        def uuid(self) -> str:
            return self.representation_path.rsplit("#", 1)[-1]

        @uuid.setter
        def uuid(self, value: str) -> None:
            raise TypeError("The uuid is read-only")

    xtype = property(lambda self: helpers.xtype_of(self._element))
    name: str = c.properties.AttributeProperty(  # type: ignore[assignment]
        "name", optional=True, default=""
    )
    description = c.properties.HTMLAttributeProperty(
        "documentation", optional=True
    )

    _element: aird.DRepresentationDescriptor
    _constructed: bool

    __nodes: list[etree._Element] | None

    @classmethod
    def from_model(
        cls,
        model: capellambse.MelodyModel,
        descriptor: aird.DRepresentationDescriptor,
    ) -> Diagram:
        """Wrap a diagram already defined in the Capella AIRD."""
        self = cls.__new__(cls)
        self._model = model
        self._element = descriptor
        self._constructed = True
        self.__nodes = None
        return self

    def __init__(self, **kw: t.Any) -> None:
        # pylint: disable=super-init-not-called
        raise TypeError("Cannot create a Diagram this way")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._model is other._model and self._element == other._element

    @property
    def nodes(self) -> c.MixedElementList:
        if self.__nodes is None:
            self.__nodes = list(
                aird.iter_visible(self._model._loader, self._element)
            )
        return c.MixedElementList(
            self._model, self.__nodes.copy(), c.GenericElement
        )

    @property
    def _allow_render(self) -> bool:
        return self._model._fallback_render_aird

    @property
    def viewpoint(self) -> str:
        return aird.viewpoint_of(self._element)

    @property
    def representation_path(self) -> str:
        """The ID of the representation, i.e. the actual diagram.

        Capella distinguishes between the representation (which contains
        all visual data) and a representation descriptor, which only
        contains a handful of metadata like the diagram name and
        description. Both have their own IDs, and the descriptor
        contains a link to the representation.
        """
        return self._element.attrib["repPath"]

    @property
    def target(self) -> c.GenericElement:  # type: ignore[override]
        target = aird.find_target(self._model._loader, self._element)
        return c.GenericElement.from_model(self._model, target)

    @property
    def type(self) -> modeltypes.DiagramType:
        """Return the type of this diagram."""
        sc = aird.get_styleclass(self._element)
        try:
            return modeltypes.DiagramType(sc)
        except ValueError:  # pragma: no cover
            LOGGER.warning("Unknown diagram type %r", sc)
            return modeltypes.DiagramType.UNKNOWN

    @property
    def filters(self) -> cabc.MutableSet[str]:
        """Return a set of currently activated filters on this diagram."""
        return aird.ActiveFilters(self._model, self)

    @filters.setter
    def filters(self, filters: cabc.Iterable[str]) -> None:
        self.filters.clear()
        for filter in filters:
            self.filters.add(filter)

    def _create_diagram(self, params: dict[str, t.Any]) -> diagram.Diagram:
        return aird.parse_diagram(self._model._loader, self._element, **params)

    def invalidate_cache(self) -> None:
        """Reset internal diagram cache."""
        self.__nodes = None
        super().invalidate_cache()

    def _AbstractDiagram__load_cache(self, converter: DiagramConverter):
        cache_handler = self._model.diagram_cache
        cachedir = getattr(self._model, "_diagram_cache_subdir", None)
        if cache_handler is None or cachedir is None:
            raise KeyError(self.uuid)

        if not isinstance(converter, DiagramFormat):
            raise KeyError(self.uuid)

        try:
            ext = converter.filename_extension
            with cache_handler.open(cachedir / (self.__real_uuid + ext)) as f:
                cache = f.read()
        except FileNotFoundError:
            LOGGER.debug("Diagram not in cache: %s (%s)", self.uuid, self.name)
            raise KeyError(self.__real_uuid) from None

        return converter.from_cache(cache)


class DiagramAccessor(c.Accessor):
    """Provides access to a list of diagrams below the specified viewpoint."""

    def __init__(
        self,
        viewpoint: str | None = None,
        *,
        cacheattr: str | None = None,
    ) -> None:
        super().__init__()
        self.cacheattr = cacheattr
        self.viewpoint = viewpoint

    def __get__(self, obj, objtype=None):
        del objtype
        if obj is None:  # pragma: no cover
            return self

        descriptors = aird.enumerate_descriptors(
            obj._model._loader, viewpoint=self.viewpoint
        )
        return c.CachedElementList(
            obj._model,
            list(descriptors),
            Diagram,
            cacheattr=self.cacheattr,
        )


class SVGFormat:
    """Convert the diagram to SVG."""

    filename_extension = ".svg"
    mimetype = "image/svg+xml"

    @staticmethod
    def convert(dg: diagram.Diagram) -> str:
        return convert_svgdiagram(dg).to_string()

    @staticmethod
    def convert_pretty(dg: diagram.Diagram) -> str:
        buf = io.StringIO()
        svgdg = convert_svgdiagram(dg).drawing
        drawing = svgdg._Drawing__drawing  # type: ignore[attr-defined]
        drawing.write(buf, pretty=True)
        return buf.getvalue()

    @staticmethod
    def from_cache(cache: bytes) -> str:
        return cache.decode("utf-8")


class PNGFormat:
    """Convert the diagram to PNG."""

    filename_extension = ".png"
    mimetype = "image/png"

    @staticmethod
    def convert(dg: diagram.Diagram) -> bytes:
        try:
            import cairosvg
        except OSError as error:
            raise RuntimeError(
                "Cannot import cairosvg. You are likely missing .dll's."
                " Please see the README for instructions."
            ) from error

        scale = float(os.getenv("CAPELLAMBSE_PNG_SCALE", "1"))
        return cairosvg.svg2png(SVGFormat.convert(dg), scale=scale)

    @staticmethod
    def from_cache(cache: bytes) -> bytes:
        return cache


def convert_svgdiagram(
    dg: diagram.Diagram,
) -> svg.generate.SVGDiagram:
    """Convert the diagram to a SVGDiagram."""
    jsondata = diagram.DiagramJSONEncoder().encode(dg)
    return svg.generate.SVGDiagram.from_json(jsondata)


class ConfluenceSVGFormat:
    """Convert the diagram to Confluence-style SVG."""

    filename_extension = ".svg"
    prefix = (
        f'<ac:structured-macro ac:macro-id="{uuid.uuid4()!s}" ac:name="html"'
        ' ac:schema-version="1">'
        "<ac:plain-text-body><![CDATA["
    )
    postfix = "]]></ac:plain-text-body></ac:structured-macro>"

    @classmethod
    def convert(cls, dg: diagram.Diagram) -> str:
        return "".join((cls.prefix, SVGFormat.convert(dg), cls.postfix))

    @classmethod
    def convert_pretty(cls, dg: diagram.Diagram) -> str:
        return (
            cls.prefix
            + "\n"
            + SVGFormat.convert_pretty(dg)
            + "\n"
            + cls.postfix
        )

    @classmethod
    def from_cache(cls, cache: bytes) -> str:
        return "".join((cls.prefix, cache.decode("utf-8"), cls.postfix))


class SVGDataURIFormat:
    filename_extension = ".svg"
    preamble = "data:image/svg+xml;base64,"

    @classmethod
    def convert(cls, dg: diagram.Diagram) -> str:
        payload = SVGFormat.convert(dg)
        b64 = base64.standard_b64encode(payload.encode("utf-8"))
        return "".join((cls.preamble, b64.decode("ascii")))

    @classmethod
    def from_cache(cls, cache: bytes) -> str:
        b64 = base64.standard_b64encode(cache)
        return "".join((cls.preamble, b64.decode("ascii")))


class SVGInHTMLIMGFormat:
    filename_extension = ".svg"
    mimetype = "text/html"

    @staticmethod
    def convert(dg: diagram.Diagram) -> markupsafe.Markup:
        payload = SVGDataURIFormat.convert(dg)
        return markupsafe.Markup(f'<img src="{payload}"/>')

    @staticmethod
    def from_cache(cache: bytes) -> str:
        payload = SVGDataURIFormat.from_cache(cache)
        return markupsafe.Markup(f'<img src="{payload}"/>')


class TerminalGraphicsFormat:
    """The kitty terminal graphics protocol diagram format.

    This graphics format generates terminal escape codes that transfer
    PNG data to a TTY using the `kitty graphics protocol`__.

    __ https://sw.kovidgoyal.net/kitty/graphics-protocol/
    """

    filename_extension = ".png"

    @classmethod
    def convert(cls, dg: diagram.Diagram) -> bytes:
        data: bytes = PNGFormat.convert(dg)
        return cls.from_cache(data)

    @staticmethod
    def from_cache(cache: bytes) -> bytes:
        container = b"\x1b_Ga=T,q=2,f=100,m=%d;%b\x1b\\"

        chunks: list[bytes] = []
        png_b64 = base64.standard_b64encode(cache)
        while png_b64:
            chunk, png_b64 = png_b64[:4096], png_b64[4096:]
            m = (0, 1)[bool(png_b64)]
            chunks.append(container % (m, chunk))

        return b"".join(chunks)

    @staticmethod
    def is_supported() -> bool:
        """Return whether the used terminal supports graphics.

        This implementation checks whether stdin, stdout and stderr are
        connected to a terminal, and whether the ``$TERM`` environment
        variable is set to a know-supportive value. Currently the only
        recognized value is ``xterm-kitty``.
        """
        return (
            all(os.isatty(i) for i in range(3))
            and os.getenv("TERM") == "xterm-kitty"
        )


def _find_format_converter(fmt: str) -> DiagramConverter:
    eps = imm.entry_points(group="capellambse.diagram.formats", name=fmt)
    if not eps:
        raise UnknownOutputFormat(f"Unknown image output format {fmt}")
    return next(iter(eps)).load()


def _iter_format_converters() -> t.Iterator[tuple[str, DiagramConverter]]:
    for ep in imm.entry_points(group="capellambse.diagram.formats"):
        try:
            conv = ep.load()
        except ImportError:
            pass
        else:
            yield (ep.name, conv)
