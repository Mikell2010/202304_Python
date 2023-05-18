class CuentaBancaria:
    cuentas = []#bonus
    def __init__(self, name, balance, tasa_interes):
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
        return f"{self.balance}"
        

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self
    
    @classmethod #bonus
    def imprimir_todas_las_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()
    



class Usuario:

    def __init__(self, name):
        self.name = name
        self.cuenta = CuentaBancaria(balance=0, tasa_interes=0.01, name=name)

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.cuenta.mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self, amount, usuario): #bonus
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self

Michael = Usuario("Michael")
Michael.cuenta.deposito(100)
Michael.mostrar_balance_usuario()












