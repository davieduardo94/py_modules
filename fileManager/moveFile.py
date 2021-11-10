from tqdm import tqdm
import time

"""
csvPath - pasta de origem do arquivo
csvDest - destino do arquivo
verificar a extensão do arquivo
"""

def moveFile():
    print('Movendo arquivo para pasta selecionada')
    files = glob.glob(os.path.join(csvPath, '*.csv'))
    for fileInFolder in tqdm(files, total=len(files)):
        shutil.move(fileInFolder, csvDest)
        time.sleep(0.5)
    files = ""
