"""
    Ejercicios basicos
"""

 # Preguntar al usuario cuantos años tiene y según ello decirle si puede entrar
 # a la zona del bar, el restaurante o la zona de juegos para niños.
 
usuarioEdad = int (input("Cuantos años tienes: "))
 
if usuarioEdad >= 18:
    print("Bienvenido a la zona de bar")
elif usuarioEdad <= 9:
    print("Diriguete a la zona de juegos para niños")
else:
    print("Puedes entrar a cualquir parte del restaurante")
    
# Vamos a poner los números en una lista
numeros = []

# Le agregamos 3 números
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# Asumir que el mayor es el primero de la lista
mayor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero > mayor:
        mayor = numero
# Imprimir el resultado
print("Mayor:", mayor)