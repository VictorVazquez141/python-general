'''
Función que reciba una lista  y devuelva el numero mayor dentro de ella
'''
#Declaramos la fución con el parametro de nombre 'lista'
def num_max (lista):
    mayor = lista[0] # mayor inicia como el primer elemento de la lista introducida
    
    for n in lista: #Hacemos el ciclo que recorra cada elemento(n) de la 'lista'
        
        # Si ese elemnto seleccionado es x valor, se denomina como "mayor" y lo devuelve para reconocerlo
        if n > mayor: 
            mayor = n
    return mayor
    
      # Asi con cada elemento recorrido de la lista, si encontro un numero mayor y los siguientes no lo superan, lo reconoce como el mayor
    
lista_usuario = [23,54,13,6,8,34,25]
print(num_max(lista_usuario))
