from math import pi
from math import pow

def  valida(cadena):
    try:
        float(cadena)
        if float(cadena) > 0.0:
            return True
        else:
            return False
    except:
        return False

def bucle(cadena, magnitud):
    while not valida(cadena):
        print("ERROR. Introduce un número válido\n")
        cadena = input("\nIntroduce metros lineales de {}.....: ".format(magnitud))

    return cadena

def calculaPintura(area):

    _BOTE_METROS = 0.01
    _LITRO_METRO = 0.05

    boteAComprar = area * _BOTE_METROS

    litrosAComprar = area * _LITRO_METRO

    print("Necesitarás {} litro/s para pintar {} metro/s cuadrados de techo.\n".format(litrosAComprar, area))

    if boteAComprar > round(boteAComprar):
            boteAComprar = round(boteAComprar) + 1

    else:
            boteAComprar = round(boteAComprar)

    print("Debes comprar {} bote/s de pintura\n".format(boteAComprar))



while True:
    print("***************** ELIGE UNA OPCIÓN : *************************\n")
    print("1.- PINTAR UN CUADRADO............:\n")
    print("2.- PINTAR UN CÍRCULO ............:\n")
    opcion = input("Opción (1 / 2 / Salir)..: ")

    if opcion == "1":
        
        ancho = input("\nIntroduce metros lineales de ANCHO.....: ")
        ancho = bucle(ancho, "ANCHO")
        largo = input("\nIntroduce metros lineales de LARGO.....: ")
        largo = bucle(largo, "LARGO")

        anchoP = float(ancho)
        largoP = float(largo)

        area = anchoP * largoP
        calculaPintura(area)
  
    elif opcion == "2":

        #Fórmula Área Círculo ::....Pi R cuadrado ... PiR2
        radio = input("\nIntroduce el Radio del Círculo...:")
        radio = bucle(radio, "RADIO")

        radioP = float(radio)

        areaCirculo = pi*pow(radioP, 2)
        calculaPintura(areaCirculo)

    else:
        print("\nBye, bye....")
        break
    