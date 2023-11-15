def get_menu_tree(menu, menu_tree=None, menu_path=None, menu_positions=None):
    if menu_tree is None:
        menu_tree = []
    if menu_path is None:
        menu_path = []
    if menu_positions is None:
        menu_positions = []
       
    children = menu.children.all().order_by('name')  
    if children:
        menu_tree.append(children)
    
    menu_path.append(menu)
    
    if menu.parent:
        menu_positions.append(list(menu.parent.children.all().order_by('name')).index(menu))
        return get_menu_tree(menu.parent, menu_tree, menu_path, menu_positions)
    else:
        menu_indents = []
        for key in range(len(menu_positions)):
            menu_indents.append(sum(menu_positions[key:]) * 23)
        menu_indents.append(0)
        menu_indents.reverse()
        menu_tree.reverse()
        return menu_tree, menu_indents, menu_path
