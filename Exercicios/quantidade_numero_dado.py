from random import randrange

qtdade = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


def jogar_dado():
    return quantidade_vezes(randrange(1, 7))


def quantidade_vezes(num):
    soma = int(qtdade.get(num)) + 1
    qtdade[num] = soma


for x in range(0, 100):
    jogar_dado()

print(qtdade)
