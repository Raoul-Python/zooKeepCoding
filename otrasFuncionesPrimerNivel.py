def maximo(*l):#Recoger l parámetros numéricos y me los transforma en una lista
    if len(l)==0:
        return 0
    
    numMax = l[0]

    for x in range(1, len(l)):#Voy recorriendo la lista posición a posición
        if l[x] > numMax:
            numMax = l[x]

    return numMax

def minimo(*l):#Recoger l parámetros numéricos y me los transforma en una lista
    if len(l)==0:
        return 0
    
    numMax = l[0]

    for x in range(1, len(l)):#Voy recorriendo la lista posición a posición
        if l[x] < numMax:
            numMax = l[x]

    return numMax

def media(*l):
    suma = 0
    if len(l) == 0:
        return 0

    for i in l:
        suma += i

    return suma / len(l)

funciones = {

    "max": maximo,
    "min": minimo,
    "med" :media
}#El dicciionario funciones me guarda FUNCIONES como VALORES MAXIMO, MINIMO Y MEDIA


def devuelvemeUnaFuncion(nombreFuncion):

    nombreFuncion = nombreFuncion.lower()

    if nombreFuncion in funciones.keys():
        
        return funciones[nombreFuncion]#Me devuelve directamente la función

    else:
        return None

if __name__ == "__main__":

    """ y =[1, 5, -23, 45, -234]
    print(maximo(1, 15, 3, 9, -1))
    print(minimo(1, 15, 3, 9, -1))
    print(media(1, 15, 3, 9, -1))"""

    print(devuelvemeUnaFuncion("max")(1,15,3,9,-1))
    print(devuelvemeUnaFuncion("min")(1,15,3,9,-1))
    print(devuelvemeUnaFuncion("med")(1,15,3,9,-1))



