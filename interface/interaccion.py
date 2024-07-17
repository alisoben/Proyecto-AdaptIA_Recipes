import os
import tkinter as tk
from tkinter import font as tkFont, messagebox, ttk
from PIL import Image, ImageTk
from core.models import RecetaGenerator
import markdown2
from tkhtmlview import HTMLLabel

class InteraccionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recetas Personalizadas")
        self.center_window(1080, 720)

        self.primary_color = '#00796B'  # Verde oscuro
        self.secondary_color = '#4DB6AC'  # Verde medio
        self.tertiary_color = '#B2DFDB'  # Verde claro
        self.background_color = '#FFFFFF'  # Blanco
        self.entry_background_color = '#FFFFFF'  # Blanco
        self.text_color = '#212121'  # Gris oscuro
        self.text_entry_color = '#212121'  # Gris oscuro
        self.active_button_color = '#4DB6AC'  # Verde medio para el estado activo del botón

        self.root.configure(bg=self.background_color)

        # Elegir una fuente
        font_family = "Arial"
        self.custom_font = tkFont.Font(family=font_family, size=12)
        self.custom_font_bold = tkFont.Font(family=font_family, size=12, weight="bold")
        self.custom_font_title = tkFont.Font(family=font_family, size=24, weight="bold")

        # Título de la aplicación con el logo
        self.title_frame = tk.Frame(root, bg=self.background_color)
        self.title_frame.pack(pady=20, side=tk.TOP, fill=tk.X)

        # Cargar y mostrar la imagen del logo
        self.logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.jpg')  # Ruta de la imagen del logo
        self.load_logo(self.logo_path)

        self.logo_label.pack(side=tk.LEFT, padx=10)  # Ajusta el padding según sea necesario

        self.title_label = tk.Label(self.title_frame, text="Recetas Personalizadas", bg=self.background_color, fg=self.primary_color, font=self.custom_font_title)
        self.title_label.pack(side=tk.LEFT)

        # Crear un marco para mostrar la receta adaptada
        self.frame_output = tk.Frame(root, bg=self.background_color)
        self.frame_output.pack(pady=5, fill='both', expand=True)  # Aumentar tamaño del marco

        # Texto para mostrar la receta adaptada
        self.receta_label = HTMLLabel(self.frame_output, html="", bg=self.tertiary_color, fg=self.text_color, font=self.custom_font)
        self.receta_label.pack(pady=0, padx=20, fill='both', expand=True)  # Expandir para llenar el marco

        # Crear un marco para los campos de entrada
        self.frame_input = tk.Frame(root, bg=self.background_color)
        self.frame_input.pack(pady=10, side=tk.LEFT, fill=tk.Y)

        # Crear etiquetas y entradas para el nombre del platillo y las restricciones
        self.plato_frame = tk.Frame(self.frame_input, bg=self.background_color)
        self.plato_frame.grid(row=0, column=0, pady=5, padx=(20, 5), sticky='ew')
        self.plato_label = tk.Label(self.plato_frame, text="Nombre del platillo:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.plato_label.pack(side=tk.LEFT)
        self.plato_entry = ttk.Entry(self.plato_frame, width=50, font=self.custom_font, style="TEntry")
        self.plato_entry.pack(side=tk.RIGHT, padx=(5, 0))

        self.restricciones_frame = tk.Frame(self.frame_input, bg=self.background_color)
        self.restricciones_frame.grid(row=1, column=0, pady=5, padx=(20, 5), sticky='ew')
        self.restricciones_label = tk.Label(self.restricciones_frame, text="Restricciones:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.restricciones_label.pack(side=tk.LEFT)
        self.restricciones_entry = ttk.Entry(self.restricciones_frame, width=50, font=self.custom_font, style="TEntry")
        self.restricciones_entry.pack(side=tk.RIGHT, padx=(5, 0))

        # Botón para adaptar receta
        self.adaptar_button = tk.Button(self.frame_input, text="Adaptar", command=self.adaptar_receta, font=self.custom_font, bg=self.primary_color, fg=self.entry_background_color, activebackground=self.active_button_color, activeforeground=self.entry_background_color, borderwidth=0, highlightthickness=0, padx=20, pady=10)
        self.adaptar_button.grid(row=0, column=2, rowspan=2, padx=185, pady=40, sticky='nsew')

        # Estilo para el botón redondeado
        self.adaptar_button.configure(borderwidth=0, relief='solid', highlightthickness=0)
        self.adaptar_button.bind("<Enter>", self.on_enter)
        self.adaptar_button.bind("<Leave>", self.on_leave)

        # Crear un estilo para ttk Entry
        style = ttk.Style()
        style.configure("TEntry", fieldbackground=self.entry_background_color, background=self.entry_background_color, foreground=self.text_entry_color, padding=5)
        style.map("TEntry", fieldbackground=[('active', self.tertiary_color)])

        # Barra de menús
        self.menu_bar = tk.Menu(root, bg=self.primary_color, fg=self.background_color, activebackground=self.tertiary_color, activeforeground=self.background_color)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.primary_color, fg=self.background_color)
        self.file_menu.add_command(label="Salir", command=root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        # Menú Ayuda
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.primary_color, fg=self.background_color)
        self.help_menu.add_command(label="Instrucciones", command=self.show_about)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        # Inicializar la API de Gemini
        self.recetaGenerator = RecetaGenerator()
        
        
    def center_window(self, width, height):
        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas x e y para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Ajustar la coordenada y para que la ventana se coloque más arriba
        y -= 50
        # Establecer la geometría de la ventana
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def load_logo(self, path):
        # Cargar la imagen del logo
        image = Image.open(path)
        image = image.resize((50, 50), Image.LANCZOS)  # Redimensionar imagen del logo si es necesario
        self.logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(self.title_frame, image=self.logo, bg=self.background_color)

    def adaptar_receta(self):
        plato = self.plato_entry.get()
        restricciones = self.restricciones_entry.get()
        if not plato.strip():
            self.insert_text_with_animation("Error: El campo 'Plato' no puede estar vacío.")
            return
        if not restricciones.strip():
            self.insert_text_with_animation("Error: El campo 'Restricciones' no puede estar vacío. Si no tiene restricciones, escriba 'Ninguna'.")
            return
        # Llamar a la API para adaptar receta
        receta_adaptada = "<h2>Receta adaptada para {} con las siguientes restricciones: {}</h2><br>".format(plato, restricciones)
        receta_adaptada += self.recetaGenerator.generar_receta(plato, restricciones)
        self.receta = receta_adaptada
        # Convertir el texto Markdown a HTML para mostrarlo en el widget HTMLLabel
        html_content = markdown2.markdown(receta_adaptada)

        self.receta_label.set_html(html_content)


    def show_about(self):
        messagebox.showinfo("Instrucciones", "Adaptador de Recetas Personalizadas\n\n- Ingresar el platillo a adaptar\n- Ingresar las restricciones que considere")

    def on_enter(self, event):
        event.widget['background'] = self.secondary_color

    def on_leave(self, event):
        event.widget['background'] = self.primary_color

if __name__ == "__main__":
    root = tk.Tk()
    app = InteraccionApp(root)
    root.mainloop()
