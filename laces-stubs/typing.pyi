from typing import Any, Protocol, TypeAlias, Union

from django.forms.widgets import Media
from django.template import Context
from django.utils.safestring import SafeString

RenderContext: TypeAlias = Union[Context, dict[str, Any]]

class HasRenderHtmlMethod(Protocol):
    def render_html(
        self,
        parent_context: RenderContext | None,
    ) -> SafeString: ...

class HasRenderMethod(Protocol):
    def render(self) -> SafeString: ...

Renderable: TypeAlias = Union[HasRenderHtmlMethod, HasRenderMethod]

class HasMediaProperty(Protocol):
    @property
    def media(self) -> Media: ...
