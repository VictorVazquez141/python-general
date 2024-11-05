#Pedir al usuario que diga cualquier texto real 
## Calcular cuanto tarda en decir la frase
## Calcular las palabras que dijo el usuario

print("--------------------")
texto_user = input("Bienvenido. Porfavor ingresa un texto: ")

numero_palabras = texto_user.split(" ")
cantidad_palabras = len(numero_palabras)
print(f"Tu ingresaste: {cantidad_palabras} palabras y te tardaste {cantidad_palabras /2} en decirlas")

if cantidad_palabras >= 10 :
    print("Esas fueron suficientes palabras por decir")
if cantidad_palabras < 10:
    print("Esas fueron pocas palabras")

