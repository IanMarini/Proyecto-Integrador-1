usuarios = []  # Lista para almacenar usuarios

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
        agregar_usuario()
    elif opcion_menu_usuarios == '2':
        ver_usuarios()
    elif opcion_menu_usuarios == '3':
        actualizar_usuario()
    elif opcion_menu_usuarios == '4':
        eliminar_usuario()
    elif opcion_menu_usuarios == '5':
        menu_principal()
    else:
        print('Por favor, ingrese una opción válida')
        mostrar_menu_usuarios()


def agregar_usuario():
    nombre = input('Ingrese el nombre del usuario: ')
    apellido = input('Ingrese el apellido del usuario: ')
    id = input('Ingrese el ID del usuario: ')
    usuarios.append({'nombre': nombre, 'apellido': apellido, 'ID': id})
    print(f'Usuario agregado exitosamente: {nombre} {apellido}')
    mostrar_menu_usuarios()

def ver_usuarios():
    print('Lista de usuarios...')
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Apellido: {usuario['apellido']}, ID: {usuario['ID']}")
    mostrar_menu_usuarios()

def actualizar_usuario():
    id = input('Ingrese el ID del usuario a actualizar: ')
    for usuario in usuarios:
        if usuario['ID'] == id:
            nuevo_nombre = input('Ingrese el nuevo nombre del usuario: ')
            nuevo_apellido = input('Ingrese el nuevo apellido del usuario: ')
            usuario['nombre'] = nuevo_nombre
            usuario['apellido'] = nuevo_apellido
            print('Usuario actualizado exitosamente')
            mostrar_menu_usuarios()
    print('No se encontró ningún usuario con ese ID')
    mostrar_menu_usuarios()

def eliminar_usuario():
    id = input('Ingrese el ID del usuario a eliminar: ')
    for usuario in usuarios:
        if usuario['ID'] == id:
            usuarios.remove(usuario)
            print('Usuario eliminado exitosamente')
            mostrar_menu_usuarios()
    print('No se encontró ningún usuario con ese ID')
    mostrar_menu_usuarios()
