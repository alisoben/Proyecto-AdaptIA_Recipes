from core.api import GeminiAPI
from core.config import config

class RecetaGenerator:
    def __init__(self):
        self.api = GeminiAPI()
        
    def generar_receta(self, plato, restricciones):
        
        prompt = config.prompt_template.format(
                plato=plato,
                restricciones=restricciones
            )
        receta = self.api.generate_answer(prompt)
        return receta