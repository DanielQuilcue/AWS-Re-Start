# Python 3.10.8
# UTF-8

# By Daniel Quilcue

# Import modulos
import subprocess

# Rutas de creación de archivo txt
# Con estas opciones captura el stdout del comando
ruta = subprocess.run(["pwd"], captureoutput=True,text=True) 
ruta = ruta.stdout

# El stdout incluye "\n" al final, por eso hay que recortarlo
ruta = ruta[0:(len(ruta)-1)] 

# Guarda los numeros em .txt
def saveNumberFile(currentNumber):
    with open(ruta + "/results.txt", "a+") as results:
        results.write(str(currentNumber) + "\n")

# Condición para validar que numero es primo
def numbercondition(number):
    currentDivisorNumber = number - 1
    while currentDivisorNumber >= 2:
        if number % currentDivisorNumber == 0:
            return False
        currentDivisorNumber -= 1
    return True

# Validad hasta la cantidad dada si es primo
def primeNumbers(quantity):
    currentNumber = 2
    while currentNumber <= quantity:
        if numbercondition(currentNumber):
            saveNumberFile(currentNumber)
        currentNumber += 1

# Cantidad de números que recorrera la función primeNumbers
primeNumbers(250)
