# '''Ejercicios UDEMY'''

# datos_type = [int,str,float]


# almacen = []
# usuarios = []

# peticion_1 = input("Introduce tu producto: ")
# peticion_2 = input("Introduce tu nombre: ")

# def almacernar():
#     print("Esto es una función para almacenar!")
#     almacen.append(peticion_1)
#     print(almacen)
    
# def registro_usuario():
#     print("Registrando usuario...")
#     usuarios.append(peticion_2)
#     print(usuarios)
    
    
# almacernar()
# registro_usuario()

# '''------------Calculo de daño por segundos'''
# def damage(damage, speed, time):
#     if damage <0 or speed < 0:
#         return "Invalid"
    
#     if time == "second":
#         return damage * speed *1
        
#     if time == "minute":
#         return damage * speed *60
            
#     if time == "hour":
#         return damage * speed * 3600
    

# print(damage(-2,2, "hour"))


# '''-------------Incremento de un numero entero al anterior'''
# def incremento(n):
#     return n +1

# print(incremento(9))


# '''-----------------De minutos a segundos'''
# def conversion(numero):
#     return numero * 60

# print(conversion(5)) # 300

# '''------------Calcular area de un triangulo'''
# def triangulo(base,altura):
#     return base * altura /2

# print(triangulo(3,2))

# '''--------------Encontrar el descuento'''
# def descuento(price, desc):
#     return desc*price /100

# print(descuento(1500,50))


# '''-----------Radianes en grados'''
# from math import pi 
# def radians(grados):
#     return round(grados* (180/pi),1)

# print(radians(20))


# '''------------Numero de curzon'''
# def curzon(num):
#     crz =  1 + 2**num % 1 + 2**num
#     if crz % crz == 0:
#         return True
#     else: return False

# print(curzon(10))


# '''-----------Suma de resistencias'''
# def series(lst):
#     return sum(lst)

# print(series([1,3,5,6]))


# '''-----------Calculadora basica'''
# def calculadora(num1, signo, num2):
#     if num1 == 0 or num2 == 0:
#         return "No es divicible en 0"
#     elif signo == "-":
#         return num1 - num2
#     elif signo == "*":
#         return num1 * num2
#     elif signo == "/":
#         return num1 / num2
#     elif signo == "+":
#         return num1 + num2

# print(calculadora(0, "*",9))

# '''-----------¿Que tan pesado es?'''
# from math import pi
# def masa(r, h):
#     return round(pi* (r**2) *h /1000,1)

# print(masa(4,10))

'''----Encontrar el numero impar
def find_odd(lst):
    lista=[]
    # Recorrer lista ingresada
    for i in lst:
        while i:
            print()
            len(lst) += 1
            
        if i == map(len(lista)):
            print("repetido")
            

print(find_odd([1,2,4,2,1]))
'''


'''--------Devuelve factorial'''
# import math 
# def factorial(num):
#     return math.factorial(num)

# print(factorial(3))
# print(factorial(5))
# print(factorial(13))

'''---------Encontrar el numero que falta'''
# def faltante(lst):
#     ordenada = sorted(lst)
#     lista=[]
#     for i in ordenada:
#         lista.append(i)
#         # print(lista)
#         if i != len(ordenada):
#             print(i+1)
    
    
# print(faltante([1,3,4,8,7,5,6,9]))

'''-------Volumen total de cajas'''

# def volumen_total(cajas): # en este parametro se indica la entrada de un array [] sin necesidad de definirla
#     total_vol = 0 # contador de cajas
#     for caja in cajas:
#         largo, alto, ancho = caja  # Indicamos las dimenciones de la(s) caja(s)
#         volumen= largo*ancho*alto 
#         total_vol += volumen
    
#     return total_vol

# print(volumen_total([(3,2,5),(4,3,6),(2,2,2),(5,4,3)]))
    

'''Numero es par o no'''
# def num_par(num):
#     if num %2 == 0:
#         return f"El numero {num} es par"
#     else: 
#         return f"El numero {num} es inpar"
    
# print(num_par(2))
# print(num_par(5))

# Modificación para el primer commit 

'''función que duplique los numeros de una lista (lambda)'''
def duplication(lista):
    lista = list(map(lambda x: x*2, lista))
    print(lista)
    
duplication([2,4,6,8,10])