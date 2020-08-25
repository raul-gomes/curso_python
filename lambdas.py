dobro = lambda x, y: x * y

print(dobro(5, 10))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('raul', 'gomes'))

amar = lambda: 'Como não amar Python'

print(amar())


def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

funcao = geradora_funcao_quadratica(2, 3, 4)

print(funcao(1))

print(geradora_funcao_quadratica(3, 0, 1)(2))
