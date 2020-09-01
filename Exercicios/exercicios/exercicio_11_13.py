"""

Exercicio 11: Elaborar um programa para calcular media aritimetica e ponderada

"""

def media(notas):
    if notas[0].lower() == 'a':
        return (notas[1] + notas[2] + notas[3]) / 3
    else:
        return (notas[1]*5 + notas[2]*3 + notas[3]*2) / 10

notas = ['p', 8, 6, 1]

print(media(notas))

"""

Exercicio 12: Calcular os valores de um numero

"""

def soma_numero(num):
    soma = 0
    if num <= '0':
        return 'Numero Inválido'
    for n in num:
        soma += int(n)
    return f'A soma dos valores é: {soma}'

num = 333

print(soma_numero(str(num)))

"""

Exercicio 13: Fazer uma operação entre dois numeros

"""

def calcular(calc):
    if calc[0] == '+':
        return f'A soma é: {calc[1] + calc[2]}'
    if calc[0] == '-':
        return f'A soma é: {calc[1] - calc[2]}'
    if calc[0] == '*':
        return f'A soma é: {calc[1] * calc[2]}'
    else:
        return f'A soma é: {calc[1] / calc[2]}'


calc = ['/', 10, 20]

print(calcular(calc))