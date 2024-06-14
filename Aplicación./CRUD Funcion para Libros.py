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