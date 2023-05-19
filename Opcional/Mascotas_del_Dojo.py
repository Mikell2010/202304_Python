class Ninja:
    
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        self.mascota.comer()
        return self

    def bañar(self):
        self.mascota.sonido()
        return self
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.premios}, {self.comida_mascota}, {self.mascota}"



class Mascota:

    def __init__(self, name, tipo, golosinas, salud, energia, ruido):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 50
        self.ruido = ruido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud +=10
        return self
        
    def jugar(self):
        self.salud += 5
        
        return self

    def sonido(self):
        print(self.ruido)

    def __str__(self):
        return f"{self.name}, {self.tipo}, {self.golosinas}, {self.salud}, {self.energia}, {self.ruido}"
    

mi_mascota = Mascota("fofi","perro", "golosina sabrosa", 100, 50, "ladrar")#esto es una instancia de la clase Mascota
print(mi_mascota)

mi_ninja = Ninja("Michael", "Perez", "Premio 1", "carne", mi_mascota)#esto es una instancia de la clase Ninja mas el atributo mi_mascota
print(mi_ninja)



