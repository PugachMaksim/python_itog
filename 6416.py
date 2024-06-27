"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование."""


from collections import namedtuple
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

File = namedtuple('File', ['name', 'extension', 'is_dir', 'parent_dir'])


def get_file_info(path):
    """Функция получает на вход путь до директории и возвращает список объектов namedtuple"""
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(File(file.split('.')[0], file.split('.')[1], False, os.path.basename(root)))
        for dir in dirs:
            file_list.append(File(dir, None, True, os.path.basename(root)))
    return file_list


if __name__ == '__main__':
    path = input('Введите путь до директории: ')
    file_list = get_file_info(path)
    with open('file_info.txt', 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(f'{file.name} {file.extension} {file.is_dir} {file.parent_dir}\n')
    logger.info('Файл с информацией о файле создан')