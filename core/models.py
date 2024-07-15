from core.api import GeminiAPI

class RecipeAdjuster:
    def __init__(self, api_client):
        self.api_client = api_client

    def ajustar_receta(self, receta, dieta):
        return self.api_client.ajustar_receta(receta, dieta)
