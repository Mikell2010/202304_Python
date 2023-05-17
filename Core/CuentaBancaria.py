class CuentaBancaria:
    cuentas = []#bonus
    def __init__(self,name):
        self.tasa_interes = 0.01
        self.balance = 0
        self.name = name
        CuentaBancaria.cuentas.append(self)#bonus
        
    def deposito(self, balance):
        self.balance += balance
        return self

    def retiro(self, balance):
        if self.balance - balance >=0:
            self.balance -= balance
        else:
            print("Fondos insuficientes: cobrando una tarifa $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"Usuario: {self.name}, Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self
    
    @classmethod #bonus
    def imprimir_todas_las_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()
    


Michael= CuentaBancaria("Michael")
#print(Michael.balance)

Jenny= CuentaBancaria("Jenny")
#print(Jenny.balance)

Michael.deposito(1000).deposito(2000).deposito(3000).retiro(1000).generar_interes().mostrar_info_cuenta()
Jenny.deposito(1000).deposito(2000).retiro(1000).retiro(2000).retiro(3000).retiro(4000).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()#bonus

#bonus:utiliza un metodo de clase para imprimir todas las instancias de la
#informacion de una cuenta bancaria.