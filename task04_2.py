import os
import logging


def files_in_dir():
    files = os.listdir(path='.')
    print(files)
    amount = len(files)
    dir = os.getcwd()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)
    logger.debug(f'Количество файлов в каталоге {dir} равно {amount}')
