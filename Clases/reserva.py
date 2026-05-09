class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):
        print("===== RESERVA =====")
        self.cliente.mostrar_info()
        self.servicio.mostrar_servicio()
        print(f"Estado: {self.estado}")