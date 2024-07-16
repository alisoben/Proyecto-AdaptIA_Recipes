from core.config import config
import google.generativeai as genai

class GeminiAPI:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        if not hasattr(self, 'initialized'):
            if not config.API_KEY:
                raise ValueError("API Key está faltando en la configuración.")
            genai.configure(api_key=config.API_KEY)
            self.initialized = True
            
    def generate_answer(self, prompt):
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        try: 
            response = model.generate_content(prompt, 
                                                generation_config=genai.types.GenerationConfig(
                                                    candidate_count = 1,
                                                    temperature = 0.5,
                                                )
                                            )
            answer = response.text if hasattr(response, 'text') else str(response)
            return answer
        except Exception as e:
                return f"Error en la generación de la respuesta: {str(e)}"