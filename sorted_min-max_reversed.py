"""

Sorted - Usado em qualquer iteravel

"""

print("Função Sorted")

lista = [4, 9, 6, 1, 8, 3]
tupla = (4, 9, 6, 1, 8, 3)

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob1234", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print('----')
print(sorted(lista))
print(sorted(lista, reverse=True))
print(lista)
print('----')
print(sorted(tupla))
print(tupla)
print('----')

for usaruio in usuarios:
    print(usaruio)

print('----')

organizados = sorted(usuarios, key=lambda usuario: usuario["username"].lower())

for organizado in organizados:
    print(organizado)

print('----')

organizados = sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))

for organizado in organizados:
        print(organizado)

"""

Min e Max

"""

print("\n\nFunção Min e Max")

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(max(lista))

print(max(3, 6, 9, 7))

print(max(dicionario))

print(max(dicionario.values()))

print(min(lista))

print(min(3, 6, 9, 7))

print(min(dicionario))

print(min(dicionario.values()))

print(max(usuarios, key=lambda usuario: len(usuario["username"]))['tweets'])

print(min(usuarios, key=lambda usuario: len(usuario["username"])))


"""

Reversed - uso semelhante ao sorted, so que usado para inverter os iteraveis

"""

print("\n\nFunção Reversed")


print(list(reversed(lista)))

print(list(reversed(tupla)))

for letra in reversed('abcde'):
    print(letra, end=' ')

print('\n')

print((' '.join(list(reversed('abcde')))))
