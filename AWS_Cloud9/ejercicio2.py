"""v3. Un usuario ingresará un número n (entero), quiere que se impriman los números pares del 0 hasta incluir ese número n

input: 10
output: 
0
2
4
6
8
10
"""


number = int(input("Ingresar un número: "))

for i in range(0, number+1, 2):
    print(i)