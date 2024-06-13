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