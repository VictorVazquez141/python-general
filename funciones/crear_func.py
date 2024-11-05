'''
FUNCIONES PROPIAS 
-se definen con la palabra 'def' y en seguida el nombre de la función, seguido de '():' 

EJEMPLO:
def nombre_funcion (parametros):
    #Cuerpo de la función
    #codigo ejecutante al llamar la función
    
    return resultado # Opcional...

'''
# Ejemplo con una función sin parametros 
def saludar():
    print("Hi, the 'def' is a function!")

saludar() #De esta forma se llaman y se ejecutan 


#Ejecutando funciones con parametros 
def nameUser(nombre,apellido):
    print(f"Hi user: {nombre} {apellido}\n")
    
nameUser("victor","Vazquez")

#Retorno de valores (manejo de datos)
def password_random (num):
    list_leter = "abcdefg"
    number_int = str(num)
    num = int(number_int[0])
    c1 = num - 2 
    c2 = num 
    c3 = num - 5
    g_password = f"{list_leter[c1]}{list_leter[c2]}{list_leter[c3]}{num*2}"
    print(g_password)
'''
password_random(1) # gid16: (posicionamientos de las letras y el numero '8' x2
'''

import random
#Generador de contraseñas
def g_contraseña(usuario):
    usuario = str(usuario)
    if usuario: 
        print("Generando contraseña...")
        contraseña = []
        while len(contraseña) < 10:
            numero_rand = random.randint(1,100)
            contraseña.append(numero_rand)
            continue
        
        print(usuario,contraseña)
    else:
        print("El usuario no es valido.")
'''
g_contraseña(input("Escribe tu usuario: "))
'''


# parametro args
def suma(*numeros): #El * indica que sera una lista de datos a ingresar (o sea mas de uno)
    return sum(numeros)

resultado = suma(2,3,4,5,6,7,4)
print(resultado)
