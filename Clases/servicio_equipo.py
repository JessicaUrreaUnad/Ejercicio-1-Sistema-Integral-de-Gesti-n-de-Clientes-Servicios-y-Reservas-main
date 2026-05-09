from Clases.servicio import Servicio

class ServicioEquipo(Servicio):

    def __init__(self, nombre, costo, dias):
        super().__init__(nombre, costo)
        self.dias = dias

    def calcular_costo(self):
        return self.costo * self.dias

    def mostrar_servicio(self):
        print(f"Servicio Equipo: {self.nombre}")