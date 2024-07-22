from os import chdir, listdir, getcwd
from pathlib import Path

path = Path('/','var','log', 'astc_installer')

chdir(path)
print(listdir())
print(getcwd())
