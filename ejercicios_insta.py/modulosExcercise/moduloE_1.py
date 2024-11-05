'''
Devolver numeros random
'''

import random 

def numberRand():
    number_random = random.randint(1,1000000)
    print(f"El numero ramndom generado es: {number_random}")

numberRand()