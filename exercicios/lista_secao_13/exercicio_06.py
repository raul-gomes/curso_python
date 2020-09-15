import re
from collections import Counter

with open('texto_usuario.txt') as arq:
    texto = arq.read()
    dict = Counter(re.sub('[^abcdefghijklmnopqrstuvxwyz]', '', texto.lower()))
    print(dict)
