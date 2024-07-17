from core.api import GeminiAPI
import os
from dotenv import load_dotenv

class RecetaGenerator:
    def __init__(self):
        load_dotenv()
        self.api = GeminiAPI()
        self.prompt_template = """
            Adaptar el platillo: {plato} según las indicaciones y restricciones: {restricciones}.
            Mencionar los ingredientes adaptados y las instrucciones para su preparación.
            Eres un nutricionista que adapta los platillos que le gustan a sus clientes de forma que cambia los elementos, sus proporciones y procesos de preparación para cumplir con la restricción.
            Generar solo una pequeña introducción al platillo, la lista de ingredientes adaptados, las instrucciones para la preparación y algunas notas adicionales para sugerencias. Usa un tono educado y formal.
            El texto se utilizara para un programa, por lo que quiero que seas directo, y solo brindes lo que te indique, sin ningun titulo extra.
            Utiliza únicamente platillos reales y bien conocidos. Verifica que {plato} sea un platillo real antes de proceder.
            Por ejemplo, para el platillo Lomo Saltado con la restricción Dieta, los ingredientes que generará son:
            Ingredientes:
            - 100g Tofu (en lugar de carne)
            - 1 cebolla roja grande, cortada en gajos
            - 2 tomates medianos, cortados en gajos
            - 1 pimiento (rojo o amarillo), cortado en tiras
            - 1 taza de quinua cocida (opcional)
            Además, proporciona un análisis nutricional detallado en items al final de la receta respecto al platillo generado, incluyendo calorías, proteínas, grasas y carbohidratos.
        """
        
        
        
        
    def generar_receta(self, plato, restricciones):
        prompt = self.prompt_template.format(
                plato=plato,
                restricciones=restricciones
            )
        receta = self.api.generate_answer(prompt)
        return receta