from datetime import datetime


class Empleado:
    def __init__(self, id_empleado: int, nombre: str, email: str, departamento: str):
        self.__id_empleado = id_empleado  
        self._nombre = nombre             
        self._email = email
        self._departamento = departamento

    def get_id_empleado(self):
        return self.__id_empleado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def obtener_info(self):
        return f"[ID: {self.__id_empleado}] Empleado: {self._nombre} | Depto: {self._departamento}"


class TecnicoSostenible(Empleado):
    def __init__(self, id_empleado: int, nombre: str, email: str, especialidad: str):
        super().__init__(id_empleado, nombre, email, departamento="Energías Renovables")
        self.__especialidad = especialidad  # Atributo privado

    def get_especialidad(self):
        return self.__especialidad

    def obtener_info(self):
        info_base = super().obtener_info()
        return f"{info_base} | Especialidad Técnica: {self.__especialidad}"


class AdministradorSistema(Empleado):
    def __init__(self, id_empleado: int, nombre: str, email: str, nivel_acceso: str):
        super().__init__(id_empleado, nombre, email, departamento="TI y Ciberseguridad")
        self.__nivel_acceso = nivel_acceso

    def auditar_sistema(self):
        return f"El administrador {self._nombre} está auditando los registros de seguridad con nivel {self.__nivel_acceso}."


class Proyecto:
    def __init__(self, id_proyecto: int, nombre_proyecto: str, presupuesto: float):
        self.__id_proyecto = id_proyecto
        self.__nombre_proyecto = nombre_proyecto
        self.__presupuesto = presupuesto
        self.__estado = "En Desarrollo"

    def get_nombre_proyecto(self):
        return self.__nombre_proyecto

    def get_presupuesto(self):
        return self.__presupuesto

    def actualizar_estado(self, nuevo_estado: str):
        self.__estado = nuevo_estado
        return f"Proyecto '{self.__nombre_proyecto}' actualizado a estado: {self.__estado}"


class RegistroTiempos:
    def __init__(self, id_registro: int, empleado: Empleado, proyecto: Proyecto, horas_invertidas: float):
        self.__id_registro = id_registro
        self.__empleado = empleado      
        self.__proyecto = proyecto      
        self.__horas_invertidas = horas_invertidas
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d")

    def generar_detalle_tiempo(self):
        return (f"Registro #{self.__id_registro} - Colaborador: {self.__empleado.get_nombre()} "
                f"| Proyecto: {self.__proyecto.get_nombre_proyecto()} "
                f"| Horas: {self.__horas_invertidas} hrs ({self.__fecha_registro})")


class ReporteCorporativo:
    def __init__(self, id_reporte: int, tipo_reporte: str):
        self.__id_reporte = id_reporte
        self.__tipo_reporte = tipo_reporte

    def exportar_reporte(self):
        return f"Reporte corporativo #{self.__id_reporte} de tipo '{self.__tipo_reporte}' generado y validado con éxito."