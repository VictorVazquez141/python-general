'''
TUPLAS 
-Son estructuras de datos que pueden almacenar colecciones ordenadas de elementos 
-Las tuplas son inmutables, es decir, una vez creados no se pueden modificar (Garantiza que los datos no se alteren accidentalmente)

////// Usos //////
-Registros: Almacenar datos heterogeneos 
-Claves de diccionario: (POO)
-Devolución de multiples valores: las personas pueden devolver multiples valores empaquetados en tuplas
'''

# Tipos de tuplas

tupla_1 = () # Vacia
tupla_2 = (1,2,3,4,5)
tupla_2_1 = (23, "'String'", False, 3.1416) # Multiples valores 
tupla_3 = (12,) # de un solo elemento (se necesita una "," al final)
tupla_4 = 22,5,7,2,3,1 # Empaquetado de tupla

# Acceder por indices (Lo mismo para los indices con numeros negativos)
print(tupla_2[1])
'''
Los accesos hacia los datos de las tuplas son similares al de las listas, solo utilizando los [ ]
'''

# DESEPMAQUETADO
print(f"Tupla: {tupla_2_1}")
a, b, c, d = tupla_2_1
print("\nDesempaquetados: ")
print(f"Position a: {a}")
print(f"Position b: {b}")
print(f"Position c: {c}")
print(f"Position d: {d}")

# Desempaquetado parcial
mi_tupla = (1, 2, 3, 4, 5)
a, b, *resto = mi_tupla
print(a)      # Salida: 1
print(b)      # Salida: 2
print(resto)  # Salida: [3, 4, 5]

# Ignorar valores (ignoramos con el _ )
a, _, c = (1, 2, 3)
print(a)  # Salida: 1
print(c)  # Salida: 3


