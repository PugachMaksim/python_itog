import argparse
import logging
import os
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename="dir.log", filemode="w", style='{', encoding="utf-8", level=logging.INFO,
                    format='функция {funcName}: {msg}'
                    )
logger = logging.getLogger(__name__)

#проверка пути
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


# парсер, передача через терминал
parser = argparse.ArgumentParser(description='MyApp')
parser.add_argument('-path', type=dir_path, help="Введите путь...")
args = parser.parse_args()
print(args)

MyDir = namedtuple('MyDir', ['name', 'expansion', 'catalog_flag', 'parent_directory'])

directory = r'D:\users\pmv\Desktop\башня\акты\передача фронта работ\СМАРТ'
listDir = []


def diiir(directory):
    for path, dirs, files in os.walk(os.path.normpath(directory)):
        for filename in files:
            name, expansion = os.path.splitext(filename)
            expansion = expansion.replace('.', '')
            catalog_flag = None
            parent_directory = os.path.dirname(path)
            file = MyDir(name, expansion, catalog_flag, parent_directory)
            logger.info(f'{name=},{expansion=},{parent_directory=}')
            listDir.append(file)
        for folder_name in dirs:
            name = folder_name
            catalog_flag = "True"
            parent_directory = os.path.dirname(path)
            folder = MyDir(name, " ", catalog_flag, parent_directory)
            logger.info(f'{name=},{expansion=},{parent_directory=}')
            listDir.append(folder)
    # print(*listDir, sep='\n')


# print(diiir(directory))
# diiir(directory)
print(diiir(args.path))
