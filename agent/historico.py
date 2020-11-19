import random

"""
Classe com as funcoes para sugestoes historicas
"""

class AgenteHistorico():

    def __init__(self):
        self.name = "Histórico"
        self.nickname = "hist"

    def agent_suggestion(self):
        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
        return suggestion