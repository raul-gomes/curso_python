listas = [0, 1, 2, 3, 4, 5, 6]

numeros = [0, 1, 2, 3, 4, 5, 6]

nome = 'Geek University'


def funcao(valor):
    return valor * valor


print([lista for lista in listas if not lista % 2 == 0])

print([lista for lista in listas if lista % 2 == 0])

print([funcao(lista) for lista in listas])

print([numero * 2 for numero in listas])

print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

print([lista * 3 for lista in range(0, 11)])

print([numero for numero in numeros if not numero % 2])

print([numero for numero in numeros if numero % 2])

print([numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros])

dicionario = {}

for numero in numeros:
    if numero % 2:
        dicionario[numero] = 'impar'
    else:
        dicionario[numero] = 'par'

print(dicionario)

l1 = [1,2,3,4,5,6,7,8,9]

print([(v1, v2) for v1 in l1 for v2 in range(3)])
