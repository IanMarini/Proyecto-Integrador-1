prestamos = []  # Lista para almacenar préstamos

def mostrar_menu_prestamos():
    print("")
    print('1. Registrar Préstamo')
    print('2. Ver Préstamos')
    print('3. Registrar Devolución')
    print('4. Volver al menú principal')
    print("")
    opcion_menu_prestamos = input('Por favor, elija la opción deseada: ')

    if opcion_menu_prestamos == '1':
        registrar_prestamo()
    elif opcion_menu_prestamos == '2':
        ver_prestamos()
    elif opcion_menu_prestamos == '3':
        registrar_devolucion()
    elif opcion_menu_prestamos == '4':
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_prestamos()

def registrar_prestamo():
    id_usuario = input('Ingrese el ID del usuario que realiza el préstamo: ')
    isbn_libro = input('Ingrese el ISBN del libro a prestar: ')
    prestamos.append({'ID_usuario': id_usuario, 'ISBN_libro': isbn_libro})
    print(f'Préstamo registrado exitosamente para el usuario {id_usuario} y el libro {isbn_libro}')
    mostrar_menu_prestamos()

def ver_prestamos():
    print('Lista de préstamos...')
    for prestamo in prestamos:
        print(f"ID de Usuario: {prestamo['ID_usuario']}, ISBN del Libro: {prestamo['ISBN_libro']}")
    mostrar_menu_prestamos()

def registrar_devolucion():
    id_usuario = input('Ingrese el ID del usuario que devuelve el libro: ')
    isbn_libro = input('Ingrese el ISBN del libro a devolver: ')
    for prestamo in prestamos:
        if prestamo['ID_usuario'] == id_usuario and prestamo['ISBN_libro'] == isbn_libro:
            prestamos.remove(prestamo)
            print(f'Devolución registrada exitosamente para el usuario {id_usuario} y el libro {isbn_libro}')
            mostrar_menu_prestamos()
    print('No se encontró ningún préstamo asociado a este usuario y libro')
    mostrar_menu_prestamos()