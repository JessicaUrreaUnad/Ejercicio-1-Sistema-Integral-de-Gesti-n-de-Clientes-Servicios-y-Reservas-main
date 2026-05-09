from Clases.servicio import Servicio

class ServicioSala(Servicio):

    def __init__(self, nombre, costo, horas):
        super().__init__(nombre, costo)
        self.horas = horas

    def calcular_costo(self):
        return self.costo * self.horas

    def mostrar_servicio(self):
        print(f"Servicio Sala: {self.nombre}")