def mostrar_menu_prestamos():
    print("")
    print('1. Registrar Préstamo')
    print('2. Ver Préstamos')
    print('3. Registrar Devolución')
    print('4. Volver al menú principal')
    print("")
    opcion_menu_prestamos = input('Por favor, elija la opción deseada: ')

    if opcion_menu_prestamos == '1':
        print('Registrar Préstamo seleccionado')
    elif opcion_menu_prestamos == '2':
        print('Ver Préstamos seleccionado')
    elif opcion_menu_prestamos == '3':
        print('Registrar Devolución seleccionado')
    elif opcion_menu_prestamos == '4':
        from index import menu_principal
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_prestamos()
