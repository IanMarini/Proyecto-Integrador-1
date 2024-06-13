import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='4466',
        database='Gestion_Biblioteca'
    )
    return connection
print("===========================================")
print("SE REALIZO LA CONEXCION DE MANERA EXITOSA")
print("===========================================")


print("======================")
print("FUNCIONES PARA LIBROS")
print("======================")
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
# Funcion para traer y mostrar los datos de la Tabla Libros.
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Libros")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Funcion para actualizar libros.
def update_book(id, disponibilidad):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Libros SET Disponibilidad = %s WHERE ID = %s", (disponibilidad, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion eliminar libros.
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
    
# Funcion para traer y mostrar los datos de la Tabla Usuarios.
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Funcion actualizar usuario.
def update_user(id, telefono):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Usuarios SET Telefono = %s WHERE ID = %s", (telefono, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion eliminar usuario.
def delete_user_and_loans(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Eliminar préstamos asociados al usuario
    cursor.execute("DELETE FROM Prestamos WHERE ID_Usuario = %s", (user_id,))
    connection.commit()
    print(f"Préstamos asociados al usuario con ID {user_id} eliminados")
    
    # Eliminar el usuario
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

# Funcion para traer y mostrar los datos de la Tabla Prestamos.
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

# Funcion actualizar prestamos.
def update_loan(id, fecha_devolucion):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Prestamos SET Fecha_Devolucion = %s WHERE ID = %s", (fecha_devolucion, id))
    connection.commit()
    cursor.close()
    connection.close()

# Funcion eliminar prestamos.
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
def add_category(nombre):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Categorias (Nombre) VALUES (%s)", (nombre,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Categoría agregada: {nombre}")

def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Categorias")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print("Obteniendo todas las categorías")
    return result

def delete_category(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Categorias WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Categoría con ID {id} eliminada")





if __name__ == "__main__":
    # Agregar un libro
    add_book('El Alquimista', 'Paulo Coelho', '978-0061122415', 'HarperOne', 1993, True)

    # Obtener todos los libros
    libros = get_books()
    for libro in libros:
        print(libro)

    # Actualizar la disponibilidad de un libro
    update_book(1, False)

    # Eliminar un libro
    delete_book(2)

    # Agregar un usuario
    add_user('Pedro Gonzales', 'Calle Flores 789, Ciudad', '111-2222', 'pedro.gonzales@example.com')

    # Obtener todos los usuarios
    usuarios = get_users()
    for usuario in usuarios:
        print(usuario)

    # Actualizar el teléfono de un usuario
    update_user(1, '351-6623038')

    # Eliminar un usuario
    delete_user_and_loans(2)

    # Agregar un préstamo
    add_loan(1, 1, '2024-06-01')

    # Obtener todos los préstamos
    prestamos = get_loans()
    for prestamo in prestamos:
        print(prestamo)

    # Actualizar la fecha de devolución de un préstamo
    update_loan(1, '2024-06-10')

    # Eliminar un préstamo
    delete_loan(2)

    # Agregar una categoría
    add_category('Ficción')

    # Obtener todas las categorías
    categorias = get_categories()
    for categoria in categorias:
        print(categoria)

    # Eliminar una categoría
    delete_category(2)
