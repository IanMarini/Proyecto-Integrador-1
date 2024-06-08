def mostrar_menu_categorias():
    print("")
    print('1. Agregar Categoría')
    print('2. Ver Categorías')
    print('3. Eliminar Categoría')
    print('4. Volver al menú principal')
    print("")
    opcion_menu_categorias = input('Por favor, elija la opción deseada: ')

    if opcion_menu_categorias == '1':
        print('Agregar Categoría seleccionado')
    elif opcion_menu_categorias == '2':
        print('Ver Categorías seleccionado')
    elif opcion_menu_categorias == '3':
        print('Eliminar Categoría seleccionado')
    elif opcion_menu_categorias == '4':
        from index import menu_principal
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_categorias()
