# Для запуска можно использовать python task04_1.py notepad

from sys import argv
import subprocess

script, file = argv

try:
    subprocess.run(file)
except FileNotFoundError:
    print(f'Файл {file} не существует')
except:
    print(f'Не удаётся запустить {file}')
