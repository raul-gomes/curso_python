copia = []
with open('texto_usuario.txt') as arq:
    texto = arq.read()

    for char in texto:
        if char.lower() in 'aeiouéêãáó':
            char = '*'
        copia += char

    copia = str(''.join(copia))

with open('texto_usuario_copia.txt', 'w') as arq:
    arq.write(copia)

with open('texto_usuario_copia.txt') as arq:
    print(arq.read())
