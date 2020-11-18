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
        self.sum = self.cards_sum()
    
    def card_dataframe(self):
        cardrank = [self.cardrank1, self.cardrank2, self.cardrank3, self.cardrank4, self.cardrank5]
        cardvalue = [self.card1, self.card2, self.card3, self.card4, self.card5]
        data = {'Cards':cardrank,
                'Values':cardvalue}
        df = pd.DataFrame(data)
        return df

    def card_value(self, card):
        if card == 'A':
            return 11
        elif card == 'T' or card == 'J' or card == 'Q' or card == 'K':
            return 10
        else:
            return card

    def cards_sum(self):
        cardssum = self.card1 + self.card2 + self.card3 + self.card4 + self.card5
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
        self.ranks_total = 0
        self.ranks_available = []
        self.dataframe = {}

        # inicializando os valores
        self.cards_total = self.get_total_cards()
        self.ranks_total = self.get_total_ranks()
        self.dataframe = self.deck_dataframe()
        self.ranks_available = self.get_available_ranks()
        self.dataframe = self.ranks_available
        
    def get_total_cards(self):
        return len(self.suits) * len(self.ranks) * self.qdecks

    def get_total_ranks(self):
        qtd_suits = len(self.suits) * self.qdecks
        qtd_ranks = [i * qtd_suits for i in self.ranks]
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
        player = Player(pcard1, pcard2, pcard3, pcard4, pcard5)
        dealer = Player(dcard1, dcard2, dcard3, dcard4, dcard5)
        deck = Deck(player, dealer, qdecks) 

        #print("Deck: \n"+deck.dataframe+"\n")
        #print("Jogador: \n"+player.dataframe.to_string()+"\n")
        #print("Dealer: \n"+dealer.dataframe.to_string()+"\n")

        # sugestoes dos agentes
        #agente_aleatorio = AgenteAleatorio()
        #print("Agente Aleatório: "+agente_aleatorio.agent_suggestion())

        agente_tradicional = AgenteTradicional(player, dealer)
        #print("Agente Tradicional: "+agente_tradicional.agent_suggestion())

        #agente_historico = AgenteHistorico()
        #print("Agente Histórico: "+agente_historico.agent_suggestion())

        #agente_probabilistico = AgenteProbabilistico()
        #print("Agente Probabilístico: "+agente_probabilistico.agent_suggestion())

        # resultados dos agentes
        #agente_resultado = AgenteResultado()
        #print("Agente Resultado: ")

    #def calcular_probabilidade():
    #    