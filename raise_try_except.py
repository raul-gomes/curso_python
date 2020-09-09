def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if cor not in cores:
        raise ValueError(f'A cor precisa ser: {cores}')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'verde')

# Método Genérico
try:
    geek()
except:
    print('Deu Erro')

# Método expecifico
try:
    len(5)
except TypeError:
    print('Deu Erro Especifico')

# Método expecifico com detalhes
try:
    len(5)
except TypeError as err:
    print(f'Deu Erro: {err}')

# Método expecifico com detalhes de mais de uma exceção
try:
    len(5)
except TypeError as err_a:
    print(f'Deu Erro: {err_a}')
except NameError as err_b:
    print(f'Deu Erro: {err_b}')



