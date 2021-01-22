lista = [1, 3, 14, 9, -1,26, 15]

listaDobles = map(lambda x: x*2, lista) #Map usa 2 argumentos, la operación que hacemos sobre cada item y sobre 
                                        #que lista la hacemos

for item in listaDobles:
    print(item)
    
print(type(listaDobles))


listaPares = filter(lambda x: x % 2 == 0, lista)

print(type(listaPares))

listaP = []

for item in listaPares:
    print(item)
    listaP.append(item)


print(listaP)