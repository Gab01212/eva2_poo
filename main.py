from database import conectar_bd
from models import Usuario

def main():
    print("--- INICIANDO PRUEBA DE EVALUACIÓN POO ---")
    
    conexion = conectar_bd()

    usuario_prueba = Usuario(
        rut="12.345.678-9",
        nombre="Gabriel Urra",
        email="gabriel@example.com",
        id_usuario=1,
        rol="Administrador"
    )

    print("\nInformación del Objeto Instanciado:")
    print(usuario_prueba.obtener_detalle())


    if conexion and conexion.is_connected():
        conexion.close()
        print("\nConexión a MySQL cerrada correctamente.")

if __name__ == "__main__":
    main()