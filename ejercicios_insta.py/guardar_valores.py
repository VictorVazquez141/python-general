'''
Programa que guarde los valores en listas definidas

// Registro de alumnos
'''
lista_nombres = []
lista_apellidos = []
lista_edades = []
alumnos = []

print("Registro de alumnos.\n")

nombre_input = input("Nombre: ")
apellido_input = input("Apellido: ")
edad_input = input("Edad: ")

def registros(nombre, apellido, edad):
    edad = int(edad)
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)
    lista_edades.append(edad)
    print(f"\nNombre:{lista_nombres}\nApellido:{lista_apellidos}\nEdad:{lista_edades}")


registros(nombre_input,apellido_input,edad_input)
    
    
    
