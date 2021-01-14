import math

def sumaTodos(limitTo):
    suma = 0
    for i in range(limitTo+1):
        suma += i

    return suma


def sumaCuadrados(limitTo):
    resultado = 0
    for x in range(limitTo+1):
        resultado = math.pow(x, 2)

    return resultado

if __name__ == "__main__":
    print(sumaCuadrados(4))

    n =100
    print("La suma de todos los números del 1 al {} es {}".format(n, sumaTodos(n)))
