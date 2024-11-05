lista = ["Bienvenida", "Victor", "1234", 343, True, False, None] #Modificable
print(lista[2])

tupla = ("esto","es",1,"tupla","y no se modifica","como el array") #Inmodificable
print(tupla[3])

lista[3] = 141
print(lista) #Modifica el array

# tupla[2] = "Cara"
# print(tupla) #Error


# Set (conjuntos)

conjunto = {
    "Victor",
    False,
    3.1416,
    "Manuel"
}
print("Victor" in conjunto)

diccionario = {
    "nombre": "Victor manuel",
    "apellido": "Vazquez",
    "Edad": 24,
    "estatura": "1.79"
}
print(diccionario["apellido"],diccionario["estatura"])