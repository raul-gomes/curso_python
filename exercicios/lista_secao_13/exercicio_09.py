def abre_arquivo(nome):
    try:
        with open(f'{nome}.txt') as arq:
            texto = arq.read()
            return texto
    except:
        return 'Problema ao abrir o arquivo'

def criar_arquivo(nome, texto):
    with open(f'{nome}.txt', 'w') as arq:
        arq.write(texto)
        return 'Arquivo criado com sucesso'

def concatenar_arquivo(texto_1, texto_2):
    return texto_1 + "\n" + texto_2


texto_1 = abre_arquivo('texto_01')
texto_2 = abre_arquivo('texto_02')

print(criar_arquivo('texto_concatenado', concatenar_arquivo(texto_1, texto_2)))



