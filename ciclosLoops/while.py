"""
Loop While
- Es utilizado para ejecutar un bloque de codigo repetidamente, siempre y cuando una condición dada sea TRUE (verdadera)

****************************
while condición:           |
    # bloque de codigo     |
****************************
La condición es evaluada antes de la interación del bucle
Si la condición es verdadera se ejecuta el bucle 
Si la condición es falsa (False) el bucle termina y el programa continua el codigo 

"""

# Imprimir nuneros del 1 al 5 
contador = 1
while contador <= 5:
    print(contador)
    contador += 1 

# Bucle infinito
'''
while True:
    print("Ejecutando bucble infinito... Usa clt+C para cancelar bucle")
'''


'''
Break y continue 
-Estad declaraciones se pueden utilizar para controla r el flujo detro de un ciclo while
-break: se usa para salir del bucle inmediatamente
-continue: se usa para saltar el resto del codigo dentro del bucle y pasar a la siguiente iteración
 se define tambien como el volver a comenzar con el condicional de la iteración marcada
'''

# Break
contador_1 = 1
while True:
    print(contador_1)
    contador_1 += 1
    if contador_1 > 10:
        break # al ser mayor a 10 sale del bucle
print("\n")
# continue
contador_2 = 1
while contador_2 < 10:
    contador += 1
    if contador_2 % 2 == 0:
        continue # Salta la impresión para lo numeros pares
    print(contador_2)
    

