# Estos son solo metodos aplicados unicamente a cadenas 

cadena1 = "Hola mundo"
cadena2 = "cadena de pruebas"

# print(dir(cadena1)) #Con el dir mostramos todas las cosas que sde pueden hacer con el objeto indtroducido dir()

# print(dir(1234))

# metod1 = cadena2.upper() #declaración de metodo para todo en mayusculas 
# print(metod1);
# print("This is My Texto VATO".lower()) #Todo en minuscula 


texto1 = "lorem Ipsum dolor sit am equivalents et dolor sit amet et al."
word1 = "This is my word"
pin = "343"
placa = "VJSBPL"


# FIND
# print(texto1.find("et"))
# print(word1.find("m"))

# # INDEX
# print(word1.index("i")) #Ayuda a encontrar coincidencias o aparición del calor especificado 

# # ISNUMERIC
# print(word1.isnumeric())
# print(pin.isnumeric())

# # ALPHANUMERIC
# print(pin.isalpha())
# print(placa.isalpha()) #Solo acepta valores de la A a la Z unicamente

# # COUNT
# print(word1.count("at"))
# print(texto1.count("sit")) #Revisa y cuenta que hay dos coincidencias dentro de la variable y devuelve su cantidad

# # LEN (cuenta los caracteres de una cadena) (ES UNA FUNCION)
# print(len(word1))
# print(len(pin))


#STARTSWITH (muestra en valores boleanos el inicio de las cadenas) ENDSWITH (viseversa)
cadena3 = "Welcome to my house"
pin1 = "141"

# print(cadena3.startswith("t")) # false
# print(cadena3.startswith("w")) # false 
# print(cadena3.endswith("e")) # false

#REPLASE (el primer parametro señala lo que se quiere remplazar y el segundo lo que lo remplasará)
print(pin1+" Ahora vale: "+pin1.replace("41", "17"))
print(cadena3+" Ahora vale: "+cadena3.replace("house", "school"))


# SPLIT (devuelve una separación de cadenas con la separacion de elementos en matriz)
print(cadena3.split(" "))
print(cadena3[0])



'''
FORMATOS CON STRINGS
'''
nombre = "victor"
apellido =  "Vazquez"

formato_v1 = "Mi nombre es "+nombre+" y mi apellidpo "+apellido
print(formato_v1)

formato_v2 = "Hola, mi nombre es {} y me apellido {}. esta versión utiliza 'format'".format(nombre,apellido)
print(formato_v2)