import os, csv, json, pandas as pd

"""
Classe com as funções para manipulação de arquivos

Exemplos de uso:

# salvando informações no json
arquivo_json = Arquivo("ci_info.json")
arquivo_json.setJSONasFile(data_json)

# resgatando informações do json
data_json = arquivo_json.getJSONasFile()
print(data_json)

# salvando resultado em um arquivo
arquivo = Arquivo(nome="resultado.csv")
arquivo.setJSONasCSV(data_json)
"""

class Arquivo:

    def __init__(self, nome="resultado.csv", caminho="./data/", encoding="utf-8"):
        self.nome = nome
        self.caminho = caminho
        self.encoding = encoding

    # Verifica se o arquivo informado existe
    def checkFile(self):
        try:
            with open(self.caminho+self.nome, encoding=self.encoding) as file:
                file.close()
                return True
        except Exception as e:
            print (e)
            return False

     # Retorna os dados de um arquivo CSV como JSON
    def getCSVasJSON(self, delimiter=","):
        if self.checkFile():

            csv_data = []
            with open(self.caminho+self.nome, encoding=self.encoding) as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
                for row in csv_reader:
                    csv_data.append(row)
                csv_file.close()

                json_data = json.dumps(csv_data)
                #print(json_data)
                return json_data

 
    # Retorna os dados de um arquivo JSON
    def getJSONasFile(self):
        if self.checkFile():

             with open(self.caminho+self.nome, encoding=self.encoding) as json_file:
                json_data = json.load(json_file)
                json_file.close()

                return json_data

    # Salva os dados de um JSON para CSV
    def setJSONasCSV(self, json_data, delimiter=","):
        if self.checkFile():

            df = pd.read_json(json_data)
            df.to_csv(self.caminho+self.nome, index=False, line_terminator="\n", sep=delimiter)

     # Salva os dados de um JSON em um arquivo JSON
    def setJSONasFile(self, json_data):
        if self.checkFile():

            with open(self.caminho+self.nome, "w+", encoding=self.encoding) as json_file:
                json.dump(json_data, json_file)
                json_file.close()