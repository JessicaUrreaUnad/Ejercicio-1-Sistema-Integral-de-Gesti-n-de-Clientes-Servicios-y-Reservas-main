from Clases.cliente import Cliente
from Clases.servicio_sala import ServicioSala
from Clases.servicio_equipo import ServicioEquipo
from Clases.servicio_asesoria import ServicioAsesoria
from Clases.reserva import Reserva

cliente1 = Cliente("Jessica", "3001234567")

cliente1.mostrar_info()
try:
    cliente2 = Cliente("", "")

except ValueError as error:
    print("Error:", error)

    with open("logs.txt", "a") as archivo:
        archivo.write(f"Error detectado: {error}\n")
        servicio1 = ServicioSala("Sala VIP", 50000, 2)
print("Costo Sala:", servicio1.calcular_costo())

servicio2 = ServicioEquipo("Computador", 30000, 3)
print("Costo Equipo:", servicio2.calcular_costo())

servicio3 = ServicioAsesoria("Python", 80000, 1)
print("Costo Asesoría:", servicio3.calcular_costo())

reserva1 = Reserva(cliente1, servicio1)

reserva1.confirmar()

reserva1.mostrar_reserva()
servicio1 = ServicioSala("Sala VIP", 50000, 2)
print("Costo Sala:", servicio1.calcular_costo())

servicio2 = ServicioEquipo("Computador", 30000, 3)
print("Costo Equipo:", servicio2.calcular_costo())

servicio3 = ServicioAsesoria("Python", 80000, 1)
print("Costo Asesoría:", servicio3.calcular_costo())

reserva1 = Reserva(cliente1, servicio1)

reserva1.confirmar()

reserva1.mostrar_reserva()