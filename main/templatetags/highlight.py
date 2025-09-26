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


# myapp/templatetags/date_extras.py

@register.filter
def ordinal_day(value):
    day = value.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "TH"
    else:
        suffix = ["ST", "ND", "RD"][day % 10 - 1]
    return f"{day}{suffix} {value.strftime('%B')}"
