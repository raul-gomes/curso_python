lista_cidade = []
maior = 0


def abre_arquivo():
    with open('cidades.txt') as arq:
        texto = arq.readlines()
        return texto


def cria_arquivo(texto):
    with open('maior_populacao.txt', 'w') as arq:
        arq.write(f'A Cidade com maior populção é {texto[0]} com População de {texto[1]}')


cidades = abre_arquivo()

for cidade in cidades:
    teste = cidade.split(':')
    dict = [teste[0], int(teste[1])]
    lista_cidade.append(dict)

for cidade in lista_cidade:
    if int(cidade[1]) > maior:
        maior_cidade = cidade
        maior = cidade[1]

cria_arquivo(maior_cidade)
