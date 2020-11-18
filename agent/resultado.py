import random

# classe para avaliacao do resultado dos agentes analiticos
class AgenteResultado():

    def __init__(self):
        self.name = "Resultado"
        self.nickname = "resu"

    def agent_suggestion(self):
        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
        return suggestion