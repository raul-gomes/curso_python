"""

Reduce ()

"""

from functools import reduce


def soma(x, y):
    return x + y


numeros = [1, 2, 3, 4, 5, 6]


res = reduce(soma, numeros)

res_labmda = reduce(lambda x, y: x + y, numeros)

print(res)

print(res_labmda)

"""

Any e all

"""

dados = [0, 1, 2, 3, 4, 5]

print(all(dados)) # Retorna True se todos os elementos forem verdadeiros ou se o iteravel estiver vazio.

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all(nome[0] == 'C' for nome in nomes))

print(any(dados)) # Retorna True se pelo menos um elemento for verdadeiro se o iteravel estiver vazio retorna false

print(any([]))
