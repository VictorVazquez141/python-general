# DICCIONARIOS REFERENTE A LO QUE ES LENGUAJE tipo JSON u Objetos
persona = {
    "Nombre": "Victor Manuel",
    "Apellido": "Vazquez Ramirez",
    "edad": 24,
    "signo": "Acuario"
}

libros = {
    0 : "Matematicas",
    1 : "Españor",
    2 : "Historia",
    3 : "Fisica"
}

clave1 = persona.keys() #Simplemente devuelve las claves de cada elemento (JSON, DICCIONARIO)
print(f"->print hecho con 'keys' : {clave1}") 

clave2 = persona.get("edad") #Si no encuentra lo que se le pide continua el programa
print(f"->print hecho con 'get' : {clave2}") 

clave3 = libros.clear() #Esto elimina todo lo de la lista (objeto)
print(f"->Esto es lo que muestra de 'libros' con el clear() : {clave3} o {libros}")

clave4 = persona.pop("signo") #Elimina el elemento indicado
print(f"->print que elimina un elemento de persona: Eliminado = {clave4} by ->",persona)
