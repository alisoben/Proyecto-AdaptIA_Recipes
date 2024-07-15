import os
class Config:
    API_KEY = os.getenv('AIzaSyCXuGoSxdR4njzo3JMX4yPaDGv0e_6oIbc')
    BASE_URL = 'https://api.gemini.com/v1/' 

config = Config()