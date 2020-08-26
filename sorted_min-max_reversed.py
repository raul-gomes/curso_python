"""
Sorted - Usado em qualquer iteravel
"""

lista = [4, 9, 6, 1, 8, 3]
tupla = (4, 9, 6, 1, 8, 3)

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
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
