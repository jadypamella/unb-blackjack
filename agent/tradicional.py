import pandas as pd
from data.file import File

# classe para sugestoes tradicionais
class AgenteTradicional():

    def __init__(self, player, dealer):
        self.name = "Tradicional"
        self.nickname = "trad"
        self.filename = "tradicional.csv"

        #print("Jogador: \n"+player.dataframe.to_string()+"\n")
        self.get_data()

       # data = pd.read_csv(self.data_file)
        #data = pd.read_csv(self.data_file)
        #print(data)

    def agent_suggestion(self):
        #suggestion_list = ['Hit', 'Stand']
        #suggestion = random.choice(suggestion_list)
        #return suggestion
        pass

    def get_data(self):
        file = File(self.filename)
        #arquivo.fileInfo()
        
        df = file.getCSVasDataframe()
        print(df)
        return df
        