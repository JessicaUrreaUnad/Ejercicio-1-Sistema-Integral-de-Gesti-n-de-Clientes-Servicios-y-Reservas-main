from Clases.servicio import Servicio

class ServicioAsesoria(Servicio):

    def __init__(self, nombre, costo, sesiones):
        super().__init__(nombre, costo)
        self.sesiones = sesiones

    def calcular_costo(self):
        return self.costo * self.sesiones

    def mostrar_servicio(self):
        print(f"Servicio Asesoría: {self.nombre}")