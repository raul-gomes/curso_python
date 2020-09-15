"""

r - leitura (padrão)
w - escrita
x - abre para escrita somente se o arquivo não existir. Caso o arquivo existe, gera o erro FileExistsError
a - adiciona o conteudo no final do do arquivo, caso o arquivo não exista será criado.
+ - Leitura e escrita, juntamento com o com alguma das letras acima


"""

try:
    with open('texto.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo. \n')
except FileExistsError:
    print('Arquivo já existe')

with open('texto.txt', 'a') as arquivo:
    arquivo.write('\n Adicionando mais conteudo')

with open('texto.txt') as arquivo:
    print(arquivo.read())
