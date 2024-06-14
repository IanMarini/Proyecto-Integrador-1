if __name__ == "__main__":

# A continuación, añadimos un nuevo libro a la base de datos con la función add_book. 
# Esta función inserta un nuevo registro en la tabla Libros.
    # Agregar un libro
    add_book('El Alquimista', 'Paulo Coelho', '978-0061122415', 'HarperOne', 1993, True)
    print("SE AGREGO UN LIBRO") 

#La función get_books recupera todos los registros de la tabla Libros y los almacena en la variable libros. 
# Luego, el bucle for itera sobre cada libro y lo imprime, mostrando todos los libros disponibles en la base de datos.
    # Obtener todos los libros
    libros = get_books()
    for libro in libros:
        print(libro)
        print("MUESTRA LOS DATOS DE LA TABLA LIBROS")

# La función update_book actualiza el campo Disponibilidad del libro con ID igual a 1. 
# En este caso, establece la disponibilidad como True, indicando que el libro está disponible.
    # Actualizar la disponibilidad de un libro
    update_book(1, True)
    print("ACTUALIZO UN LIBRO")

# La función delete_book elimina el libro con ID igual a 11 de la tabla Libros, 
# eliminando así el registro del libro de la base de datos.
    # Eliminar un libro
    delete_book(11)
    print("ELIMINO UN LIBRO REGISTRADO")

# Agregar un nuevo usuario
# Primero, creamos un nuevo usuario en la base de datos utilizando la función add_user. 
# Esta función inserta un nuevo registro en la tabla Usuarios con los datos proporcionados.
    # Agregar un usuario
    add_user('Alan Gonzales', 'Calle Paco 789, Ciudad', '123-4512', 'Balan.gonzales@example.com')
    print("SE AGREGO UN USUARIO")

# La función get_users recupera todos los registros de la tabla Usuarios y los almacena en la variable usuarios. 
# Luego, el bucle for itera sobre cada usuario y lo imprime, mostrando todos los usuarios registrados en la base de datos.
    # Obtener todos los usuarios
    usuarios = get_users()
    for usuario in usuarios:
        print(usuario)
        print("MUESTRA LOS DATOS DE LA TABLA USUARIOS")

# La función update_user actualiza el campo Telefono del usuario con ID igual a 3. 
# En este caso, establece el nuevo teléfono como "351-8623638".
    # Actualizar el teléfono de un usuario
    update_user(3, '351-8623638')
    print("ACTUALIZO UN USUARIO")

# La función delete_user_and_loans elimina el usuario con ID igual a 5 de la tabla Usuarios junto con todos sus préstamos asociados. 
# Esto asegura que no queden registros huérfanos en la base de datos.
    # Eliminar un usuario
    delete_user_and_loans(5)
    print("ELIMINO UN USUARIO REGISTRADO")

# La función add_loan inserta un nuevo registro en la tabla Prestamos con los datos proporcionados:
    # Agregar un préstamo
    add_loan(1, 1, '2024-06-01')
    print("SE AGRGO UN PRÉSTAMO")

#La función get_loans recupera todos los registros de la tabla Prestamos y los almacena en la variable prestamos.
# Luego, el bucle for itera sobre cada préstamo y lo imprime, mostrando todos los préstamos registrados en la base de datos.
    # Obtener todos los préstamos
    prestamos = get_loans()
    for prestamo in prestamos:
        print(prestamo)
        print("MUESTRA LOS DATOS DE LA TABLA PRÉSTAMOS")

#La función update_loan actualiza el campo Fecha_Devolucion del préstamo con ID igual a 1. 
# En este caso, establece la nueva fecha de devolución como '2024-06-10'.
    # Actualizar la fecha de devolución de un préstamo
    update_loan(1, '2024-06-10')
    print("ACTUALIZO LA FECHA DE DEVOLUCIÓN")

#La función delete_loan elimina el préstamo con ID igual a 2 de la tabla Prestamos, 
# eliminando así el registro del préstamo de la base de datos.
    # Eliminar un préstamo
    delete_loan(2)
    print("ELIMINO UN PRESTAMO REGISTRADO")

# La función add_category inserta un nuevo registro en la tabla Categorias con el nombre proporcionado, 
# en este caso, "Ficción".
    # Agregar una categoría
    add_category('Ficción')
    print("SE REGISTRO UNA CATEGORIA NUEVA")

# La función get_categories recupera todos los registros de la tabla Categorias y los almacena en la variable categorias. 
# Luego, el bucle for itera sobre cada categoría y la imprime, mostrando todas las categorías registradas en la base de datos.
    # Obtener todas las categorías
    categorias = get_categories()
    for categoria in categorias:
        print(categoria)
    print("MUESTRA LOS DATOS DE LA TABLA CATEGORIA")

# La función delete_category elimina la categoría con ID igual a 2 de la tabla Categorias, 
# eliminando así el registro de la categoría de la base de datos.
    # Eliminar una categoría
    delete_category(2)
    print("ELIMINO UNA CATEGORIA")