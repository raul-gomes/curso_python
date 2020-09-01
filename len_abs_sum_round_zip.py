"""

len() e sum() - LEN serve para mostrar o taminho de um iteravel e SUM serve para somar os iteraveis

"""
print('----- SUM -----')
print(sum([1, 2, 3, 4, 5], 56))

"""

abs() - Retorna um valor absoluto de um numero inteiro ou real.

"""

print('\n\n----- ABS() -----')

print(abs(-5))

print(abs(5))

print(abs(3.47))

print(abs(-3.47))

"""

round() - retorna um valor arredondado

"""

print('\n\n----- ROUND() -----')

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.2199999, 2))

"""

zip() - cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis passados com entradas em pares

"""

print('\n\n----- ZIP() -----')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8]

zip1 = zip(lista1, lista2)

print(type(zip1))

print(list(zip1))

zip1 = zip(lista1, reversed(lista2))

print(dict(zip1))

zip1 = zip(lista2, reversed(lista1))

print(dict(zip1))

lista3 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*lista3)))

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)
