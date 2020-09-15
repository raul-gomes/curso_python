with open('texto_usuario.txt') as arq:
    caracter = input('Digite um caracter: ')
    texto = arq.read()
    if caracter in texto:
        print(f'O caracter {caracter} está no texto')
    else:
        print(f'O caracter {caracter} não está no texto')