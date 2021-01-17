def esNumero(cadena):
    try:
        float(cadena)
        if float(cadena) > 0:
            return True
        else:
            return False

    except:
        return False

ancho = input("Introduce ancho ....: ")


while not esNumero(ancho):
    print("ERROR... Introduce un número de ANCHO correcto")
    ancho = input("Introduce ancho ....: ")

largo = input("Introduce largo ....: ")

while not esNumero(largo):
    print("ERROR... Introduce un número de LARGO correcto")
    largo = input("Introduce largo ....: ")


anchoN = float(ancho)
largoN = float(largo)


yardaCuadrada = 0.83612736 # metros cuadrados
metroCuadrado = 1.30795062 # yardas cuadradas

areaTotal = anchoN * largoN



opc = input("¿Quiéres el área en Metros Cuadrados o Yardas Cuadradas (M/Y)....?  ")

opc = opc.upper()#Lo paso a minúsculas, por si acaso

if opc == "M":
    areaYardas = areaTotal / yardaCuadrada
    print("{:.2f} m. de ancho y {:.2f} m. de largo son {:.4f} metros cuadrados o {:.4f} yardas cuadradas.".format(anchoN, largoN, areaTotal, areaYardas))

elif opc == "Y":
    areaMetros = areaTotal / metroCuadrado
    print("{:.2f} yardas de ancho y {:.2f} yardas de largo son {:.4f} yardas cuadradas o {:.4f} metros cuadrados.".format(anchoN, largoN, areaTotal, areaMetros))




