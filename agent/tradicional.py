import random
import pandas as pd

from data.arquivo import Arquivo

# classe para sugestoes tradicionais
class AgenteTradicional():

    def __init__(self, player, dealer):
        self.name = "Tradicional"
        self.nickname = "trad"
        self.data_file = "tradicional.csv"

        #print("Jogador: \n"+player.dataframe.to_string()+"\n")
        print(self.get_data())

    def agent_suggestion(self):
        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
        return suggestion

    def get_data(self):
        arquivo = Arquivo(self.data_file)
        data_json = arquivo.getCSVasJSON()
        df = pd.read_json(data_json) # converte json para pandas dataframe
        return df