comedoresCadena = input("Número de personas que comen pizza....:  ")
numeroPizzasCadena = input("¿Cuántas pizzas a repartir........?   ")

pizzeros = int(comedoresCadena)
pizzas = int(numeroPizzasCadena)
if pizzeros % 2 == 0:
    numeroPorcionesPorPizza = pizzeros

else:
    numeroPorcionesPorPizza = pizzeros + 1

numPorcionesTotales = numeroPorcionesPorPizza * pizzas

print("{} pizzeros con {} pizzas.".format(pizzeros, pizzas))
print("Cada persona toma {} porciones".format(pizzas))
print("Sobran {} porciones.".format((numeroPorcionesPorPizza - pizzeros) * pizzas))



