import tkinter as tk
from tkinter import ttk

class InteraccionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interacción Simple")
        self.root.geometry("400x200")

        # Crear un marco para el contenido principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(expand=True)

        # Crear etiqueta de saludo
        self.hola_label = ttk.Label(self.frame, text="Hola", font=("Helvetica", 24))
        self.hola_label.pack(pady=20)

        # Botón de saludo
        self.hola_button = ttk.Button(self.frame, text="Saludar", command=self.mostrar_hola)
        self.hola_button.pack(pady=10)

    def mostrar_hola(self):
        self.hola_label.config(text="¡Hola Mundo!")

