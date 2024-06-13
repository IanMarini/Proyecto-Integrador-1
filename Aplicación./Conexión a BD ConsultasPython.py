import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='4466',
        database='Gestion_Biblioteca'
    )
    return connection
print("===============================================")
print("---SE REALIZO LA CONEXCION DE MANERA EXITOSA---")
print("===============================================")



print("=====================")
print("FUNCIONES PARA LIBROS")
print("=====================")
# Funciones CRUD para Libros.
def add_book(titulo, autor, isbn, editorial, anio_publicacion, disponibilidad):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Libros (Titulo, Autor, ISBN, Editorial, Anio_Publicacion, Disponibilidad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (titulo, autor, isbn, editorial, anio_publicacion, disponibilidad))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion para TRAER Y MOSTRAR LOS DATOS DE LA TABLA LIBROS.
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Libros")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Funcion para ACTUALIZAR LIBROS.
def update_book(id, disponibilidad):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Libros SET Disponibilidad = %s WHERE ID = %s", (disponibilidad, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion para ELIMINAR LIBROS.
def delete_book(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Libros WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()



print("=======================")
print("FUNCIONES PARA USUARIOS")
print("=======================")
# Funciones CRUD para Usuarios
def add_user(nombre, direccion, telefono, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Usuarios (Nombre, Direccion, Telefono, Email)
        VALUES (%s, %s, %s, %s)
    """, (nombre, direccion, telefono, email))
    connection.commit()
    cursor.close()
    connection.close()
    
# Funcion para TRAER Y MOSTRAR LOS DATOS DE LA TABLA USUARIOS.
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Funcion para ACTUALIZAR USUARIOS.
def update_user(id, telefono):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Usuarios SET Telefono = %s WHERE ID = %s", (telefono, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion para ELIMINAR USUARIOS.
def delete_user_and_loans(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Eliminar préstamos asociados al usuario.
    cursor.execute("DELETE FROM Prestamos WHERE ID_Usuario = %s", (user_id,))
    connection.commit()
    print(f"Préstamos asociados al usuario con ID {user_id} eliminados")
    
    # Eliminar el usuario.
    cursor.execute("DELETE FROM Usuarios WHERE ID = %s", (user_id,))
    connection.commit()
    print(f"Usuario con ID {user_id} eliminado")
    
    cursor.close()
    connection.close()



print("========================")
print("FUNCIONES PARA PRESTAMOS")
print("========================")
# Funciones CRUD para Prestamos
def add_loan(id_libro, id_usuario, fecha_prestamo, fecha_devolucion=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Prestamos (ID_Libro, ID_Usuario, Fecha_Prestamo, Fecha_Devolucion)
        VALUES (%s, %s, %s, %s)
    """, (id_libro, id_usuario, fecha_prestamo, fecha_devolucion))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion para TRAER Y MOSTRAR LOS DATOS DE LA TABLA PRESTAMOS.
def get_loans():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT Prestamos.ID, Libros.Titulo, Usuarios.Nombre, Prestamos.Fecha_Prestamo, Prestamos.Fecha_Devolucion 
        FROM Prestamos
        JOIN Libros ON Prestamos.ID_Libro = Libros.ID
        JOIN Usuarios ON Prestamos.ID_Usuario = Usuarios.ID
    """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Funcion para ACTUALIZAR PRESTAMOS.
def update_loan(id, fecha_devolucion):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Prestamos SET Fecha_Devolucion = %s WHERE ID = %s", (fecha_devolucion, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion para ELIMINAR PRESTAMOS.
def delete_loan(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Prestamos WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()

print("=========================")
print("FUNCIONES PARA CATEGORIAS")
print("=========================")
# Funciones CRUD para Categorias
# Funcion para ACTUALIZAR PRESTAMOS.
def add_category(nombre):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Categorias (Nombre) VALUES (%s)", (nombre,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Categoría agregada: {nombre}")

# Funcion para TRAER Y MOSTRAR LOS DATOS DE LA TABLA PRESTAMOS.
def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Categorias")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print("Obteniendo todas las categorías")
    return result

# Funcion para ELIMINAR PRESTAMOS.
def delete_category(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Categorias WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Categoría con ID {id} eliminada")

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

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
