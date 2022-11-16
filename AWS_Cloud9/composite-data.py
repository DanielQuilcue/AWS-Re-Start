"""
    librerias 
"""
import csv # Modulo para trabajar archivos csv
import copy # Modulo para sacar una copia de cierta coleccion.

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

print(myVehicle)

# Forma para msotrar solo llaves ys sus valores

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
myInventoryList = [] # Declaramos una lista

# Manejo de archivos, csv

#With open (incluir la ruta / noimbre del archivo)
# Por defecto tiene un modulo de lectura (R)
# Modos de lectura (R), escritura (w), edicion (a) (append)

with open("car_fleet.csv") as csvFile:
    csvReader = csv.reader(csvFile)
    lineCount = 0
    
    for row in csvReader: # Separar las lineas por por filas
        if lineCount == 0:
            # Metodo  .jon() es de str para convertir la lista en string
            # Entre comillas se coloca el separador que se quiere
            print(f"LE nombre de las colimnas son_ {', '.join(row)}")
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            currentVehicle = copy.deepcopy(myVehicle) # Una copia exacta desvinculada del diccionario original
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            myInventoryList.append(currentVehicle) # Agregar el vehiculo actual a la lista de inventario
            
            lineCount += 1 # Para saber cuantas filas hemos tratado
    print(f"se contaron {lineCount} lineas")
    
    print()
    
    # Forma de imprimir los elementos de la lista con su valores ordenados
    # For anidades
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print(f"{key} : {value}")
            print("-"*40)
        print()
            
