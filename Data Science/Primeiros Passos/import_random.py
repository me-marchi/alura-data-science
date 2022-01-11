from random import randrange, seed

seed(11)
print(randrange(0,11))
print(randrange(0,11))
print(randrange(0,11))

lista = []

for i in range(8):  
    lista.append(randrange(0,11))
print(lista)