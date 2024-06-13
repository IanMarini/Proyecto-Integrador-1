from libros import mostrar_menu_libros
from usuarios import mostrar_menu_usuarios
from prestamos import mostrar_menu_prestamos
from categorias import mostrar_menu_categorias

def menu_principal():
    print('Bienvenido al sistema de gestión de biblioteca')
    print('1. Gestionar Libros')
    print('2. Gestionar Usuarios')
    print('3. Gestionar Préstamos')
    print('4. Gestionar Categorías')
    print('5. Salir')

    num = input('Por favor, elija la opción deseada: ')

    if num == '1':
        mostrar_menu_libros()
    elif num == '2':
        mostrar_menu_usuarios()
    elif num == '3':
        mostrar_menu_prestamos()
    elif num == '4':
        mostrar_menu_categorias()
    elif num == '5':
        print('Saliendo del sistema...')
    else:
        print('Por favor, ingrese una opción válida')
        menu_principal()

if __name__ == '__main__':
    menu_principal()