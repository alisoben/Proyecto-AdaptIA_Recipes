import tkinter as tk
from tkinter import font as tkFont, messagebox
from PIL import Image, ImageTk

class InteraccionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recetas Personalizadas")
        self.root.geometry("1080x720")

        self.primary_color = '#17252A'  # Color muy oscuro
        self.secondary_color = '#2B7A78'  # Color medio
        self.tertiary_color = '#3AAFA9'  # Color claro
        self.background_color = '#FEFFFF'  # Color muy claro
        self.entry_background_color = '#FEFFFF'  # Blanco muy claro
        self.text_color = '#17252A'  # Mismo color muy oscuro para texto
        self.text_entry_color = '#17252A'  # Mismo color muy oscuro para texto de entrada
        self.active_button_color = '#2B7A78'  # Color medio para el estado activo del botón

        self.root.configure(bg=self.background_color)

        # Elegir una fuente
        font_family = "Arial"
        self.custom_font = tkFont.Font(family=font_family, size=12)
        self.custom_font_bold = tkFont.Font(family=font_family, size=12, weight="bold")
        self.custom_font_title = tkFont.Font(family=font_family, size=24, weight="bold")

        # Título de la aplicación con el logo
        self.title_frame = tk.Frame(root, bg=self.background_color)
        self.title_frame.pack(pady=20)

        # Cargar y mostrar la imagen del logo
        self.logo_path = "/Users/Amy/Downloads/IA_GEN_RECETAS/assets/logo.jpg"  # Ruta de la imagen del logo
        self.load_logo(self.logo_path)

        self.logo_label.pack(side=tk.LEFT, padx=10)  # Ajusta el padding según sea necesario

        self.title_label = tk.Label(self.title_frame, text="Recetas Personalizadas", bg=self.background_color, fg=self.primary_color, font=self.custom_font_title)
        self.title_label.pack(side=tk.LEFT)

        # Crear un marco para mostrar la receta adaptada
        self.frame_output = tk.Frame(root, bg=self.background_color)
        self.frame_output.pack(pady=10)

        # Texto para mostrar la receta adaptada
        self.receta_text = tk.Text(self.frame_output, height=15, width=100, bg=self.tertiary_color, fg=self.text_color, font=self.custom_font)
        self.receta_text.pack(pady=5)

        # Crear un marco para los campos de entrada
        self.frame_input = tk.Frame(root, bg=self.background_color)
        self.frame_input.pack(pady=20)

        # Crear etiquetas y entradas para el nombre del platillo y las restricciones
        self.plato_label = tk.Label(self.frame_input, text="Nombre del platillo:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.plato_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        self.plato_entry = tk.Entry(self.frame_input, width=50, font=self.custom_font, bg=self.entry_background_color, fg=self.text_entry_color, highlightbackground=self.secondary_color, highlightthickness=1)
        self.plato_entry.grid(row=1, column=0, pady=5, padx=5, sticky='w')

        self.restricciones_label = tk.Label(self.frame_input, text="Restricciones:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.restricciones_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        self.restricciones_entry = tk.Entry(self.frame_input, width=50, font=self.custom_font, bg=self.entry_background_color, fg=self.text_entry_color, highlightbackground=self.secondary_color, highlightthickness=1)
        self.restricciones_entry.grid(row=3, column=0, pady=5, padx=5, sticky='w')

        # Botón para adaptar receta
        self.adaptar_button = tk.Button(root, text="Adaptar", command=self.adaptar_receta, font=self.custom_font, bg=self.primary_color, fg=self.entry_background_color, activebackground=self.active_button_color, activeforeground=self.entry_background_color)
        self.adaptar_button.pack(pady=20)

        # Barra de menús
        self.menu_bar = tk.Menu(root, bg=self.primary_color, fg=self.background_color)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.primary_color, fg=self.background_color)
        self.menu_bar.add_command(label="Salir", command=root.quit)

        # Menú Ayuda
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.primary_color, fg=self.background_color)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        self.help_menu.add_command(label="Instrucciones", command=self.show_about)

    def load_logo(self, path):
        # Cargar la imagen del logo
        image = Image.open(path)
        image = image.resize((50, 50), Image.LANCZOS)  # Redimensionar imagen del logo si es necesario
        self.logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(self.title_frame, image=self.logo, bg=self.background_color)

    def adaptar_receta(self):
        plato = self.plato_entry.get()
        restricciones = self.restricciones_entry.get()

        # Lógica para adaptar receta
        receta = "Receta adaptada para {} con las siguientes restricciones: {}".format(plato, restricciones)
        self.receta_text.delete(1.0, tk.END)
        self.receta_text.insert(tk.END, receta)

    def show_about(self):
        messagebox.showinfo("Instrucciones", "Adaptador de Recetas Personalizadas\n\n- Ingresar el platillo a adaptar\n- Ingresar las restricciones que considere")


