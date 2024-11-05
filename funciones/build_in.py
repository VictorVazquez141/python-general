''' 
Funciones integradas.
-Son utilizadas sin necesidad de modulos adicionales. Tienen tareas ya especificadas. 

POR EJEMPLO.

// Funciones de enstrada y salida //
print()
input()

//Conversión de tipo...//
int()
float()
str()
bool()
list()

'''
numeros = [2,76,52,4,8,3,4,7,98,32,5]

#El mas alto
num_masAlto = max(numeros) #max(): operación matematica que devuelve el valor mas alto
print(num_masAlto)

#el numero menor. Lo contrario de max()
num_masBajo = min(numeros)
print(num_masBajo)

#Redondeando decimales
numero = round(42.6859)
print(numero)

# retorna el valor falsr --> 0, vacio, False, None
resultado_bool = bool("cadena de Texto")
print(resultado_bool)#True

#Retorna el vallor true --> siempre y cuando todos los valores sean verdaderos 
resultado_all = all([[0,"string"], True,234])
print(resultado_all)

#suma total de ...
suma_total = sum(numeros)
print(suma_total)
