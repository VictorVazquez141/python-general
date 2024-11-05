'''
CILCLOS ANIDADOS 
-Son bucles dentro de otros bucles. Se refiere a que hay uno dentro de otro para realizar tareas repetitivas
de manera estructurada y eficiente
-Son utiles al recorrer estructuras de datos complejas como listas de listas o matrices
'''
# Listas dentro de una lista
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matriz[0],"\n")

print("Matriz.")
contador = 1
for lista in matriz:
    print(lista)
    for i in lista:
        print(f"{contador}: {i}")
    contador += 1

# Ejemplo de recorrido de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][2] + matriz[2][0]) #Sumas comn matrices