from agent.aleatorio import AgenteAleatorio
from agent.historico import AgenteHistorico
from agent.probabilistico import AgenteProbabilistico
from agent.tradicional import AgenteTradicional
from data.file import File

"""
Classe com as funcoes para avaliacao do resultado dos agentes analiticos
"""

class AgenteResultado():

    def __init__(self, agente_aleatorio, agente_historico, agente_probabilistico, agente_tradicional, resultado_partida, sugestao_escolhida):
        self.name = "Resultado"
        self.nickname = "resu"
        self.filename = "resultado.csv"
        self.dataframe = {}

        self.resultado_partida = resultado_partida
        self.sugestao_escolhida = sugestao_escolhida

        self.rwinprobability = '?' 
        self.rwinresult = resultado_partida
        self.ahistsuggestion = agente_historico.suggestion
        self.ahistchosen = '?'
        self.ahistwinloss = '?'
        self.aprobsuggestion = agente_probabilistico.suggestion
        self.aprobchosen = '?'
        self.aprobwinloss = '?'
        self.atradsuggestion = agente_tradicional.suggestion
        self.atradchosen = '?'
        self.atradwinloss = '?'
        self.aaleasuggestion = agente_aleatorio.suggestion
        self.aaleachosen = '?'
        self.aaleawinloss = '?'

        self.get_info()

    def get_info(self):
        print("*** Informações do Resultado ***")
        print('sugestao_escolhida: '+str(self.resultado_partida))
        print('resultado_partida: '+str(self.sugestao_escolhida))
        print('ahistsuggestion: '+str(self.ahistsuggestion))
        print('ahistchosen: '+str(self.ahistchosen))
        print('ahistwinloss: '+str(self.ahistwinloss))
        print('aprobsuggestion: '+str(self.aprobsuggestion))
        print('aprobchosen: '+str(self.aprobchosen))
        print('aprobwinloss: '+str(self.aprobwinloss))
        print('atradsuggestion: '+str(self.atradsuggestion))
        print('atradchosen: '+str(self.atradchosen))
        print('atradwinloss: '+str(self.atradwinloss))
        print('aaleasuggestion: '+str(self.aaleasuggestion))
        print('aaleachosen: '+str(self.aaleachosen))
        print('aaleawinloss: '+str(self.aaleawinloss))

    def get_data(self):
        file = File(self.filename)
        return file.getCSVasDataframe()

    def set_data(self):
        file = File(self.filename)
        return file.setDataframeasCSV(data = self.dataframe)