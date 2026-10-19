
class Persona:
    """Clase base (Superclase) que representa una persona."""
    def __init__(self, rut: str, nombre: str, email: str):
        self._rut = rut         
        self._nombre = nombre
        self._email = email

    def get_rut(self):
        return self._rut

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_email(self):
        return self._email

    def set_email(self, nuevo_email):
        self._email = nuevo_email

    def obtener_detalle(self):
        return f"RUT: {self._rut} | Nombre: {self._nombre} | Email: {self._email}"


class Usuario(Persona):
    """Clase derivada (Herencia) que extiende de Persona."""
    def __init__(self, rut: str, nombre: str, email: str, id_usuario: int, rol: str):
        super().__init__(rut, nombre, email)  
        self.__id_usuario = id_usuario        
        self.__rol = rol                      

    def get_id_usuario(self):
        return self.__id_usuario

    def get_rol(self):
        return self.__rol

    def set_rol(self, nuevo_rol):
        self.__rol = nuevo_rol

    def obtener_detalle(self):
        detalle_base = super().obtener_detalle()
        return f"[ID: {self.__id_usuario}] {detalle_base} | Rol: {self.__rol}"