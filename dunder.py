"""

Dunder Name e Dunder Main

Dunder Name - __name__

Dunder Main - __main__

Em Pyton, são utilizados dunder para criar funções, atributos, propriedades e etc. utilizando Double under para não gerar
conflito com os nomes desses elementos na programação.

"""

from Curso_Python.funcoes_com_parametro import soma_impares


if __name__ == '__main__':
    print(soma_impares([1, 2, 3, 4, 5, 6]))
