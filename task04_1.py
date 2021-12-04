# Для запуска можно использовать python task04_1.py notepad

from sys import argv
import subprocess

script, file = argv

try:
    subprocess.run(file)
except FileNotFoundError:
    print(f'File {file} does not exist')
except Exception as e:
    print(f'Error is {e}')
