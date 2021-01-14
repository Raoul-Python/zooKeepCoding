def normal(x):
    return x

def sumaTodos(limite, funcion):
    resultado = 0

    for i in range(limite+1):
        resultado += funcion(i)

    return resultado

def cuadrado(y):
    return y**2

n = 100
n = 3

#Funciones de 1er nivel, funciones que admiten FUNCIONES COMO PARÁMETROS 
print(sumaTodos(n, normal))
print(sumaTodos(n, cuadrado))

