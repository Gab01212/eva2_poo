import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """
    Establece la conexión a la base de datos MySQL utilizando la librería oficial.
    Incorpora manejo de excepciones (try-except) para capturar fallos de conexión.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",          # Ajusta tu contraseña si aplica
            database="ecotech_db"
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"[Error de Conexión] No se pudo conectar a la base de datos MySQL: {e}")
        return None

# ==========================================
# OPERACIONES CRUD CON MANEJO DE EXCEPCIONES
# ==========================================

def registrar_empleado_db(conexion, nombre, email, departamento):
    """Inserta un registro (Create) en la base de datos de forma segura."""
    if not conexion or not conexion.is_connected():
        print("[Error] No hay conexión activa a la base de datos.")
        return False
    
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO empleados (nombre, email, departamento) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, email, departamento))
        conexion.commit()
        print(f"[BD Éxito] Empleado '{nombre}' registrado correctamente en la base de datos.")
        cursor.close()
        return True
    except Error as e:
        print(f"[Error CRUD - Create] Falló el registro del empleado: {e}")
        return False

def consultar_empleados_db(conexion):
    """Consulta registros (Read) desde la base de datos."""
    if not conexion or not conexion.is_connected():
        return []
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_empleado, nombre, email, departamento FROM empleados")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except Error as e:
        print(f"[Error CRUD - Read] Falló la consulta: {e}")
        return []

def actualizar_proyecto_db(conexion, id_proyecto, nuevo_estado):
    """Actualiza un registro (Update) en la base de datos."""
    if not conexion or not conexion.is_connected():
        return False
    
    try:
        cursor = conexion.cursor()
        sql = "UPDATE proyectos SET estado = %s WHERE id_proyecto = %s"
        cursor.execute(sql, (nuevo_estado, id_proyecto))
        conexion.commit()
        print(f"[BD Éxito] Proyecto ID {id_proyecto} actualizado a estado '{nuevo_estado}'.")
        cursor.close()
        return True
    except Error as e:
        print(f"[Error CRUD - Update] Falló la actualización: {e}")
        return False

def eliminar_proyecto_db(conexion, id_proyecto):
    """Elimina un registro (Delete) de la base de datos."""
    if not conexion or not conexion.is_connected():
        return False
    
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM proyectos WHERE id_proyecto = %s"
        cursor.execute(sql, (id_proyecto,))
        conexion.commit()
        print(f"[BD Éxito] Proyecto ID {id_proyecto} eliminado correctamente.")
        cursor.close()
        return True
    except Error as e:
        print(f"[Error CRUD - Delete] Falló la eliminación: {e}")
        return False
