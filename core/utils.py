def cargar_receta(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def guardar_receta(file_path, receta):
    with open(file_path, 'w') as file:
        file.write(receta)