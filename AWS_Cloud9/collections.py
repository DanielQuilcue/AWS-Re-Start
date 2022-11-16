"""
    List form Cloud9
"""
"""
    * Una lista una caracteristica de elementos ordenados 
    * Es mutable, puede variar su contenido
    * Admite elementos repetidos, de cualquier tipo de daros como elementos.
    * se declara como parentesis cuadrado ty su contenido se separa con comas.
    * puede estar vacias
"""
# En esta actividad, editará un script en Python para almacenar una colección de nombres de frutas o una lista.

print("Lista")

fruits = ["Apple", "Banana", "Cherry"]
print(type(fruits))
print(fruits)

# Accediendo al contenido de una lista por su posición
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Modificando una lista
fruits[2] = "Orange"
print(fruits)



"""
    sort
"""
# Ordena la lista

"""
    Tupla
    
    * Casi lo mismo que la Lista
    * Es inmutable
    * Se inicia con parentesis redondos separados los elementos por comas.
"""
# Una tupla es similar a una lista, pero no se puede cambiar. Un tipo de dato que no se puede cambiar después de su creación se conoce como 
# inmutable. Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([]).


print("Tupla")

fruitsTuplas = ("Apple", "Banana", "Cherry")

print(type(fruitsTuplas))
print(fruitsTuplas)

# Accesiendo a la tupla

print(fruitsTuplas[0])
print(fruitsTuplas[1])
print(fruitsTuplas[2])



"""
    Defincion de Diccionario
    
    * Un diccionario es una lista cuyas posiciones tienen nombres asignados (claves). Imagine que su lista muestra la fruta favorita de distintas personas.

"""
print("Diccionario")

myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saavi": "Banana",
    "Paulo": "Pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Accediendo al dicionario por nombre

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saavi"])
print(myFavoriteFruitDictionary["Paulo"])
