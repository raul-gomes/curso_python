texto = []

def cria_arquivo(nome, texto):
    try:
        with open(f'{nome}.txt', 'w') as arq:
            arq.write(''.join(texto))
            return 'Arquivo criado com sucesso'
    except:
        return 'Não foi possivel criar o arquivo'

def converte_maiscula(texto):
    copia = []
    for caracter in texto:
        copia += caracter.upper()
    return ''.join(copia)

with open('texto_usuario.txt') as arq:
    texto = arq.read()

nome = input('Informe o nome do arquivo: ')



print(cria_arquivo(nome, converte_maiscula(texto)))


