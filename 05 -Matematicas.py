
def suma(x, y):
    return x+y

def resta(x, y):
    return x-y

def producto(x,y):
    return x*y

def division(x,y):
    return x/y

def validaNumero(cadena):
    try:
        float(cadena)

        if float(cadena) > 0:
            return True
        else:
            print("ERROR. Introduce un número positivo")
            return False
    except:
        print("\nNúmero no válido. Introduce un número entero y positivo.\n")
        return False

def mostrarResultados(n1, n2):
    print("\nResultados de las operaciones matemáticas básicas...:\n")
    print("{} + {} = {}\n".format(n1, n2, suma(n1,n2)))
    print("{} - {} = {}\n".format(n1, n2, resta(n1,n2)))
    print("{} x {} = {}\n".format(n1, n2, producto(n1,n2)))
    print("{} / {} = {}\n".format(n1, n2, division(n1,n2)))

numero1 = input("Introdue el primer número.... >>>  ")


while not validaNumero(numero1):# Mientras validaNumero(numero1)nos devuelva falso
    numero1 = input("Introdue el primer número.... >>>  ")


n1 = float(numero1)

numero2 = input("Introduce el segundo número.... >>> ")


while not validaNumero(numero2):
    numero2 = input("Introduce el segundo número.... >>> ")

n2 = float(numero2)

mostrarResultados(n1, n2)







