#Conjuntos creados con set()
#No se le pueden insertar conjuntos 
conjunto = set(["Dato1","Dato2"])
print(conjunto) #OK

#Conjuntos dentro de otros conjuntos (conjunto1 dentro de conjunto2)

conjunto1 = frozenset(["Dato3","Dato4"])#Esto es un conjunto encapsulado o inmutable
conjunto2 = {conjunto1,"Dato5","Dato6"} #conjunto dentro de otro
print(conjunto2)

#TEORIA DE CONJUNTOS 
"""
En este caso se toma desde la perspectiva del conjunto:
-Si el conjunto que se toma es a, el subconjunto es b
-Si el conjunto es b, el subconjunto es a
//Todo conjunto se tiene que tener dentro de las llaves {}
"""
conjunto_a = {1,2,3,4,5}
conjunto_b = {1,3,5}

# ejmplo con un condicional:
if conjunto_a.issubset(conjunto_b) == True: #el a es subconjunto de  b
    print("El conjunto a SI es sub del b") #false
else: #el b es sub del a
    print("El conjunto b es sub del a") #true

# ejemplo con signos de comparación:
#subconjunto de a
resultado = conjunto_b.issubset(conjunto_a) 
resultado = conjunto_b <= conjunto_a
print(resultado)
#conjunto de a
resultado = conjunto_b.issubset(conjunto_a) 
resultado = conjunto_b > conjunto_a
print(resultado)

#Para que se cumpla un sub tiene que ser solo algunos elementos del conjunto

'''
Aqui se elaboran ejercicios con lecturas en Chat GPT.

Conjunto = set(). Es una coleccióndesordenada de elementos únicos. Utilizados para 
operaciones matematicas como uniones, inserciones, diferencia y diferencia simetrica.
'''
# Se crean con set() o con {}

conjunto_vacio = set() 
print(conjunto_vacio) # set()

conjunto_llaves = {1,2,3,4,5,6}

# ------------ OPERACIONES BASICAS DE CONJUNTOS
# Añadir elemento
# conjunto_llaves.add(100) # {1,2,3,4,5,6,100}
conjunto_vacio.add(100) 
print(conjunto_vacio) # {100}
# Para eliminar elementos 
conjunto_vacio.remove(100)
conjunto_llaves.remove(4)
print(conjunto_llaves) 
print(conjunto_vacio)

# Metodo para unir conjuntos ( | o union())
conjunto_union = {7,8,9}
join = conjunto_llaves | conjunto_union
join_1 = conjunto_llaves.union(conjunto_union)
print(join)
print(join_1)

# Insercción y union son direferntes, esto es insercción
conjunto_1 = {3,7,5,1,8}
conjunto_2 = {2,4,5,7,8}
inserccion_1 = conjunto_1 & conjunto_2
print(inserccion_1)

conjunto_3 = {1,7,9,3,4}
inserccion_2 = conjunto_1.intersection(conjunto_3)
print(inserccion_2)


