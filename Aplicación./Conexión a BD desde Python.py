import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='4466',
        database='Gestion_Biblioteca'
    )
    return connection

# Funciones CRUD para Libros
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

def get_libros():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Libros")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_book(id, disponibilidad):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Libros SET Disponibilidad = %s WHERE ID = %s", (disponibilidad, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_book(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Libros WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()

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

def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_user(id, telefono):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Usuarios SET Telefono = %s WHERE ID = %s", (telefono, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()

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

def update_loan(id, fecha_devolucion):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Prestamos SET Fecha_Devolucion = %s WHERE ID = %s", (fecha_devolucion, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_loan(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Prestamos WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()

# Funciones CRUD para Categorias
def add_category(nombre):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Categorias (Nombre) VALUES (%s)", (nombre,))
    connection.commit()
    cursor.close()
    connection.close()

def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Categorias")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def delete_category(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Categorias WHERE ID = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
