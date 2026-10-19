import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """
    Establece la conexión a la base de datos MySQL utilizando la librería oficial mysql-connector-python.
    Ajusta los valores de host, user, password y database según tu configuración.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="evaluacion_poo" 
        )
        if conexion.is_connected():
            print("¡Conexión exitosa a la base de datos MySQL!")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None