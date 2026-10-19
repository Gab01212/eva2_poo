from database import conectar_bd, registrar_empleado_db, actualizar_proyecto_db
from models import TecnicoSostenible, Proyecto

def validar_entrada_numerica(mensaje):
    """Valida que el usuario ingrese un número válido sin romper el programa."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("[Aviso] El valor no puede ser negativo. Intente nuevamente.")
                continue
            return valor
        except ValueError:
            print("[Error de Validación] Entrada inválida. Debe ingresar un número.")

def validar_texto_no_vacio(mensaje):
    """Valida que la entrada de texto no esté en blanco."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0:
            return texto
        print("[Error de Validación] El campo no puede estar vacío.")

def main():
    print("=====================================================")
    print(" ECOTECH SOLUTIONS - SISTEMA INTEGRADO (EVALUACIÓN)  ")
    print("=====================================================\n")

    # 1. Establecer Conexión a Base de Datos con Manejo de Excepciones
    conexion = conectar_bd()
    if not conexion:
        print("[Aviso del Sistema] Operando en modo desconectado debido a un error de red o BD.")

    print("\n--- 2. Demostración de Programación Orientada a Objetos ---")
    try:
        # Validación de entradas simuladas / interactivas seguras
        nombre_ingresado = "Gabriel Urra"
        email_ingresado = "gabriel.urra@ecotech.cl"
        
        tecnico1 = TecnicoSostenible(101, nombre_ingresado, email_ingresado, "Eficiencia Energética")
        print(tecnico1.obtener_info())

        proyecto1 = Proyecto(1, "Parque Solar Los Álamos", 50000000.0)

        # 3. Demostración de Operaciones CRUD y Manejo de Errores
        if conexion and conexion.is_connected():
            print("\n--- Ejecutando Operaciones CRUD en Base de Datos ---")
            
            # CREATE (Registrar)
            registrar_empleado_db(conexion, tecnico1.get_nombre(), email_ingresado, "Energías Renovables")
            
            # UPDATE (Actualizar)
            actualizar_proyecto_db(conexion, proyecto1.get_id_proyecto(), "Completado")
            
            conexion.close()
            print("\nConexión cerrada de forma segura.")

    except Exception as e:
        print(f"[Excepción Crítica Detectada] Ocurrió un error inesperado en la ejecución: {e}")

if __name__ == "__main__":
    main()