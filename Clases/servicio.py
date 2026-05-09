from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def mostrar_servicio(self):
        pass