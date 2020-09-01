"""

Exercicio 14: Calcular se o carro é economico ou não (km/l)

"""

def calc_econimco(km, litros):
    media = km / litros
    if media <= 8:
        return 'Venda o Carro!'
    elif 8 < media <= 14:
        return 'Economico'
    else:
        return 'Super Economico'

km = 15
litros = 1

print(calc_econimco(km, litros))


"""

Exercicio 15: Definir os lados e tipos de um triangulo. 

"""

def lado_triangulo(lados):
    for lado in lados:
        verifica_lado = lados.copy()
        verifica_lado.remove(lado)
        if lado <= sum(verifica_lado):
            e_tringaulo = True
        else:
            return False
    return e_tringaulo


def tipo_triangulo(lados):
    cont = 0
    for x in lados:
        tipo = lados.copy()
        tipo.remove(x)
        for y in tipo:
            if x == y:
                cont += 1
    if cont == 0:
        return 'Triangulo Escaleno'
    elif cont == 2:
        return 'Triangulo Isósceles'
    else:
        return 'Triangulo Equilátero'


lados = []
num = 1

while True:
    if len(lados) == 3:
        break
    if num > 0:
        num = float(input('Informe a medida do triangulo: '))
        if num > 0:
            lados.append(num)
    else:
        print('informe um numero valido')
        num = 1

if lado_triangulo(lados):
    print(tipo_triangulo(lados))
else:
    print('Não é um triangulo')


"""

Exercicio 16: Irá desenhar uma linha na tela 

"""

def desenha_linha(qtdade_caracteres):
    return '=' * qtdade_caracteres

print(desenha_linha(60))

"""

Exercicio 17: Soma dos numero inteiros dentre um intervalo

"""

def soma_valores(intervalo):
    soma = 0
    for x in range(min(intervalo), max(intervalo)+1):
        soma += x
    return soma

intervalo = [20, 5]

print(soma_valores(intervalo))