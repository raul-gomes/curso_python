"""

filter() - Retorna sempre True ou False

"""

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

res = filter(lambda x: x > statistics.mean(dados), dados)

print(res)

print(list(res))

print(list(res))


usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

usuarios_inativos = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)

usuarios_inativos_com_not = filter(lambda usuario: not usuario['tweets'], usuarios)

print(list(usuarios_inativos))

print(list(usuarios_inativos_com_not))

nomes = ['Vanessa', 'Ana', 'Maria']

# Juntando MAP e FILTER

print(list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) >= 5, nomes))))
