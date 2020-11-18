import random

# classe para sugestoes aleatorias
class AgenteAleatorio():

    def __init__(self):
        self.name = "Aleatório"
        self.nickname = "alea"

    def agent_suggestion(self):
        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
        return suggestion