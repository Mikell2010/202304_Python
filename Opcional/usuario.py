class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_deposito(self, amount):
        self.amount += amount

    def hacer_retiro(self, amount):
        self.amount -= amount

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.amount}")

    def transferir_dinero(self, amount, usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()


michael = Usuario ("michael")
jenny = Usuario ("jenny")
mario = Usuario ("mario")


michael.hacer_deposito(100)
michael.hacer_deposito(200)
michael.hacer_deposito(50)
michael.hacer_retiro(45)
michael.mostrar_balance_usuario()

jenny.hacer_deposito(1000)
jenny.hacer_deposito(1000)
jenny.hacer_retiro(500)
jenny.hacer_retiro(300)
jenny.mostrar_balance_usuario()

mario.hacer_deposito(1500)
mario.hacer_retiro(1000)
mario.hacer_retiro(5000)
mario.hacer_retiro(3000)
mario.mostrar_balance_usuario()

jenny.transferir_dinero(400 ,michael)