'''
Devolver un resultado si un numero es par o inpar
'''
number_user = input("Introduce un numero: ")

def numero_entero(number_user):
    number_user = int(number_user) 

    if number_user %2 == 0: print("El numero es par!") 
    else: print("El numero es inpar")

numero_entero(number_user)

