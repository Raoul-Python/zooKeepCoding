from datetime import datetime

def dameMes(mes):
    meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    return meses[mes-1]

def dameTiempo():

    objeto = datetime.now()
    print("Día:",objeto.day)

    print("Mes:",dameMes(objeto.month)) 
    print("Año:",objeto.year)

    print("Hora: {}:{}:{}".format(objeto.hour, objeto.minute, objeto.second))

todo = datetime.now()

edad =int(input("¿Cuántos años tienes? "))
edadJubilacion = int(input("¿A qué edad te jubilarás? "))

if edadJubilacion-edad > 0:

    print("Te quedan {} años para jubilarte.".format(edadJubilacion-edad))
    print("Estamos en el año {}, te jubilarás en {}".format(todo.year, todo.year+(edadJubilacion-edad)))
else:
    print("Ya puedes jubilarte......")

#print(type(objeto.month))