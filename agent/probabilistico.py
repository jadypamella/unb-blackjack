

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

        self.suggestion = self.agent_suggestion()
        #self.probability_info()

    def probability_info(self):

        # Probability of obtaining a natural blackjack
        # Outs = (4A + 410) * deck
        #print(self.deck.dataframe)
        #print(self.deck.cards_total)
        #print(self.deck.cards_total_available)

        #self.player.card1 
        #self.player.card2
        #self.player.card3
        #self.player.card4 
        #self.player.card5
        #self.player.dataframe
        #self.player.cardsum 

        pass

    def probability_blackjack(self):
        pass

    def probability_bust(self):
        pass

    def probability_win_stand(self):    
        return 25

    def probability_lose_stand(self):      
        return 10

    def probability_win_hit(self):      
        return 20

    def probability_lose_hit(self):       
        return 10

    def agent_suggestion(self):

        '''
        - Pws: a probabilidade do jogador ganhar (win) a partida caso permaneça com a
        pontuação atual (stand);
        - Pls: a probabilidade do jogador perder (lose) a partida caso permaneça com a
        pontuação atual (stand);
        - Pwh: a probabilidade do jogador ganhar (win) a partida caso peça mais uma carta
        (hit);
        - Plh: a probabilidade do jogador perder (lose) a partida caso peça mais uma carta
        (hit);
        Temos que, caso a Pws - Pls seja maior que a Pwh - Plh, o agente deve sugerir a
        ação Stand, caso contrário, deve sugerir a ação Hit.
        '''

        suggestion = 'Error'
        try: # calculando a probabilidade
            
            pws = self.probability_win_stand()
            pls = self.probability_lose_stand()
            pwh = self.probability_win_hit()
            phs = self.probability_lose_hit()

            ps = pws - pls # probabilidade stand
            ph = pwh - phs # probabilidade hit

            # Retornando a sugestao do agente
            if(ph >= ps):
                suggestion = 'Hit'
            else:
                suggestion = 'Stand'

        except Exception as e:
            print(e)
             
        return suggestion