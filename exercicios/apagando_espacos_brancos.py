paises = ['', 'Argentina', '', 'Brasil', 'Chile', '   ', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

res_lambda = filter(lambda pais: len(pais.strip()) > 0, paises)

print(list(res_lambda))

print(list(res))