from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from menu.models import Menu
from menu.functions import get_menu_tree

register = template.Library()

@register.simple_tag
def draw_menu(menu_slug):
    if menu_slug:
        try:
            menu = Menu.objects.get(slug=menu_slug)
        except Menu.DoesNotExist:
            return ''
    else:
        menu = Menu.objects.get(nesting_level=0)

    menu_tree, menu_indents, menu_path = get_menu_tree(menu)
    
    html = '<nav>'
    for children, indent in zip(menu_tree, menu_indents):
        html += f'<div style="margin-top: {indent}px">'
        for child in children:
            url = reverse('menu:menu', args=[child.slug])
            if child in menu_path:
                classes = 'a current-menu'
                span = '<span>➤</span>'
            else:
                classes = 'a'
                span = ''   
            html += f'<a href="{url}" class="{classes}">{child.name}{span}</a>'
        html += '</div>'    
    html += '</nav>'
    
    return mark_safe(html)