class MathDojo:
    """Clase MathDojo."""

    def __init__(self):
        self.resultado = 0  # Estado de está se propiedad se mantiene en el objeto
 
    def sumar(self, num, *nums):  # *args
        self.resultado += num

        for n in nums:
            self.resultado += n
        return self
    
    def restar(self, num, *nums):
        self.resultado -= num

        for n in nums:
            self.resultado -= n
        return self


# Crear una instancia:
math_dojo = MathDojo()

# Para probar:
total = math_dojo.sumar(2).sumar(2, 5, 1).restar(3, 2)
print(total.resultado)  # debería imprimir 5

def sumar(*args):
    total = 0

    for num in args:
        total += num

    return total


resultado = sumar(2, 4, 1, 5, 20, 20, 100)
print(resultado)