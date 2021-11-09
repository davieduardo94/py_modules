# codigos para importacao do arquivo no banco
import csv
import os
import pyodbc
from Data.utils import (csvDest, csvEdit, csvPath, database, password, server,username)
from tqdm import tqdm
import time

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
crsr = cnxn.cursor()

# funcao para executar os processos SQL
def odbcExec(sql):
    crsr.execute(sql)
    cnxn.commit()

# fechar a conexao
def closeODBC():
    crsr.close()
    cnxn.close()

# conexao com o servidor
def conectSQL():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    crsr = cnxn.cursor()


def importarArquivo():
    fileList = os.listdir(csvDest)
    formatFiles(fileList)
    print('Importando dados para o banco de dados GCL')
    for flie in tqdm(fileList, total=len(fileList)):
        # print(flie)
        truncateTable(flie)
        loadFile(csvEdit, flie)
        time.sleep(0.5)
    closeODBC()


def truncateTable(arquivo):
    sql = "IF OBJECT_ID('"+arquivo[:len(arquivo)-4]+"')  IS NOT NULL TRUNCATE TABLE ["+database+"].."+arquivo[:len(arquivo)-4]
    # print(sql,'\n')
    conectSQL()
    odbcExec(sql)

def loadFile(caminho, arquivo):
    sql = "BULK INSERT ["+database+"].."+arquivo[:len(arquivo)-4]+" FROM '"+caminho+arquivo+"' WITH(FIRSTROW = 2, FIELDTERMINATOR = '	' ,MAXERRORS = 10000, ROWTERMINATOR = '\n', BATCHSIZE = 500000,CODEPAGE = 65001,DATAFILETYPE = 'char') "
    # print(sql, '\n')
    conectSQL()
    odbcExec(sql)
    
def formatFiles(filelist):
    print('Ajustando arquivos CSV')
    for file in tqdm(filelist, total=len(filelist)):
        # print('Carregando: '+file)
		# abrindo o csv da pasta raiz
        with open(csvDest+file, 'r', newline='', encoding="utf-8") as csv_file:
            # realizando ajustes do arquivo
            csv_file =  ''.join([line for line in csv_file]).replace("	","").replace(",","	").replace("	 "," ").replace('"','')
            # gerando novo arquivo csv formatado
            newCSV = open(csvEdit+file[:len(file)-4]+'.csv', 'w', encoding="utf-8", newline='')
            # escrevendo dados extraidos do csv_file (raiz)
            newCSV.writelines(csv_file)
            # fechando o arquivo
            newCSV.close()
            time.sleep(0.5)
