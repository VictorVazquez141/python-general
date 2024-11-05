'''
////////// Listas 
-Colecciones ordenadas mutables, pueden contenenr diferentes tipos de elementos (incluso otras listas)
'''
lista_1 = []
lista_2 = [1,2,3,4,5,6]
list_misx = [25,False,"string_1",2.6]
listas_lista = [[1,4,7], [2,5,8], [3,6,9]]

# Su acceso es igual al de los conjuntos 
print(listas_lista[1][2]) # 8
# Agregar 
lista_2.append(123)
print(lista_2)

'''
//////////// METODOS COMUNES PARA LISTAS /////////
'''
lista_3 = [1,2,3,4,5,6,7,8,9,0]
print(f"Nueva lsita: {lista_3}")
print("\n///// Añadir elementos /////") 
# AÑADIR ELEMETNOS ("append()", "extend()", "insert()")
lista_3.append(15), print(f"Con .append(15): {lista_3}") # Añadir en ultima posición 
lista_3.extend([30]), print(f"Con extend([30]): {lista_3}") # Se utiliza la función de corchetes dentro de los parentesis 
lista_3.insert(0,0), print(f"Con insert('index','value'): {lista_3}") # Se pide la posición (index) del valor a insertar, y despues mismo valor 

print("\n///// Eliminar elementos /////") 
lista_3.remove(30), print(f"Con remove(30): {lista_3}")
lista_3.pop(), print(f"Con pop(): {lista_3}") # Eliminamos el ultimo elemento por defecto (podemos indicar el index a borrar)
lista_3.clear(), print(f"Con clear(): {lista_3} => Esta vacia")

lista_4 =[1,3,8,6,9,42,5,7,22,4,76,49,25] 
print(f"\nNueva lsita {lista_4}")
print("///// Ordenar y revertir elementos /////\n") 

lista_4.sort(), print(f"Con sort() se acomoda la lista: {lista_4}") # En automatico los oderdena de menor a mayor
lista_4.reverse(), print(f"Con reverse(): {lista_4}") # Los aplica de reversa pero ordenados de mayor a menor

lista_4_copia = lista_4.copy() # Copia
print(lista_4_copia)

# # Filtrar elemntos en una lista
# pares = [x for x in range(20) if x % 2 == 0]
# print(f"\nPares de una lista: {pares}")


