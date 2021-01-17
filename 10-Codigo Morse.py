codigo_morse = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..","E":".", "F":"..-.","G":"--.","H":"....", "I":"..","J":".---",
    "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...","T":"-",
    "U":"..-", "V":"..._", "W":".--", "X":"-..-","Y":"-.--","Z":"--..", "1":".----", "2":"..---","3":"...--",
    "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9": "----.", "0":"-----"
}

#for clave in codigo_morse:

 #   print("{} -> {}".format(clave,codigo_morse[clave]))


frase = input("Escribe algo....: ")
cadena = ""

for letra in frase:
    letra = letra.upper()

    if letra == " ":
        cadena += " \n"
    else:
        cadena += codigo_morse[letra] + " "

print(cadena)



    

