import mysql.connector
from mysql.connector import Error

def conectar_bd():

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",              
            database="ecotech_db"     
        )
        if conexion.is_connected():
            print("¡Conexión exitosa a la base de datos MySQL de EcoTech Solutions!")
            return conexion
    except Error as e:
        print(f"Error crítico al conectar a la base de datos: {e}")
        return None