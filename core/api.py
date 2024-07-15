from core.config import config
import google.generativeai as genai

class GeminiAPI:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            if not config.API_KEY:
                raise ValueError("API Key esta faltando en la configuración.")
            genai.configure(api_key=config.API_KEY)
            self.initialized = True
        
    def generar_receta(self, plato, restricciones):
        genai.configure(api_key=config.API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt_template = """
            Adaptar el platillo: {plato} según las indicaciones y restricciones: {restricciones}.
            Mencionar los ingredientes y las instrucciones para su preparación.
            Eres un nutricionista que adapta los platillos que le gustan a sus clientes de forma que cambia elementos y procesos de preparación para cumplir con la restricción.
            Generar solo una pequeña introducción al platillo, la lista de ingredientes adaptados, las instrucciones para la preparación y algunas notas adicionales para sugerencias. Usa un tono educado y formal.
            El texto se utilizara para un programa, por lo que quiero que seas directo, y solo brindes lo que te indique, sin ningun titulo extra.
            Por ejemplo, para el platillo Lomo Saltado con la restricción Dieta, los ingredientes que generará son:
            Ingredientes:
            - 400g Tofu
            - 1 cebolla roja grande, cortada en gajos
            - 2 tomates medianos, cortados en gajos
            - 1 pimiento (rojo o amarillo), cortado en tiras
            - 2 dientes de ajo, picados
            - 1 taza de quinua cocida (opcional, para acompañar)
        """
        prompt = prompt_template.format(plato=plato, restricciones=restricciones)
        response = model.generate_content(prompt)
        receta = response.text if hasattr(response, 'text') else str(response)
        return receta