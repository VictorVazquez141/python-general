'''
/// JUEGO DE PIEDRA, PAPEL O TIJERA ///
Elementos nuevos a utilizar y conocer:
- def (funciones): Crea codigo reutilizable con tarea especifica que adapta parametros de entrada y devuelve un valor 

- rand(random): En python se utiliza para la generación de NUMEROS aleatorios y realizar OPERACIONES con aleatoriedad

- not o not is
- range 
'''
import random 

lista = ['piedra','papel','tijera']
print("\nBenvenido a piedra, papel o tijera! :)")
cpu_choice = random.choice(lista)
user_choice = input("Escoge tu iopción (piedra, papel o tijera): ")

def info ():
    print(f"CPU eligió: {cpu_choice} y el usuario {user_choice}\n")

def usuario (): 
    print(f"Gana el usuario con {user_choice.upper()}")
    
def cpu ():
    print(f"Gana el CPU con {cpu_choice.upper()}")
    

if user_choice == cpu_choice:
    info()
    print("Es un empate!")
elif user_choice == 'piedra' and cpu_choice == 'papel':
    info()
    cpu()
elif user_choice == 'piedra' and cpu_choice == 'tijera':
    info()
    usuario()
elif user_choice == 'papel' and cpu_choice == 'piedra':
    info()
    usuario()
elif user_choice == 'papel' and cpu_choice == 'tijera':
    info()
    cpu()
elif user_choice == 'tijera' and cpu_choice == 'piedra':
    info()
    cpu()
elif user_choice == 'tijera' and cpu_choice == 'papel':
    info()
    usuario()