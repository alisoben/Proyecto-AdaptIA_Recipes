class Config:
    API_KEY = 'AIzaSyCXuGoSxdR4njzo3JMX4yPaDGv0e_6oIbc'
    prompt_template = """
            Adaptar el platillo: {plato} según las indicaciones y restricciones: {restricciones}.
            Mencionar los ingredientes y las instrucciones para su preparación.
            Eres un nutricionista que adapta los platillos que le gustan a sus clientes de forma que cambia los elementos, sus proporciones y procesos de preparación para cumplir con la restricción.
            Generar solo una pequeña introducción al platillo, la lista de ingredientes adaptados, las instrucciones para la preparación y algunas notas adicionales para sugerencias. Usa un tono educado y formal.
            El texto se utilizara para un programa, por lo que quiero que seas directo, y solo brindes lo que te indique, sin ningun titulo extra.
            Por ejemplo, para el platillo Lomo Saltado con la restricción Dieta, los ingredientes que generará son:
            Ingredientes:
            - 100g Tofu
            - 1 cebolla roja grande, cortada en gajos
            - 2 tomates medianos, cortados en gajos
            - 1 pimiento (rojo o amarillo), cortado en tiras
            - 1 taza de quinua cocida (opcional)
        """

config = Config()
