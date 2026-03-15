from django.forms.widgets import Media, MediaDefiningClass
from django.utils.safestring import SafeString
from laces.typing import HasMediaProperty, RenderContext

class Component(metaclass=MediaDefiningClass):
    template_name: str
    def render_html(
        self,
        parent_context: RenderContext | None = None,
    ) -> SafeString: ...
    def get_context_data(
        self,
        parent_context: RenderContext | None = None,
    ) -> RenderContext | None: ...
    @property
    def media(self) -> Media: ...

class MediaContainer(list[HasMediaProperty]):
    @property
    def media(self) -> Media: ...
