"""
    Loop Cloud9
"""

# Se usa para repetir un bloque de codigo hasta que una condición sea falsa.

#count = 10
#while count < 10:
#   print(count)

import random # Diblioteca para general numero randum

number = random.randint(1, 5)

isCorrect = False # Iniando variable

while isCorrect != True: # mientras que no advine se sigue preguntando.
    adivina = int(input("Ingresa un número: "))
    
    if number == adivina: # compara
        print("Felicitaciones compa, ganaste, maquina")
    else:
        print("Sigue intentando")
        
# reto hacer frio o caliente

