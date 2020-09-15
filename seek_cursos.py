"""

Seek e Cursos

seek() - Serve para movimentar o cursor pelo arquivo

"""

arq = open('texto.txt')

print(arq.read())

arq.seek(0)

print(arq.read())

arq.seek(0)

#readline() - função que ler linha a linha

print(arq.readline())

arq.seek(0)

ret = arq.read()

ret.split(' ')

print(ret.split(' '))

#readlines() - Separa o texto em uma lista, onde cada elemento e uma linha do arquivo

arq.seek(0)

print(arq.readlines())

arq.close()