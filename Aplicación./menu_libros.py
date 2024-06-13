libros = []  # Lista para almacenar libros

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
        agregar_libro()
    elif opcion_menu_libros == '2':
        ver_libros()
    elif opcion_menu_libros == '3':
        actualizar_libro()
    elif opcion_menu_libros == '4':
        eliminar_libro()
    elif opcion_menu_libros == '5':
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_libros()

def agregar_libro():
    titulo = input('Ingrese el título del libro: ')
    autor = input('Ingrese el autor del libro: ')
    ano = input('Ingrese el año de publicación del libro: ')
    isbn = input('Ingrese el ISBN del libro: ')
    libros.append({'titulo': titulo, 'autor': autor, 'año': ano, 'ISBN': isbn})
    print(f'Libro agregado exitosamente: {titulo} por {autor}')
    mostrar_menu_libros()

def ver_libros():
    print('Lista de libros...')
    for libro in libros:
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, ISBN: {libro['ISBN']}")
    mostrar_menu_libros()

def actualizar_libro():
    isbn = input('Ingrese el ISBN del libro a actualizar: ')
    for libro in libros:
        if libro['ISBN'] == isbn:
            nuevo_titulo = input('Ingrese el nuevo título del libro: ')
            nuevo_autor = input('Ingrese el nuevo autor del libro: ')
            nuevo_ano = input('Ingrese el nuevo año de publicación del libro: ')
            libro['titulo'] = nuevo_titulo
            libro['autor'] = nuevo_autor
            libro['año'] = nuevo_ano
            print('Libro actualizado exitosamente')
            mostrar_menu_libros()
    print('No se encontró ningún libro con ese ISBN')
    mostrar_menu_libros()

def eliminar_libro():
    isbn = input('Ingrese el ISBN del libro a eliminar: ')
    for libro in libros:
        if libro['ISBN'] == isbn:
            libros.remove(libro)
            print('Libro eliminado exitosamente')
            mostrar_menu_libros()
    print('No se encontró ningún libro con ese ISBN')
    mostrar_menu_libros()