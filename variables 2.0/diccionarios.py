#Creando diccionarios cin dict()
diccionario = dict(nombre="victor", apellido="Vazquez") #Sus parametros son algo= significado
print(diccionario)
#Al imprimirse la variable se muestra como un objeto {"x": "y"}

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario_1= {frozenset(["Victor","Vazquez"]): "1514634"}
print(diccionario_1)

# Diccionario con fromkeys para indicar una iteración con un tipo de valor 
diccionario_1 = dict.fromkeys("ABCDE", "vocal")
print(diccionario_1)

print("\n")
"""
Un diccionario es una colección desordenada y mutuable de elementos.
Cada elemento cuenta con una clave (key) y un valor (value). Se utilizan 
para almacenar datos en pares de clave-valor, haciendo mas eficiente
acceder a sus valores por sus claves (las claves son unicas).
"""
# Ejemplo de la sintaxis ({}, : )

diccionario_a = {
    "nombre": "Victor",
    "edad": 24,
    "ciudad": "Tenancingo"
}

# OPERACIONES COMUNES CON DICCIONARIOS 

print(diccionario_a)
print(diccionario_a["nombre"]) #obtener un valor mediante la key

diccionario_a["edad"] = 23 # Actualizamos un valor 
diccionario_a["pais"] = "Mexico" # Agregamos un par (key:value)
diccionario_a["apellido"] = "Vazquez"
del diccionario_a["ciudad"] #Eliminar un par
print(diccionario_a)

#Comprovación de clave con condicional IF
if "nombre" in diccionario_a:
    print("Nombre si se encuentra en le diccionario_a\n")

#Recorrer el diccionario con el ciclo for
for key, value in diccionario_a.items():
    print(f'clave: {key}, valor: {value}')