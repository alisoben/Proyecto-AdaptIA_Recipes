import requests
from core.config import config

class GeminiAPI:
    def __init__(self):
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL

    def ajustar_receta(self, receta, dieta):
        endpoint = f'{self.base_url}/ajustar_receta'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        payload = {
            'receta': receta,
            'dieta': dieta
        }
        response = requests.post(endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
