import markdown

from django import template

register = template.Library()

@register.filter()
def markdownify(value):
    return markdown.markdown(markdown.markdown(value))
