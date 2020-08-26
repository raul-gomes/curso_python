from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(tuple(nome for nome in nomes if nome[0] == 'C'))


print(getsizeof('Geek'))
print(getsizeof(['Geek']))
print(getsizeof({'Geek'}))
print(getsizeof({1: 'Geek'}))

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
genarator_comp = getsizeof((x * 10 for x in range(1000)))
dict_comp = getsizeof({x:x * 10 for x in range(1000)})


print(f'List: {list_comp} / Set: {set_comp} / Generator: {genarator_comp} / Dictionary: {dict_comp}')
