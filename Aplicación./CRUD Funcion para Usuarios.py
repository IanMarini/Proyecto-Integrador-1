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