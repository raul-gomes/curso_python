chaves = 'abcdefg'
nums = [0, 1, 2, 3, 4, 5, 6]

numeros = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6}


dicionario = {numero:'par' if numero % 2 == 0 else 'impar' for numero in nums}

print(dicionario)

print({numero:'impar' if not numero % 2 == 0 else 'par' for numero in nums})

quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}

print(numeros)
print(quadrado)

print({valor: valor**2 for valor in nums})

mistura = {chaves[i]: nums[i] for i in range(0, len(chaves))}

print(mistura)