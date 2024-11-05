'''
EJERCICIOS
'''


#Funcion para agregar alumnos con su nombre y edad
def listAlumnos(cantidad):
    alumnos = []
    for i in range(5):
        nombre = input("Ingresa nombre: ")
        edad = int(input("Ingresa la edad: ")) #En automatico es un valor entero
        alumno = (nombre, edad)
        alumnos.append(alumno)