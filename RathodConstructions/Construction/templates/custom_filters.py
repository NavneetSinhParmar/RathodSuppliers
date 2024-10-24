from django import template

register = template.Library()

@register.filter
def index(iterable, i):
    try:
        return iterable[i]
    except (IndexError, KeyError):
        return None
