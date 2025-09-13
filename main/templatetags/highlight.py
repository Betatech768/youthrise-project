import re
from django import template

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    # Escape regex characters in query
    pattern = re.escape(query)
    highlighted = re.sub(
        pattern,
        lambda m: f'<span class="highlighted">{m.group(0)}</span>',       
        text,
        flags=re.IGNORECASE
    )
    return highlighted
highlight.is_safe = True