class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_deposito(self, amount):
        self.amount += amount
        return self

    def hacer_retiro(self, amount):
        self.amount -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.amount}")
        return self

    def transferir_dinero(self, amount, usuario): #bonus
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self


michael = Usuario ("michael")
jenny = Usuario ("jenny")
mario = Usuario ("mario")


michael.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_retiro(45).mostrar_balance_usuario()

jenny.hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(500).hacer_retiro(300).mostrar_balance_usuario()

mario.hacer_deposito(1500).hacer_retiro(1000).hacer_retiro(5000).hacer_retiro(3000).mostrar_balance_usuario()

jenny.transferir_dinero(400 ,michael) #bonus