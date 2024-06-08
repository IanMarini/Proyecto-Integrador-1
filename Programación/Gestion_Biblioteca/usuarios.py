def mostrar_menu_usuarios():
    print("")
    print('1. Agregar Usuario')
    print('2. Ver Usuarios')
    print('3. Actualizar Usuario')
    print('4. Eliminar Usuario')
    print('5. Volver al menú principal')
    print("")
    opcion_menu_usuarios = input('Por favor, elija la opción deseada: ')

    if opcion_menu_usuarios == '1':
        print('Agregar Usuario seleccionado')
    elif opcion_menu_usuarios == '2':
        print('Ver Usuarios seleccionado')
    elif opcion_menu_usuarios == '3':
        print('Actualizar Usuario seleccionado')
    elif opcion_menu_usuarios == '4':
        print('Eliminar Usuario seleccionado')
    elif opcion_menu_usuarios == '5':
        from index import menu_principal
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_usuarios()
