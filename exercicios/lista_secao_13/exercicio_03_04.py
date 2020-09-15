# Método 01
with open('texto_usuario.txt') as arq:
    vogais = 0
    consoantes = 0
    texto = arq.read()
    for caracter in texto:
        if caracter.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1
    print(f'O total de vogais: {vogais} e consoantes: {consoantes}')

# Método 02
import re
from collections import Counter

with open('texto_usuario.txt') as arq:
    texto = arq.read()
    print(Counter(re.sub('[aeiouAEIOU]', '', texto)))
