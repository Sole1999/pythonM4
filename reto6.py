
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


auto_Keyla = Auto("Audi", "NegroSLE", "2023")

print(auto_Keyla.__dict__)
print(auto_Keyla.mostrar_informacion())
print(auto_Keyla.actualizar_kilometraje(5))
print(auto_Keyla.realizar_viaje(30))
print(auto_Keyla.estado_auto())