from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.laptops_bs = []
        self.imagenes = ["E:\\programacion_Patsy\\Modulo4\\Class1\\img\\lp1.webp", "E:\\programacion_Patsy\\Modulo4\\Class1\\img\\lp2.webp", "E:\\programacion_Patsy\\Modulo4\\Class1\\img\\lp3.jpg", "E:\\programacion_Patsy\\Modulo4\\Class1\\img\\lp4.jpg", "E:\\programacion_Patsy\\Modulo4\\Class1\\img\\lp5.webp"]

        root.title("Ingresar Laptops Business")

        self.contenido()

    def contenido(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column= 1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column= 1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column= 1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column= 1)

        ttk.Label(self.root, text="Duracion de Bateria").grid(row=4, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column= 1)
        
        ttk.Label(self.root, text="Precio").grid(row=5, column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=5, column= 1)

        ttk.Button(self.root, text="+ Laptop", command=self.agregar_laptop).grid(row=6, column=0)
        
        self.mostrar_laptops = tk.Text(self.root, height= 10, width = 50)
        self.mostrar_laptops.grid(row=7, column=0, columnspan=2) 

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=7)

# marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10
    
    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(), self.almacenamiento.get(), self.duracion_bateria.get(), self.precio.get())
        self.laptops_bs.append(nueva_laptop)

        self.mostrar_laptops.insert(tk.END, nueva_laptop)

        self.mostrar_imagen_aleatorias()


    def mostrar_imagen_aleatorias(self):
        imagen_ruta = random.choice(self.imagenes)
        imagen = Image.open(imagen_ruta)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0,  anchor=tk.NW, image = foto)
        self.canva.image = foto 


        pass

root = tk.Tk()

interfaz = Interfaz(root) 
root.mainloop()

        