# For para seleccionar las opciones
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    print()
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


# Leer opciones
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


# Ejecutar las opciones dependiendo de la posición
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

# Generando el menú dependiendo de opciones y salida de opción
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        print()
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

# Función para general menú
def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Opción 4', accion4),
        '5': ('Opción 5', accion5),
        '6': ('Opción 6', accion6),
        '7': ('Salir', salir)
    }
    generar_menu(opciones, '7')

# Opciones de menú
""" Problema 1
    Se necesita un programa que le permita a un usuario dada su edad actual conocer su edad en el
    año 2070. Diseñe un algoritmo que satisfaga este requerimiento e impleméntelo en Python.
"""
def accion1():
    print()
    edadAltual = int(input("Ingresa su edad actual: "))
    edadfutura = 70
    resultadoEdad = edadAltual + edadfutura
    print(f"Su edad en 70 años sera de: {resultadoEdad} años")

""" Problema 2
    Se necesita un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por
    una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido para
    mostrar el consumo de combustible por kilómetro.
"""       
def accion2():
    print()
    kilometrosRecorridos = float(input("Ingrese los kilómetros recorridos: "))
    litrosGastados = float(input("Litros de combustibles gastados: "))
    consumoKilometros = kilometrosRecorridos / litrosGastados
    print(f"El consumo por kilómetros es de: {consumoKilometros} K")

""" Problema 3
    Se necesita un programa que solicite al usuario el ingreso de una temperatura en escala
    Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius.
"""
def accion3():
    print()
    temperaturaF = float(input("Temperatura en Fahrenheit: "))
    conversionCelsius = (5/9) * (temperaturaF - 32)
    print(f"Temperatura en Celsius es: {conversionCelsius} °C")

""" Problema 4 
    Se necesita un programa que calcule el precio final de un producto que cuenta con el 15% de
    descuento.
"""
def accion4():
    print()
    precio = float(input("Ingrese el valor del producto: "))
    descuento = 15 / 100
    precioTotal =  precio * descuento
    print(f"El precio del producto es: ${precioTotal} con un 15% de descuento")


""" Problema 5
    Desarrollar un programa que muestre los primeros 10 números de la sucesión de
    Fibonacci.
"""
def accion5():
    print()
    fibonacciN = int(input("Sucesión de números: "))

    # Dos primeros términos
    n1, n2 = 0, 1
    count = 0

    # Confirma si el numero es valido
    if fibonacciN <= 0:
        print("Por favor, ingresar un número entero positivo ")
    #Si solo existe un término, devulve n1
    elif fibonacciN == 1:
        print("Secuencia de Fibonnaci hasta" , fibonacciN ,  ":")
        print(n1)
    
    # Genera la secuencia de Fibonacci
    else:
        print("Secuencia de Fibonacci")
        print()
        while count < fibonacciN:
            print(n1)
            update = n1 + n2
            # Actualizando los valores
            n1 = n2
            n2 = update
            count += 1
"""
    Problema 6
Tenemos guardado en un diccionario los códigos morse correspondientes a cada carácter.
Escribir un programa que lea una palabra y la muestre usando el código morse.

Input: Hola
Output: .... --- .-.. .-
"""
def accion6():

    # Diccionario 
    dicionario = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----',
        '.': '.-.-.-', ',': '--..--', ':': '---...',
        ';': '-.-.-.', '?': '..--..', '!': '-.-.--',
        '"': '.-..-.', "'": '.----.', '+': '.-.-.',
        '-': '-....-', '/': '-..-.', '=': '-...-',
        '_': '..--.-', '$': '...-..-', '@': '.--.-.',
        '&': '.-...', '(': '-.--.', ')': '-.--.-'
    }

    palabras = input(" Ingrese una palabra o texto: ")
    palabraMorce = ""

    for i in palabras:
        if i != " " and i.upper() in dicionario:
            palabraMorce += dicionario[i.upper()]
        else:
            palabraMorce += i
    print(f" El texto codificado es: {palabraMorce}")
    
# Función para salir de menú
def salir():
    print('Saliendo..')

# Función main
if __name__ == '__main__': 
    menu_principal()