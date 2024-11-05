'''
///////////// Tipos de valores ///////////
'''
# DE VALOR NUMERICO A STRING
# #############
# edad = 24
# print("Tengo", edad, "años de edad") #Simple concatenacion de valores string y numericos (no importan los espacios)
# print(f"Tengo: {edad} de edad") # un solo texto con f
# print("Tengo " + str(edad) +" años de edad")# modificamos el valor de la variable numerica a string(str) (importan los espacios de texto)

# ##############


'''
////////////// Operadores Aritmeticos ///////
Operadores basicos como "+ - / * %" son similares a JS 
'''
# ################

# print(238 / 6)
# print("Cadena "+"concatenada")
# print("tres veces "*3)
# print(29 % 6)
# print(44 % 7)
# # CAPTURA UNICAMENTE EL VALOR ENTRERO DE DIVISIONES (sin decimales)
# print(10 // 3) # "3".33333
# # Elevado a ...
# print(5 ** 3) # 125
# # OPERACIÓN COMPLEJA 
# print( 2 ** 3 + 15 - 3 / 6 - 1 // 2 )


# #DETECCION DE NUMEROS PARES O IMPARTES
# numero = 5
# if numero % 2==0: # Aqui se toma como condición que los residuos tienen que ser 0 para cumplir el numero par
#     print("El numero es par")
# else: 
#     print("El numero es impar")

# #ENCONTRAMOS EL DIA DE LA SEMANA INDICADO
# dias_totales = 10
# dias_de_la_semana = 7
# dia_de_la_semana = dias_totales % dias_de_la_semana
# print(dia_de_la_semana)  # Output: 3 (si hoy es 'lunes', en 10 días será jueves)

#################

'''
//////// Valores de comparación ///////
comparaciones basicas "<, >, <=, =>, ==, ===, !=" (La respuesta siempre es boolean)
'''
#COMPARACIÓN CON NUMEROS 
print(24/4 == 6) #True
print(32 * 2 != 64) #False
#COMPARACIÓN CON STRING
print("Morelos" == "morelos") #False (MAYUS, minus)
print("Ecatepec" != "Metepec") #True 
print("Ecatepec" != "Eca"+"tepec") #False
print("2" == 2) #False


