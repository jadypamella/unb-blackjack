import pandas as pd
from data.file import File

"""
Classe com as funcoes para sugestoes tradicionais
"""

class AgenteHistorico():

    def __init__(self, player, dealer):
        self.name = "Histórico"
        self.nickname = "hist"
        self.filename = "historico.csv"
        self.player = player
        self.dealer = dealer

        self.suggestion = self.agent_suggestion()

    def get_data(self):
        file = File(self.filename)
        return file.getCSVasDataframe()
        
    def agent_suggestion(self):
        
        # Definindo a coluna do player 
        player_hand_value = self.player.cardsum
        player_column = 'psumcards'
        
        # Definindo a coluna do dealer
        dealer_hand_value = self.dealer.cardsum
        dealer_column = 'dsumcards'

        # Obtendo as linhas da planilha historica que possuem a 
        data = self.get_data()

        suggestion = 'Error'
        count_loss = 0
        count_win = 0
        try: # localizando o valor do dataframe
        
            data_parameters = (data[player_column] == player_hand_value)# & (data[dealer_column] == dealer_hand_value)
            data_value = data.loc[data_parameters]

            count_pwinloss = data_value['pwinloss'].value_counts().to_frame()
            count_loss = count_pwinloss.loc['Loss', 'pwinloss']
            count_win = count_pwinloss.loc['Win', 'pwinloss']

            # Retornando a sugestao do agente
            if(count_loss >= count_win):
                suggestion = 'Hit'
            else:
                suggestion = 'Stand'

        except Exception as e:
            print(e)
             
        return suggestion
        