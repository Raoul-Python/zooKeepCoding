def sumaTodos(limitTo):
    suma = 0
    for i in range(limitTo+1):
        suma += i

    return suma
n =100
print("La suma de todos los números del 1 al {} es {}".format(n, sumaTodos(n)))




