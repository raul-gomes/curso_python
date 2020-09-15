"""

Dica de quando tratar codigo:

TODA ENTRADA DEVE SER TRATADA

"""

# else - é somente executado se não ocorrer o erro
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# finally - é sempre executado.
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
finally:
    print(f'Você digitou {num}')

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# É necessário tratar os erros direto na função


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'


a = input('Inform o primeiro numero: ')
b = input('Informe o segundo numero: ')

print(dividir(a, b))


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor Incorreto: {err}'


a = input('Informe o primeiro numero: ')
b = input('Informe o segundo numero: ')

print(dividir(a, b))
