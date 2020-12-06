import os, csv, json, pandas as pd
from pathlib import Path

"""
Classe com as funcoes para maipulacao de arquivos
"""

class File:

    def __init__(self, filename="resultado.csv", filepath="", encoding="utf-8"):
        self.projectpath = Path().absolute()
        self.filepath = self.projectpath/'blackjack/data'
        self.filename = self.filepath/filename
        self.encoding = encoding
        
    def fileInfo(self):
        #Returns the path of the directory, where your script file is placed
        print('Absolute path : {}'.format(self.projectpath))

        #if you want to go to any other file inside the subdirectories of the directory path got from above method
        filePath = self.filename
        print('File path : {}'.format(filePath))

        #To check if file present in that directory or Not
        isfileExist = filePath.exists()
        print('isfileExist : {}'.format(isfileExist))

        #To check if the path is a directory or a File
        isadirectory = filePath.is_dir()
        print('isadirectory : {}'.format(isadirectory))

        #To get the extension of the file
        print('File extension : {}'.format(filePath.suffix))

    # Verifica se o arquivo informado existe
    def checkFile(self):
        try:
            with open(self.filename, encoding=self.encoding) as file:
                file.close()
                return True
        except Exception as e:
            print (e)
            return False

    # Retorna os dados de um arquivo CSV como Dataframe
    def getCSVasDataframe(self, delimiter=","):
        if self.checkFile():

            df = pd.read_csv(self.filename)
            return df

    # Retorna os dados de um arquivo CSV como JSON
    def getCSVasJSON(self, delimiter=","):
        if self.checkFile():

            csv_data = []
            with open(self.filename, encoding=self.encoding) as csv_file:
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

             with open(self.filename, encoding=self.encoding) as json_file:
                json_data = json.load(json_file)
                json_file.close()

                return json_data

    # Salva os dados de um JSON para CSV
    def setJSONasCSV(self, json_data, delimiter=","):
        if self.checkFile():

            df = pd.read_json(json_data)
            df.to_csv(self.filename, index=False, line_terminator="\n", sep=delimiter)

    # Salva os dados de um JSON em um arquivo JSON
    def setJSONasFile(self, json_data):
        if self.checkFile():

            with open(self.filename, "w+", encoding=self.encoding) as json_file:
                json.dump(json_data, json_file)
                json_file.close()

    # Salva os dados de um Dataframe como arquivo CSV
    def setDataframeasCSV(self, data, delimiter=","):
        if self.checkFile():

            df = data
            df.to_csv(self.filename, index=False, line_terminator="\n", sep=delimiter)