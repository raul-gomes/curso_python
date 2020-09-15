"""

É utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados após o bloco with

FORMA PYTHONICA

"""

with open('texto.txt') as arq:
    print(arq.readlines())

