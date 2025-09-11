from reto6 import Auto

auto_Keyla = Auto("Audi", "NegroSLE", "2023", 250)
auto_Javi = Auto("Ferrari", "   Murcielago", "2018", 7000)

metodo_clase = Auto.nuevo_carro()
print(metodo_clase.__dict__)

km_actualizado = Auto.actualizar_klmt(auto_Keyla, 6000)
print(km_actualizado)

print(Auto.comparar_kilometraje(auto_Keyla, auto_Javi))

print(Auto.medidor_km(auto_Javi, 41))


# print(auto_Keyla.__dict__)
# print(auto_Keyla.mostrar_informacion())
# print(auto_Keyla.actualizar_kilometraje(5))
# print(auto_Keyla.realizar_viaje(30))
# print(auto_Keyla.estado_auto())