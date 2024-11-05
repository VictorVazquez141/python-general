password = input(" Ingresa tu contraseña: ")
confirmacion = input(" Confirma tu contraseña: ")

if password == confirmacion:
    print("La contraseña es correcta")
    
    tel1 = input("Ingresa tu telefono: ")
    tel2 = input("Confirma tu telefono: ")
    
    if len(tel1) == 10 & tel1 == tel2:
        print("Telefono correctamente ingresado")
    else: 
        print("El telefono no coincide o no es valido")
    
else: 
    print("Error. Corrobora tu contraseña")
    