import os
import tkinter as tk
from tkinter import font as tkFont, messagebox, ttk
from PIL import Image, ImageTk
from core.api import GeminiAPI
import markdown2

class InteraccionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recetas Personalizadas")
        self.root.geometry("1080x720")

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
        self.frame_output.pack(pady=10, fill='both', expand=True)  # Aumentar tamaño del marco

        # Texto para mostrar la receta adaptada en formato Markdown
        self.receta_text = tk.Text(self.frame_output, height=20, width=120, bg=self.tertiary_color, fg=self.text_color, font=self.custom_font, wrap='word', borderwidth=2, relief='solid')
        self.receta_text.pack(pady=5, padx=20, fill='both', expand=True)  # Expandir para llenar el marco
        self.receta_text.config(state=tk.DISABLED)  # Hacer que el texto sea de solo lectura

        # Crear un marco para los campos de entrada
        self.frame_input = tk.Frame(root, bg=self.background_color)
        self.frame_input.pack(pady=20, side=tk.LEFT, fill=tk.Y)

        # Crear etiquetas y entradas para el nombre del platillo y las restricciones
        self.plato_label = tk.Label(self.frame_input, text="Nombre del platillo:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.plato_label.grid(row=0, column=0, pady=5, padx=5, sticky='e')
        self.plato_entry = ttk.Entry(self.frame_input, width=30, font=self.custom_font, style="TEntry")
        self.plato_entry.grid(row=0, column=1, pady=5, padx=5, sticky='w')

        self.restricciones_label = tk.Label(self.frame_input, text="Restricciones:", bg=self.background_color, fg=self.text_color, font=self.custom_font_bold)
        self.restricciones_label.grid(row=1, column=0, pady=5, padx=5, sticky='e')
        self.restricciones_entry = ttk.Entry(self.frame_input, width=30, font=self.custom_font, style="TEntry")
        self.restricciones_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')

        # Botón para adaptar receta
        self.adaptar_button = tk.Button(self.frame_input, text="Adaptar", command=self.adaptar_receta, font=self.custom_font, bg=self.primary_color, fg=self.entry_background_color, activebackground=self.active_button_color, activeforeground=self.entry_background_color, borderwidth=0, highlightthickness=0, padx=20, pady=10)
        self.adaptar_button.grid(row=2, columnspan=2, pady=20)

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
        self.gemini_api = GeminiAPI()

    def load_logo(self, path):
        # Cargar la imagen del logo
        image = Image.open(path)
        image = image.resize((50, 50), Image.LANCZOS)  # Redimensionar imagen del logo si es necesario
        self.logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(self.title_frame, image=self.logo, bg=self.background_color)

    def adaptar_receta(self):
        plato = self.plato_entry.get()
        restricciones = self.restricciones_entry.get()

        # Llamar a la API para adaptar receta
        try:
            receta_adaptada = "Receta adaptada para {} con las siguientes restricciones: {}\n".format(plato, restricciones)
            receta_adaptada += self.gemini_api.generar_receta(plato, restricciones)

            # Convertir el texto Markdown a HTML para mostrarlo en el widget Text
            html_content = markdown2.markdown(receta_adaptada)
            self.insert_text_with_animation(html_content)

        except Exception as e:
            self.insert_text_with_animation("Error al adaptar la receta!!!")
            print(f"Error al adaptar la receta: {e}")

    def insert_text_with_animation(self, content):
        # Anima la inserción de texto en el widget Text
        self.receta_text.config(state=tk.NORMAL)
        self.receta_text.delete(1.0, tk.END)
        self.receta_text.insert(tk.END, content)
        self.receta_text.config(state=tk.DISABLED)

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
