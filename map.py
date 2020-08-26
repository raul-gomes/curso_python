"""

map() - será retornado o valor da distributiva

"""

import math


def area(r):
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)

areas_lambda = map(lambda r: math.pi * (r ** 2), raios)

print(areas)

print(list(areas))

print(tuple(areas_lambda))

#OBS: Só é possivel ultilizar uma vez o resultado. Após ele será zerado.

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles',26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

c_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(cidades)
print(list(map(c_f, cidades)))

print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
