# LIST creando una lista 
lista = list(["Hola","Victor",10])
print(lista)

print(len(lista)) # devuelve los elementos de la listas

#APPEND  agrega un elemento al final de  la lista
lista.append("Agregado")
print(lista)

#INSERT agrga un elemento en una posición exacta
lista.insert(2, 24)
print(lista)

#EXTEND  agrega varios elementos a la lista
lista.extend([True,5.7])
print(lista)

#POP elimina el elemento x de la lista 
lista.pop(3)
lista.pop(-1) #Elimina el ultimo elemento de la lista
print(lista)

#REMOVE elimina un elemento especifico de la lista 
lista.remove("Agregado")
print(lista)

#SORT ordena los elementos de forma acendente
numeracion = list([12,43,True,False,1.2])
numeracion.sort(reverse=True) #Del mayor al menor
print(f"This is whit soft in reverse: {numeracion}")
numeracion.sort() #Del menor al mayor
print(f"This ir whit sort: {numeracion}")

#REVERSE invierte toda la lista 
numeracion.reverse()
print(f"This is with riverse: {numeracion}")

# #CLEAR elimina todos los elementos de la lista 
# lista.clear()
# print("Ahora tu lista es: " +lista)