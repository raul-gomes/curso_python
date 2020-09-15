"""

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional o software precisa de permissão:
    - Permissão de leitura -> leitura
    - Permissão de escrita -> escrita

StringIO - Utilizado para ler e criar arquivos em memória

"""

from io import StringIO

mensagem = 'esta é apenas uma string normal'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.close()