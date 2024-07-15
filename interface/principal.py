import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from interface.interaccion import InteraccionApp

class PantallaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla Inicial")
        self.root.geometry("1080x720")  # Ajusta el tamaño según tus necesidades

        # Nueva paleta de colores
        self.primary_color = '#17252A'  # Color muy oscuro
        self.secondary_color = '#2B7A78'  # Color medio
        self.tertiary_color = '#3AAFA9'  # Color claro
        self.background_color = '#FEFFFF'  # Color muy claro
        self.entry_background_color = '#FEFFFF'  # Blanco muy claro
        self.text_color = '#17252A'  # Mismo color muy oscuro para texto
        self.text_entry_color = '#17252A'  # Mismo color muy oscuro para texto de entrada
        self.active_button_color = '#2B7A78'  # Color medio para el estado activo del botón

        self.root.configure(bg=self.background_color)

        self.inicio_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.jpg')
        self.load_image(self.inicio_path)

        # Crear marcos para organizar la disposición
        self.top_frame = tk.Frame(root, bg=self.background_color)
        self.top_frame.pack(expand=True, fill="both")

        self.middle_frame = tk.Frame(root, bg=self.background_color)
        self.middle_frame.pack(expand=True, fill="both")

        self.bottom_frame = tk.Frame(root, bg=self.background_color)
        self.bottom_frame.pack(expand=True, fill="both")

        # Etiqueta para mostrar la imagen
        self.image_label = tk.Label(self.top_frame, image=self.image, bg=self.background_color)
        self.image_label.pack(pady=20)

        # Etiquetas para el texto
        self.label1 = tk.Label(self.middle_frame, text="Recetas hechas a medida", font=("Arial", 36, "bold"), bg=self.background_color, fg=self.primary_color)
        self.label1.pack(pady=(20, 10))
        
        self.label2 = tk.Label(self.middle_frame, text="Introduce los ingredientes que tienes y tus restricciones alimenticias.", font=("Arial", 22), bg=self.background_color, fg=self.primary_color)
        self.label2.pack(pady=(0, 10))

        self.label3 = tk.Label(self.middle_frame, text="Nuestra IA te ofrecerá recetas adaptadas a ti.", font=("Arial", 16), bg=self.background_color, fg=self.primary_color)
        self.label3.pack(pady=(0, 10))

        self.label3 = tk.Label(self.middle_frame, text="Tu receta personalizada en segundos.", font=("Arial", 16), bg=self.background_color, fg=self.primary_color)
        self.label3.pack(pady=(0, 50))

        # Botón para iniciar la interfaz de interacción
        self.button = tk.Button(self.bottom_frame, text="Iniciar", command=self.abrir_interaccion, font=("Arial", 20), bg=self.secondary_color, fg=self.entry_background_color, activebackground=self.active_button_color, activeforeground=self.entry_background_color)
        self.button.pack(pady=50, expand=True, ipady=20, ipadx=40)  # Hacer el botón más grande

    def load_image(self, path):
        # Cargar la imagen y redimensionar para que se ajuste
        image = Image.open(path)
        image = image.resize((100, 100), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        self.image = ImageTk.PhotoImage(image)

    def abrir_interaccion(self):
        # Cierra la ventana actual y abre la interfaz de interacción
        self.root.destroy()
        root = tk.Tk()
        app = InteraccionApp(root)
        root.mainloop()

def main():
    root = tk.Tk()
    app = PantallaInicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()