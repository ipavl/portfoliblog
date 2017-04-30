from pages.models import Page

from django import template

register = template.Library()

@register.filter()
def get_navbar_pages(self):
    return Page.objects.filter(show_in_menu=True).order_by('menu_sort_order')
