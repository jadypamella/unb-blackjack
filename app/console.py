import os
from blackjack import Blackjack

# classe do console principal
class Console():

    def __init__(self, pcard1=0, pcard2=0, pcard3=0, pcard4=0, pcard5=0, dcard1=0, dcard2=0, dcard3=0, dcard4=0, dcard5=0, qdecks=1):
        self.pcard1 = pcard1
        self.pcard2 = pcard2
        self.pcard3 = pcard3
        self.pcard4 = pcard4
        self.pcard5 = pcard5
        self.dcard1 = dcard1
        self.dcard2 = dcard2
        self.dcard3 = dcard3
        self.dcard4 = dcard4
        self.dcard5 = dcard5
        self.qdecks = qdecks

        self.main()
        
        self.blackjack = Blackjack(self.pcard1, self.pcard2, self.pcard3, self.pcard4, self.pcard5, self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5, self.qdecks)

        self.inicio_partida()

    def clear(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)

    def header(self):
        print("****************************")
        print("*** Análise de Blackjack ***")
        print("****************************")

    def main(self):    
        self.clear()
        self.header()

    def inicio_partida(self):
        self.pcard1 = input('Digite a sua primeira carta: ')
        self.pcard2 = input('Digite a sua segunda carta: ')
        self.dcard1 = input('Digite a carta revelada do Dealer: ')
        self.qdecks = input('Digite a quantidade de baralhos: ')
        self.blackjack = Blackjack(self.pcard1, self.pcard2, self.pcard3, self.pcard4, self.pcard5, self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5, self.qdecks)

        self.main()
        self.escolher_sugestao()

    def proxima_acao(self):
        self.main()
        self.blackjack.get_info()
        self.blackjack.get_suggestions()
        
        print('Escolha a próxima ação:')
        print('1 - Escolher sugestão')
        print('2 - Informar resultado')
        print('3 - Sair')
        self.acao_escolhida = input('Escolha a próxima ação: ')

        if (self.acao_escolhida == '1'):
            self.escolher_sugestao()
        elif (self.acao_escolhida == '2'):
            self.informar_resultado()
        else:
            pass

    def escolher_sugestao(self):
        self.main()
        self.blackjack.get_info()
        self.blackjack.get_suggestions()

        print("****************************")
        print('Informe a sugestão escolhida:')
        print('1 - Hit')
        print('2 - Stand')
        self.sugestao_escolhida = input('Sugestão escolhida: ')

        if (self.blackjack.player.busted == False and self.blackjack.dealer.busted == False):
            if (self.sugestao_escolhida == 'hit' or self.sugestao_escolhida == 'Hit' or self.sugestao_escolhida == '1'):
                self.informar_nova_carta_jogador()
                #self.proxima_acao()

            elif (self.sugestao_escolhida == 'stand' or self.sugestao_escolhida == 'Stand' or self.sugestao_escolhida == '2'):
                self.informar_resultado()
            else:
                pass



    def informar_resultado(self):
        self.main()

        print('Informe o resultado da rodada ou partida:')
        print('1 - Win')
        print('2 - Loss')
        print('3 - Draw')
        self.resultado_partida = input('Resultado da partida: ')

        if (self.resultado_partida == 'win' or self.resultado_partida == 'Win' or self.resultado_partida == '1'):
            self.blackjack.get_result(self.resultado_partida, self.sugestao_escolhida)
        elif (self.resultado_partida == 'loss' or self.resultado_partida == 'Loss' or self.resultado_partida == '2'):
            self.blackjack.get_result(self.resultado_partida, self.sugestao_escolhida)
        elif (self.resultado_partida == 'draw' or self.resultado_partida == 'Draw' or self.resultado_partida == '3'):
            self.blackjack.get_result(self.resultado_partida, self.sugestao_escolhida)
        else:
            pass

    def informar_cartas_dealer(self):
        pass

    def informar_nova_carta_jogador(self):

        # definindo a proxima carta a ser recebida
        if(self.pcard3 != 0):
            self.next_pcard = 3
            self.next_pcard_ordinal = "terceira"
            self.pcard3 = input('Digite a sua '+self.next_pcard_ordinal+' carta: ')
            self.blackjack.player.card3 = self.pcard3
        elif(self.pcard4 != 0):
            self.next_pcard = 4
            self.next_pcard_ordinal = "quarta"
            self.pcard4 = input('Digite a sua '+self.next_pcard_ordinal+' carta: ')
            self.blackjack.player.card4 = self.pcard4
        elif(self.pcard5 != 0):
            self.next_pcard = 5
            self.next_pcard_ordinal = "quinta"
            self.pcard5 = input('Digite a sua '+self.next_pcard_ordinal+' carta: ')
            self.blackjack.player.card5 = self.pcard5

    def informar_nova_carta_dealer(self):
        pass