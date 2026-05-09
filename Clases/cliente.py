from Clases.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, nombre, telefono):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if telefono == "":
            raise ValueError("El teléfono no puede estar vacío")

        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Cliente: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
