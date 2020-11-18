import random

# classe para sugestoes probabilisticas
class AgenteProbabilistico():

    def __init__(self):
        self.name = "Probabilístico"
        self.nickname = "prob"

    def agent_suggestion(self):
        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
        return suggestion