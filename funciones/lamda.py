'''
FUNCIONES LAMBDA
-Funciones anonimas, es decir, no tienen nombre explicito. Son utiles para operaciones pequeñas y rapudas, definidas
por la palabra clave 'lambda'

///Ejemplo:
lambda argumentos: expresión 
'''

# suma
operacion = lambda a, b, c : a * b - c 
print(operacion(6,4,2))

'''
Usos comunes de la función LAMBDA

// Comunmente utilizadas para FUNCIONES DE ORDEN SUPERIOR: 'map()', 'filter()' y 'sorted()'
'''

# con map(): Aplica una función a todos los elementos de una lista (u otro iterable)
numeros = [2,5,8,4,9]
cuadrados = map(lambda x: x ** 2, numeros) #lambda x toma valores de cada elemento de la lista numeros
print(list(cuadrados)) # imprimir en fomra de lista para que tomen el formato de 'numeros'
