import math

"""

Exercicio 1: Crie uma função e retorne o dobro dela.

"""

def dobro(num):
    return num * num

num = 3

print(dobro(num))

"""

Exercicio 2: Receba a data (01/01/2000) e retorne no formato (01 de Janeiro de 2000) 

"""

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
       'Dezembro')

dia = 1
mes = 12
ano = 2000

print(f'{dia} de {meses[mes-1]} de {ano}')

"""

Exercicio 3: Definir se um é positivo ou negativo

"""

def positivo_negativo(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

num = 20

if positivo_negativo(num):
    if positivo_negativo(num) == -1:
        print('Numero Negativo')
    else:
        print('Numero positivo')
else:
    print('Numero 0')

"""

Exercicio 4: Definir se o quadrado do numero e perfeito

"""

def quadrado_perfeito(num):

    if (math.sqrt(num) - int(math.sqrt(num))):
        return False
    else:
        return True


num = 17

if quadrado_perfeito(num):
    print(f'O numero {num} é um quadrado perfeito de {int(math.sqrt(num))}')
else:
    print(f'O numero {num} não é um quadrado perfeito')


"""

Exercicio 5: Calcular a area de uma esfera

"""

area = lambda r: 4/3 * math.pi * r**3

print(area(3))


"""

Exercicio 6: Conversão de horas em segundos

"""

conversao = lambda hora: horas[0] * 3600 + hora[1] * 60 + hora[2]

horas = [10, 20, 30]

print(conversao(horas))

"""

Exercicio 7: Conversção de ºC para ºF

"""

temperaturas = [10, 25, 30, 40]


print(list(map(lambda temp: temp * (9/5) + 32, temperaturas)))


"""

Exercicio 8: Calcular o valor da hipotenusa

"""

hipotenusa = lambda cateto_a, cateto_b: math.sqrt(cateto_a**2 + cateto_b**2)

print(f'A hipotenusa dos catetos 2 e 3 é: {round(hipotenusa(2, 3), 2)}')

"""

Exercicio 9: Calcular o volume do cilindro

"""

volume_cilindro = lambda h, r: math.pi * r**2 * h

print(f'Um cilindro com h 1 e raio 1 tem volume de {round(volume_cilindro(1, 1), 2)}')

"""

Exercicio 10: Qual numero e maior

"""

num1 = 30
num2 = 10

print(f'O maior numero é: {max(num1, num2)}')
