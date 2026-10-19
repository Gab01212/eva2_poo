from datetime import datetime

class Empleado:
    """Clase base que implementa encapsulamiento con atributos protegidos y privados."""
    def __init__(self, id_empleado: int, nombre: str, email: str, departamento: str):
        self.__id_empleado = id_empleado  # Atributo privado
        self._nombre = nombre             # Atributo protegido
        self._email = email
        self._departamento = departamento

    # Getters y Setters (Encapsulamiento y Protección de datos)
    def get_id_empleado(self):
        return self.__id_empleado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        if len(nombre.strip()) > 0:
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío.")

    def get_email(self):
        return self._email

    def obtener_info(self):
        return f"[ID: {self.__id_empleado}] Colaborador: {self._nombre} | Depto: {self._departamento}"


class TecnicoSostenible(Empleado):
    """Clase derivada que aplica herencia reutilizando la superclase."""
    def __init__(self, id_empleado: int, nombre: str, email: str, especialidad: str):
        super().__init__(id_empleado, nombre, email, departamento="Energías Renovables")
        self.__especialidad = especialidad

    def obtener_info(self):
        # Reutilización de código mediante polimorfismo y herencia
        info_base = super().obtener_info()
        return f"{info_base} | Especialidad: {self.__especialidad}"


class Proyecto:
    """Representa un proyecto de tecnología sostenible."""
    def __init__(self, id_proyecto: int, nombre_proyecto: str, presupuesto: float):
        self.__id_proyecto = id_proyecto
        self.__nombre_proyecto = nombre_proyecto
        self.__presupuesto = presupuesto
        self.__estado = "En Desarrollo"

    def get_id_proyecto(self):
        return self.__id_proyecto

    def get_nombre_proyecto(self):
        return self.__nombre_proyecto

    def get_presupuesto(self):
        return self.__presupuesto

    def cambiar_estado(self, nuevo_estado: str):
        self.__estado = nuevo_estado
