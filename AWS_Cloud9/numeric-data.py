"""
 Python has three numeric types: int, float, and complex
"""

#!/usr/bin/env python3
"""
    Darle permisos con chmod +x "Name.file", despues se ejecuta como un script de bash.
"""

print("Hello, world")

""" 
    Varibles
"""
    #type, para verificar tipo de datos.

number = 5
print(type(number))
print(number)


# se pueden concatenar dos textos o variables con +
# cuando se habla de números imaginarios

print("Hola "+"tú")

""" 
    Formato formato
"""

precio = 2500
unidades = 5

print("Hola, el precio es {}".format(precio))
print(f"Hola. el precio de {unidades} piezas {precio} pesos")

"""
    Bool o booleano son True o False = 1 o 0
"""

isDaniel = True

print(isDaniel == 0)

"""
    Dats flot
    
"""
# En tipo de datos solo se almacenas tipos de datos enteros, si se almacena un tipo
# de datos decimal, pasa automaticamente a datos flotante

print("Python has three numeric types: int, float, and complex")

myValue = 3.14

print(type(myValue))
print(myValue)

print(str(myValue) + " is of the data type " + str(type(myValue)))


""" 
    Dats imagine
"""
#En la matemática avanzada, un número imaginario es un número complejo, el cual se puede escribir como un número 
#real que se multiplica por la unidad imaginaria i. El tipo de dato complejo es complicado porque tiene que representar una 
#letra y un número, como 5j.


print("Python has three numeric types: int, float, and complex")

myValueI = 5j

print(type(myValueI))
print(myValueI)
print(str(myValueI) + " is of the data type " + str(type(myValueI)))

"""
    Dats boleanos
"""

print("Python has three numeric types: int, float, and complex")

myValueB = True

print(type(myValueB))
print(myValueB)
print(str(myValueB) + " is of the data type " + str(type(myValueB)))

# Boleano False

myValueF = False

print(type(myValueF))
print(myValueF)
print(str(myValueF) + " is of the data type " + str(type(myValueF)))


