#Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, 
#desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
def contar(num):
    lista = list(range(num, -1, -1))
    return lista

print(contar(5))
#resultado [5, 4, 3, 2, 1, 0]

#Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

print(imprimir_y_devolver([1,2]))
#resultado 1 2 

#Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
def primero_mas_longitud(lista):
    return lista[0] + len(lista)

print(primero_mas_longitud([1,2,3,4,5]))
#resultado 6

#Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista
#original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. 
#Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False
    
    segundo_valor = lista[1]
    nueva_lista = []

    for valor in lista:
        if valor > segundo_valor:
            nueva_lista.append(valor)
    
    print(len(nueva_lista))
    return nueva_lista


print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))
#resultado 3 [5,3,4] False

#Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
#La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
def length_and_value(tamaño,valor):
    lista = [valor] * tamaño
    return lista

resultado = length_and_value(4,7)
print(resultado)
#resultado [7,7,7,7]
resultado = length_and_value(6,2)
print(resultado)
#resultado [2,2,2,2,2,2]

#o esta esta otra solucion
def length_and_value(tamaño,valor):
    output = []
    for i in range(0, tamaño):
        output.append(valor)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))

    