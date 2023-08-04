import tkinter as tk
from PIL import Image, ImageTk  # Instalar el módulo "Pillow" para trabajar con imágenes

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

# Crear ventana para editar review
ventana = tk.Tk()
ventana.title("Editar Review")

# Mostrar el nombre del lugar
lbl_nombre = tk.Label(ventana, text="Nombre del lugar:")
lbl_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.insert(tk.END, review_info["nombre"])
entry_nombre.pack(pady=5)

# Mostrar la reseña
lbl_reseña = tk.Label(ventana, text="Reseña:")
lbl_reseña.pack(pady=5)
entry_reseña = tk.Text(ventana, height=5, width=30)
entry_reseña.insert(tk.END, review_info["reseña"])
entry_reseña.pack(pady=5)

# Mostrar la foto del local
imagen = Image.open(review_info["foto"])
imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen a tus necesidades
foto = ImageTk.PhotoImage(imagen)
lbl_foto = tk.Label(ventana, image=foto)
lbl_foto.pack(pady=10)

# Botones para calificar y reservar
btn_calificar = tk.Button(ventana, text="Calificar", command=calificar)
btn_calificar.pack(pady=5)

btn_reservar = tk.Button(ventana, text="Reservar", command=reservar)
btn_reservar.pack(pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
