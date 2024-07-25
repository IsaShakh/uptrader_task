from django import template
from django.db.models import Prefetch
from app.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    try:
        menu = Menu.objects.prefetch_related(
            Prefetch('items', queryset=MenuItem.objects.select_related('parent').all())
        ).get(name=menu_name)
        menu_items = menu.items.all()
    except Menu.DoesNotExist:
        menu_items = []

    def find_active_item(items, current_url):
        for item in items:
            if item.get_url() == current_url:
                return item
        return None

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'expanded': False  
                })
        return tree

    def mark_expanded_nodes(tree, active_item):
        for node in tree:
            if active_item and (node['item'] == active_item or is_parent(node['item'], active_item)):
                node['expanded'] = True
            mark_expanded_nodes(node['children'], active_item)

    def is_parent(parent, child):
        if child.parent is None:
            return False
        if child.parent == parent:
            return True
        return is_parent(parent, child.parent)

    active_item = find_active_item(menu_items, current_url)
    menu_tree = build_tree(menu_items)
    mark_expanded_nodes(menu_tree, active_item)

    context.update({
        'menu_name': menu_name,
        'menu_tree': menu_tree,
        'active_item': active_item,
    })
    return context
