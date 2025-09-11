
class Auto:
    def __init__(self, marca, modelo, anio, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        return self.marca , self.modelo, self.anio
    
    def actualizar_kilometraje(self, nuevo):
        if(nuevo > self.kilometraje):
            #return self.kilometraje + nuevo
            self.kilometraje += nuevo
            print(f"Se ha actualizado el kilometraje a {self.kilometraje} km.")
        else:
            print("No se puede reducir el kilometraje")
    
    def realizar_viaje(self, kilometros):
        if(kilometros >= 0):
            self.kilometraje += kilometros
            print(f"Se han recorrido {kilometros} km. El kilometraje actual es: {self.kilometraje} km")
        else:
            print("La cantidad debe ser numeros positivos.")

    def estado_auto(self):
        if(self.kilometraje < 20000):
            print("Estoy como nuevo.")
        elif(self.kilometraje >= 20000 and self.kilometraje <= 100000):
            print("Ya estoy usado.")
        else:
            print("¡Ya dejame descansar por favor!")


    #Metodo de Clase
    @classmethod
    def nuevo_carro (cls):
        marca = "Toyota"
        modelo = "VTS-554"
        anio = "2025"
        return cls(marca, modelo, anio)
    
    
    @classmethod
    def actualizar_klmt(cls, carro, kilometraje):
        if(kilometraje > 0):
            carro.kilometraje += kilometraje
            print(f"Se ha actualizado el kilometraje a {carro.kilometraje} km.")
        else:
            print("No se puede reducir el kilometraje")


    #Metodo Estatico
    @staticmethod
    def comparar_kilometraje (kmt1, kmt2):
        if(kmt1.kilometraje == kmt2.kilometraje):
            return "Los dos autos tienen el mismo kilometraje."
        return "No tienen el mismo kilometraje."
    
    @staticmethod
    def medidor_km(auto, km):
        if km >= 0:
            auto.kilometraje += km
            print(f"Se han recorrido {km} km. El kilometraje actual es: {auto.kilometraje} km")
        else:
            print("La cantidad debe ser numeros positivos.")