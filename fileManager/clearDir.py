import os
import glob
import time
from tqdm import tqdm

"""
csvDest - pasta contendo arquivos
"""

def clearDir():
    print('Limpando diretorio destino')
    csvFolder = os.listdir(csvDest)
    csvFiles = glob.glob(csvDest+'*.csv')

    if(csvFolder == []):
        print('Pasta vazia')
    else:
        for removeCSV in tqdm(csvFiles, total=len(csvFiles)):
            os.remove(removeCSV)
            time.sleep(0.5)
