# Actualizar valores en diccionarios y listas
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ]. #listo
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'. #listo
# En el directorio_deportes, cambia "Messi" por "Andrés". #listo
# Cambia el valor 20 en z a 30. #listo

x = [[5, 2, 3], [15, 8, 9]]
estudiantes = [
    {"first_name": "Michael", "last_name": "Bryant"},
    {"first_name": "John", "last_name": "Rosales"},
]
directorio_deportes = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "fútbol": ["Andrés", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 30}]


# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios
# de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])


estudiantes = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel


#Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
#la función imprima el valor almacenado en esa clave para cada diccionario. 
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

estudiantes = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)
#Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB

#Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel


#Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
#imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. 
def printInfo(some_dict):
    for key_name in some_dict:
        print(f"{len(some_dict[key_name])} {key_name.upper()}")
        for value in some_dict[key_name]:
            print(value)
        print("")

#Por ejemplo:
dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# salida:
7 #ubicaciones
San 
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 #instructores
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

