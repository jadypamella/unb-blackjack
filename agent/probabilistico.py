

"""
Classe com as funcoes para sugestoes probabilisticas
"""

class AgenteProbabilistico():

    def __init__(self, player, dealer, deck):
        self.name = "Probabilístico"
        self.nickname = "prob"
        self.player = player
        self.dealer = dealer
        self.deck = deck

    # Factorial of a positive integer n, denoted by n! is the product of all positive integers less than or equal to n
    def factorial(n):
        if n == 1: 
            return 1
        else:
            return n * factorial(n - 1)

    # A combination is a selection of items from a collection, such that (unlike permutations) the order of selection does not matter
    # This function is withou repetition 
    def combination(n, r):
        return (factorial(n) / (factorial(r) * (factorial(n - r))))

    def probability_info():

        # Probability of obtaining a natural blackjack
        # Outs = (4A + 410) * deck
        ...
        
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
        if dealer_has_ace:
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