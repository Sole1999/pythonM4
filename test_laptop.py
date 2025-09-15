from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)

#__dict__ este permite mostrar l inforacion o los parametros (atributos) de la clase

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")


# for numero in range(1, 1001):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


#print(Laptop.comparar_costo(laptop_pepito, laptop_maria))


#laptop_juanito = Laptop_Gaming("MSI", "i7", 64, 900, 20)
#print(laptop_juanito.costo)


# laptop_juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")

# print(laptop_juanito.realizar_diagnostico_sistema())


laptop_sara = Laptop_Business("MAC", "i9", 8, "24 GB", "5 HORAS")
print(laptop_sara.realizar_diagnostico_sistema())