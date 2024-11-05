'''
Strings Recargados 
Aqui se trabajan con string y con metodos diferentes utilizandolos para devolver valores variados (int, boolean, str)
'''

texto = "En el presente texto pdemos decir que sabemos programar en javascript, sql y proximamente python"
print("node.js" in texto) # FALSE (podemos hacerlo tambien con IF ELSE)

#Devolver un numero de letras 
size = len(texto) 
print(size) # 96

palabra = "otorrinolaringologo"

print(palabra.upper()) # MAYUSCULAS 
print(palabra.lower()) # minusculas 

print(palabra.count("o")) #Contar cuantas veces esta la o en existencia

palabra_1 = "otra palabra de prueba"
print(palabra_1.startswith("otra")) # True
print(palabra_1.endswith("frase")) # False
print(palabra_1.replace("otra","nueva"))
print(palabra_1.title()) #Cada inicio de palabra en mayuscuculas 

palabra_2 = "12345"
print(palabra_2.isdigit()) #Indica si el String tiene o es un valor de digito(s)


