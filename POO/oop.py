''' Principios'''
# Definición de una clases

# class Celular(): # Clase "celular"
#     # Atributos
#     marca = "Samsung"
#     modelo = "S80"
#     camara = "48Mp"
    
# celular_1 = Celular() # Objeto "Celular 1"
# celular_2 = Celular() # Objeto "Celular 2"
# print(celular_1.camara)
# celular_2.marca = "iPhone" # atributos edidtados depende a la clase
# celular_2.modelo = "13 pro max"
# print(celular_2.marca, celular_2.modelo)



# '''Ejercicios de atributos y metodos'''
# class Usuario: 
#     # Metodo constructor...
#     # self hace referencia a la misma clase, y en seguida se determinan sus atributos (parmaetros)
#     def __init__(self, nombre, apellido, edad, sexo): 
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.sexo = sexo
    
# # creamos un objeto nuevo con la clase Personaje
# user_estudiante = Usuario("Alvaro", "Robles", 19, "Hombre") #Indicamos los atributos del objeto
# print(user_estudiante.nombre, user_estudiante.edad)

'''Ejercico Clase: Estudiante'''
class Estudiante:
    # Atributos
    def __init__(self, nombre, edad, grado): 
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    # Metodos
    def estudiando(self):
        print(f'El estudiante {self.nombre} está estudiando')
    def no_estudiando(self):
        print(f'El estudiante {self.nombre} NO esta estudiando')

# Inicializamos la clase
# Ahora los digita el usuario
nombre = input("Introduce tu nombre: ")
edad = input("Intriduce tu edad: ")
grado = input("Introduce tu grado: ")

estudiante_1 = Estudiante(nombre,edad,grado)
print(f'''
      Datos del estudiante: 
        Nombre: {nombre}
        Edad: {edad}
        Grado: {grado}
      ''')

estudiar = input("Estatus: ")
if (estudiar.lower == "estudiando"):
    estudiante_1.estudiando()
else:
    estudiante_1.no_estudiando()



