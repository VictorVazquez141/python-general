'''POO con Minecraft'''

#Creación de personajes
class Personaje:  #Clase padre
    # Metodo constructor 
    def __init__(self, nombre,rol,skin):
        self.nombre = nombre 
        self.rol = rol
        self.skin = skin
    #Metodos
    def moverse(self):
        print(f'{self.nombre}: Se ha movido sobre X,Y,Z')
    def accion(slef):
        print(f'{slef.nombre}: Ha creado una mesa de crafteo')
        



