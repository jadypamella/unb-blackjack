import pandas as pd
from data.file import File

"""
Classe com as funcoes para sugestoes tradicionais
"""

class AgenteTradicional():

    def __init__(self, player, dealer):
        self.name = "Tradicional"
        self.nickname = "trad"
        self.filename = "tradicional.csv"
        self.player = player
        self.dealer = dealer

        self.suggestion = self.agent_suggestion()

    def get_data(self):
        file = File(self.filename)
        return file.getCSVasDataframe()
        
    def agent_suggestion(self):
        
        # Definindo a coluna do player 
        player_hand_value = self.player.cardsum
        player_has_ace = self.player.has_ace

        player_column = '0A'+str(player_hand_value)
        if player_has_ace:
            player_column = '1A'+str(player_hand_value-11)
        
        # Definindo a coluna do dealer
        dealer_hand_value = self.dealer.cardsum
        dealer_has_ace = self.dealer.has_ace

        dealer_column = '0A'+str(dealer_hand_value)
        if dealer_has_ace or dealer_column == '0A1':
            dealer_column = '1A0'

        # Resgatando o padrao da planilha tradicional de sugestao de acoes 
        data = self.get_data()
        data = data.set_index('States')

        suggestion = 'Error'
        try: # localizando o valor do dataframe
            data_value = data.loc[player_column, dealer_column] 

            # Retornando a sugestao do agente
            if(data_value == 1):
                suggestion = 'Hit'
            else:
                suggestion = 'Stand'

        except Exception as e:
            print ('Chave '+str(e)+' não encontrada na tabela de sugestões do agente tradicional.')
             
        return suggestion
        