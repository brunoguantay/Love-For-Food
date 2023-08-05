import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Datos de ejemplo (puedes reemplazarlos con tus propios datos)
review_info = {
    "nombre": "Restaurante A",
    "reseña": "Excelente lugar, comida deliciosa.",
    "foto": "ruta/a/tu/foto.jpg"  # Reemplaza con la ruta de tu foto descargada
}

# Funciones para calificar y reservar
def calificar():
    # Aquí puedes escribir el código para manejar la acción de calificar
    print("Calificar")

def reservar():
    # Aquí puedes escribir el código para manejar la acción de reservar
    print("Reservar")

# Crear ventana para la reseña detallada
ventana = tk.Tk()
ventana.title("Reseña Detallada")

# Marco para la imagen y la reseña
marco = ttk.Frame(ventana, padding=10)
marco.pack()

# Mostrar la imagen del local
imagen = Image.open(review_info["foto"])
imagen = imagen.resize((300, 200))  # Ajusta el tamaño de la imagen a tus necesidades
foto = ImageTk.PhotoImage(imagen)
lbl_foto = ttk.Label(marco, image=foto)
lbl_foto.pack()

# Mostrar la reseña
lbl_reseña = ttk.Label(marco, text=review_info["reseña"], wraplength=300, font=("Arial", 12))
lbl_reseña.pack(pady=10)

# Botones para calificar y reservar
boton_calificar = ttk.Button(marco, text="Calificar", command=calificar)
boton_calificar.pack(side=tk.LEFT, padx=5)

boton_reservar = ttk.Button(marco, text="Reservar", command=reservar)
boton_reservar.pack(side=tk.RIGHT, padx=5)

# Iniciar el bucle de eventos
ventana.mainloop()
