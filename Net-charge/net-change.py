"""
    Calculation of net insulin load using Python lists and loops
"""

# Asignación de variables, listas y diccionarios
# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# Diccionario nuevo 
# Para rellenar el diccionario con pares de clave-valor, inserte la primera clave
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# Ahora que tiene la base para identificar una sola entidad, puede utilizar este método para buscar todas las entidades de una lista
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Utilizará la variable netCharge proporcionada en una fórmula de carga neta basada
pH = 0
while(pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

# imprimir la variable netCharge con el pH, utilice una cadena de formato a fin de mejorar la legibilidad
print('{0:.2f}'.format(pH), netCharge)
pH += 1
