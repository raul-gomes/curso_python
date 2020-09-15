"""

Usar a função open(). Retorna um _io.TextIOWrapper

Por padrão abre o arquivo para leitura

Caso não exista o arquivo gera o erro FileNotFoundError

r - leitura
w - write

read() - ler o arquivo

close() - fechar o arquivo

closed - Verifica se o arquivo está fechado ou não

Se tentar manipular o arquivo quando ele estiver fechado gera um erro ValueError

"""

# Leitura
arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))


ret = arquivo.read()

print(ret)

print(type(ret))

#print(arquivo.read())

arquivo.seek(0)

print(arquivo.closed)

arquivo.close()

print(arquivo.closed)

# Se abrirmos um arquivo para leitura não podemos escrever e vice-versa
# So recebe valores do tipo 'str'
# Escrita

with open('texto.txt', 'w') as arq:
    arq.write('Escrever dados em arquivo e bem tranquilo. \n')
    arq.write('Podemos escrever quantas linhas que quisermos. \n')
    arq.write('Ultima linha')

with open('texto.txt') as arq:
    print(arq.read())

with open('gekk.txt', 'w') as arq:
    arq.write('Geel' * 1000)

