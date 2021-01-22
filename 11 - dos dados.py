from random import Random

numero = Random()

#Función generadora de números para dados
def generaNumeros(diccionario):

    for x in range(1000):
        resultado = str(numero.randint(1,12))

              
        if resultado == "2":
            diccionario[resultado] += 1

        elif resultado == "3":
            diccionario[resultado] += 1

        elif resultado == "4":
            diccionario[resultado] += 1

        elif resultado == "5":
            diccionario[resultado] += 1

        elif resultado == "6":
            diccionario[resultado] += 1

        elif resultado == "7":
            diccionario[resultado] += 1

        elif resultado == "8":
            diccionario[resultado] += 1

        elif resultado == "9":
            diccionario[resultado] += 1

        elif resultado == "10":
            diccionario[resultado] += 1

        elif resultado == "11":
            diccionario[resultado] += 1

        elif resultado == "12":
            diccionario[resultado] += 1

        

def muestraNumeros(diccionario):

    
    #Acumuladores
    frecAcumulada = 0


    print("{}       {}        {}           {}".format("Valor", "Frecuencia", "Frescuencia Acumulada", "Porcentaje"))

    for item in diccionario:

        frecAcumulada += diccionario[item]

        print("{:3s}              {:2d}               {:2d}                 {:3.2f} ".format(item, diccionario[item],frecAcumulada, diccionario[item]/1000*100 ))





dado = {

    "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,"6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,"12": 0

}



print("\nResultados de 2 dados: \n")
generaNumeros(dado)
muestraNumeros(dado)






