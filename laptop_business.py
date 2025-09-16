from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Almacenamiento: {self.almacenamiento}\n Duracion de Bateria: {self.duracion_bateria}\n Costo: {self.costo}\n Impuesto: {self.impuesto}\n"


    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_diagnostico ["CAPACIDAD DE ALMACENAMIENTO"] = self.almacenamiento
        resultado_diagnostico ["DURACION DE BATERIA"] = self.duracion_bateria
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico ["Mas Detalles"] = resultado_conectividad
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        verificado = {
            "DISPONIBILIDAD WIFI" : "SI" if random.choice([True,False]) else "NO",
            "ACCESO A SERVIDORES EMEPRESARIALES" : "SI" if random.choice([True, False]) else "NO"
        }
        return verificado
    
    pass
