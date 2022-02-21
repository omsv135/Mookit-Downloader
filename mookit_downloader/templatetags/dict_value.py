from django import template

register = template.Library()


@register.filter(name="dictvaluefromkey")
def dictvaluefromkey(dictionary, key):
    return dictionary[key]
