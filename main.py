from database import conectar_bd
from models import TecnicoSostenible, AdministradorSistema, Proyecto, RegistroTiempos, ReporteCorporativo

def main():
    print("=====================================================")
    print(" ECOTECH SOLUTIONS - GESTIÓN INTERNA (UNIDAD 2)      ")
    print("=====================================================\n")

    conexion = conectar_bd()

    print("\n--- 2. Instanciación de Clases y Principios POO ---")
    
    tecnico1 = TecnicoSostenible(101, "Gabriel Urra", "gabriel.urra@ecotech.cl", "Paneles Solares y Smart Grids")
    admin1 = AdministradorSistema(102, "Valeria Soto", "valeria.soto@ecotech.cl", "Nivel 3 - Avanzado")
    
    print(tecnico1.obtener_info())
    print(admin1.obtener_info())
    print(admin1.auditar_sistema())

    proyecto1 = Proyecto(50, "Granja Solar del Valle", 45000000.0)
    print(proyecto1.actualizar_estado("Fase de Pruebas"))

    registro1 = RegistroTiempos(1001, tecnico1, proyecto1, 7.5)
    print(registro1.generar_detalle_tiempo())

    reporte = ReporteCorporativo(99, "Eficiencia Operativa y Trazabilidad")
    print(reporte.exportar_reporte())

    if conexion and conexion.is_connected():
        conexion.close()
        print("\nConexión a la base de datos cerrada de forma limpia.")

if __name__ == "__main__":
    main()