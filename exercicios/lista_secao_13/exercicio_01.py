with open('arq.txt', 'w') as arq:
    while True:
        caracter = input('Digite o que se deseja e 0 para sair: ',)
        if caracter == '0':
            break
        arq.write(caracter + '\n')

with open('arq.txt') as arq:
    print(arq.read())

