from django import template
from django.template.base import FilterExpression, Parser, Token
from django.utils.safestring import SafeString

register: template.Library

class ComponentNode(template.Node):
    component: FilterExpression
    extra_context: dict[str, FilterExpression]
    isolated_context: bool
    fallback_render_method: FilterExpression | None
    target_var: str | None
    def __init__(
        self,
        component: FilterExpression,
        extra_context: dict[str, FilterExpression] | None = None,
        isolated_context: bool = False,
        fallback_render_method: FilterExpression | None = None,
        target_var: str | None = None,
    ) -> None: ...
    def render(self, context: template.Context) -> SafeString: ...

def component(parser: Parser, token: Token) -> ComponentNode: ...
