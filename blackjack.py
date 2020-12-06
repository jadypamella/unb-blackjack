import pandas as pd
from agent.aleatorio import AgenteAleatorio
from agent.historico import AgenteHistorico
from agent.probabilistico import AgenteProbabilistico
from agent.resultado import AgenteResultado
from agent.tradicional import AgenteTradicional

'''
pcard1
pcard2
pcard3
pcard4
pcard5
psumcards
dcard1
dcard2
dcard3
dcard4
dcard5
dsumcards
pblkjck
pwinloss
pbustbeat
dbustbeat
qdeck
rwinprobability
rwinresult
ahistsuggestion
ahistchosen
ahistwinloss
aprobsuggestion
aprobchosen
aprobwinloss
atradsuggestion
atradchosen
atradwinloss
aaleasuggestion
aaleachosen
aaleawinloss
'''
  
# classe padrao de jogador ou dealer
class Player():

    def __init__(self, card1, card2, card3, card4, card5):
        self.has_ace = False
        self.busted = False
        self.card1 = self.card_value(card1)
        self.card2 = self.card_value(card2)
        self.card3 = self.card_value(card3)
        self.card4 = self.card_value(card4)
        self.card5 = self.card_value(card5)
        self.cardrank1 = card1
        self.cardrank2 = card2
        self.cardrank3 = card3
        self.cardrank4 = card4
        self.cardrank5 = card5
        self.dataframe = self.card_dataframe()
        self.cardsum = self.card_sum()

    def card_dataframe(self):
        cardrank = [self.cardrank1, self.cardrank2, self.cardrank3, self.cardrank4, self.cardrank5]
        cardvalue = [self.card1, self.card2, self.card3, self.card4, self.card5]
        data = {'Cards':cardrank,
                'Values':cardvalue}
        df = pd.DataFrame(data)
        return df

    def card_value(self, card):
        if card == 'A' or card == 'a' or card == 11 or card == 1:
            self.has_ace = True
            return 11
        elif card == 'T' or card == 't' or card == 'J' or card == 'j' or card == 'Q' or card == 'q' or card == 'K' or card == 'k':
            return 10
        else:
            return card

    def card_sum(self):
        cardssum = int(self.card1) + int(self.card2) + int(self.card3) + int(self.card4) + int(self.card5)

        if cardssum > 21:
            self.busted = True

        return cardssum

# classe dos baralhos
class Deck():
    def __init__(self, player, dealer, qdecks=1):
        self.player = player
        self.dealer = dealer
        self.qdecks = qdecks
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.ranks_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.cards_total = 0
        self.cards_total_available = 0
        self.ranks_total = 0
        self.ranks_available = []
        self.dataframe = {}

        # inicializando os valores
        self.cards_total = self.get_total_cards()
        self.ranks_total = self.get_total_ranks()
        self.dataframe = self.deck_dataframe()
        self.ranks_available = self.get_available_ranks()
        self.dataframe = self.ranks_available
        self.cards_total_available = self.get_total_cards_available()
        
    def get_total_cards(self):
        return len(self.suits) * len(self.ranks) * self.qdecks

    def get_total_cards_available(self):
        return self.dataframe['Available'].sum()

    def get_total_ranks(self):
        qtd_suits = len(self.suits) * self.qdecks
        qtd_ranks = [i * int(qtd_suits) for i in self.ranks]
        qtd_ranks_len = [len(i) for i in qtd_ranks]
        return qtd_ranks_len

    def deck_dataframe(self):
        data = {'Cards':self.ranks, 
                'Values':self.ranks_values, 
                'Total':self.ranks_total,
                'Available':self.ranks_total,
                }
        
        df = pd.DataFrame(data)
        return df

    def get_available_ranks(self):
        pcards = self.player.card_dataframe()
        dcards = self.dealer.card_dataframe()
        used_cards = pcards.append(dcards)
        deck_cards = self.deck_dataframe()
        available_cards = deck_cards
        available_cards['Available'] = deck_cards['Total'] 

        for used_index, used_row in used_cards.iterrows():
            for available_index, available_row in available_cards.iterrows():
                if (str(used_row['Cards']) == str(available_row['Cards'])):
                    available_value = available_row['Available'] - 1
                    available_cards.at[available_index, 'Available'] = available_value

        return available_cards


# classe centralizadora das informacoes
class Blackjack():
    def __init__(self, pcard1=0, pcard2=0, pcard3=0, pcard4=0, pcard5=0, dcard1=0, dcard2=0, dcard3=0, dcard4=0, dcard5=0, qdecks=1):
        
        # preparacao do ambiente
        self.player = Player(pcard1, pcard2, pcard3, pcard4, pcard5)
        self.dealer = Player(dcard1, dcard2, dcard3, dcard4, dcard5)
        self.deck = Deck(self.player, self.dealer, qdecks) 

        #print("Deck: \n"+self.deck.dataframe+"\n")
        #print("Jogador: \n"+self.player.dataframe.to_string()+"\n")
        #print("Dealer: \n"+self.dealer.dataframe.to_string()+"\n")

        if(self.player.busted == False and self.dealer.busted == False): # se o jogador nao tiver estourado a pontuacao
            # sugestoes dos agentes
            self.get_suggestions
                        
            # resultados dos agentes
            #agente_resultado = AgenteResultado()
            #print("Agente Resultado: ")

    def get_suggestions(self):
        print("*** Sugestões dos Agentes Analíticos ***")

        self.agente_aleatorio = AgenteAleatorio()
        print("Agente Aleatório: "+self.agente_aleatorio.suggestion)

        self.agente_tradicional = AgenteTradicional(self.player, self.dealer)
        print("Agente Tradicional: "+self.agente_tradicional.suggestion)

        self.agente_historico = AgenteHistorico(self.player, self.dealer)
        print("Agente Histórico: "+self.agente_historico.suggestion)
        
        self.agente_probabilistico = AgenteProbabilistico(self.player, self.dealer, self.deck)
        print("Agente Probabilístico: "+self.agente_probabilistico.suggestion)

    def get_result(self, resultado_partida, sugestao_escolhida):
        result = AgenteResultado(self.agente_aleatorio, self.agente_historico, self.agente_probabilistico, self.agente_tradicional, resultado_partida, sugestao_escolhida)

    def get_info(self):
        print("*** Informações do Ambiente ***")
        print('pcard1: '+str(self.player.card1))
        print('pcard2: '+str(self.player.card2))
        print('pcard3: '+str(self.player.card3))
        print('pcard4: '+str(self.player.card4))
        print('pcard5: '+str(self.player.card5))
        print('pcardsum: '+str(self.player.cardsum))
        print('dcard1: '+str(self.dealer.card1))
        print('dcard2: '+str(self.dealer.card2))
        print('dcard3: '+str(self.dealer.card3))
        print('dcard4: '+str(self.dealer.card4))
        print('dcard5: '+str(self.dealer.card5))
        print('dcardsum: '+str(self.dealer.cardsum))
        print('qdecks: '+str(self.deck.qdecks))