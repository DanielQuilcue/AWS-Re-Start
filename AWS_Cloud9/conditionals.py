"""
    Condicional from Cloud9
"""

lloviendo = False

if lloviendo == False:
    print("Esta llaviendo")
    
#Ayudas de las comparaciones

print(lloviendo != True)
print(not lloviendo == True)

# And: las dos comparaciones son verdaderas = True pero si una es falsa = Falsa

hayRopa = False

print(lloviendo == True  and hayRopa == True)

# Or: al menos un de las comparaciones debe ser verdadera = True, si las dos son falsas  = False

print(lloviendo == True or hayRopa == True)

"""
    IF
"""

if lloviendo and hayRopa: # Equivalente a estar lloviendo a == True and ropa == True
    print("Entra la ropa")
elif lloviendo and not hayRopa:
    print("Esta como lloviendo no?")
elif hayRopa:
    print("Revisa que nada se haya caido")
else:
    print("No pasa nada, sigue en lo tuyo campeon")
    

userReply = input("¿Sumercé, necesita enviar un paquete? (Sobre, Caja o Bolsa): ")

if userReply == "Sobre":
    print("Con gusto, recuerda que el sobre debe estar en perfecto estado")
elif userReply == "Caja":
    print("Recuerda que va deacuerdo al peso")
elif userReply == "Bolsa":
    print("Revisar que la bolsa que este en perfecto en estado")
else:
    print("El paquete no es valido")
    