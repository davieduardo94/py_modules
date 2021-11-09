from tqdm import tqdm
import time
"""
csvDest - the csv location
newCSV - the new CSV created from csvDest
csvFile - the csv selected and opened to had a modifies
"""

def formatFiles(filelist):
    print('Ajustando arquivos CSV')
    for file in tqdm(filelist, total=len(filelist)):
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
