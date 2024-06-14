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