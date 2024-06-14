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