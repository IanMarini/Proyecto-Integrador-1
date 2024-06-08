def mostrar_menu_libros():
    print("")
    print('1. Agregar Libro')
    print('2. Ver Libros')
    print('3. Actualizar Libro')
    print('4. Eliminar Libro')
    print('5. Volver al menú principal')
    print("")
    opcion_menu_libros = input('Por favor, elija la opción deseada: ')

    if opcion_menu_libros == '1':
        print('Agregar Libro seleccionado')
    elif opcion_menu_libros == '2':
        print('Ver Libros seleccionado')
    elif opcion_menu_libros == '3':
        print('Actualizar Libro seleccionado')
    elif opcion_menu_libros == '4':
        print('Eliminar Libro seleccionado')
    elif opcion_menu_libros == '5':
        from index import menu_principal
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_libros()
