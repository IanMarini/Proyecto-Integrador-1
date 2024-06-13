categorias = []  # Lista para almacenar categorías

def mostrar_menu_categorias():
    print("")
    print('1. Agregar Categoría')
    print('2. Ver Categorías')
    print('3. Eliminar Categoría')
    print('4. Volver al menú principal')
    print("")
    opcion_menu_categorias = input('Por favor, elija la opción deseada: ')

    if opcion_menu_categorias == '1':
        agregar_categoria()
    elif opcion_menu_categorias == '2':
        ver_categorias()
    elif opcion_menu_categorias == '3':
        eliminar_categoria()
    elif opcion_menu_categorias == '4':
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_categorias()

def agregar_categoria():
    print('Agregar Categoría seleccionado')
    categorias.append(input('Ingrese el nombre de la categoría: '))
    print('Categoría agregada exitosamente')
    mostrar_menu_categorias()

def ver_categorias():
    print('Lista de categorías...')
    for categoria in categorias:
        print(categoria)
    mostrar_menu_categorias()

def eliminar_categoria():
    categoria = input('Ingrese el nombre de la categoría a eliminar: ')
    if categoria in categorias:
        categorias.remove(categoria)
        print('Categoría eliminada exitosamente')
    else:
        print('La categoría no existe')
    mostrar_menu_categorias()