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


_BOTE_METROS = 0.01
_LITRO_METRO = 0.05

ancho = input("\nIntroduce metros lineales de ANCHO.....: ")

ancho = bucle(ancho, "ANCHO")


largo = input("\nIntroduce metros lineales de LARGO.....: ")

largo = bucle(largo, "LARGO")

"""while not valida(ancho):
    print("ERROR. Introduce un número válido\n")
    ancho = input("\nIntroduce metros lineales de ANCHO.....: ")

while not valida(largo):
    print("ERROR. Introduce un número válido\n")
    largo = input("\nIntroduce metros lineales de LARGO.....: ")"""



anchoP = float(ancho)
largoP = float(largo)

area = anchoP * largoP

boteAComprar = area * _BOTE_METROS

litrosAComprar = area * _LITRO_METRO

print("Necesitarás {} litro/s para pintar {} metro/s cuadrados de techo.\n".format(litrosAComprar, area))

if boteAComprar > round(boteAComprar):
    boteAComprar = round(boteAComprar) + 1

else:
    boteAComprar = round(boteAComprar)


print("Debes comprar {} bote/s de pintura".format(boteAComprar))

