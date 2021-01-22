class Perro():

    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        

    def ladrar(self):
        if self.peso > 8:
            print("Guau, Gua")
        else:
            print("guau, guay")

    def __str__(self):
        return "Perro {} edad {} años, peso {} kgs".format(self.nombre, self.edad, self.peso)
        



if __name__ == "__main__":


    Salchicho = Perro("Salchicho", 15, 7.5)

    print(Salchicho.nombre)
    print(Salchicho.peso)