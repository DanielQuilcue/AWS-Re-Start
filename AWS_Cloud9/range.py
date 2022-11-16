# Range crea una secuencia de rango

# Función range con un solo argumento
# Rango va de u hasta el número dado (Sin alcanzar)

for i in range(10): # se imprime de 0 a 9, en su total mostrando unos 10 números.
    print(i)

# Rango se le puede pasar dos argumentos, donde inicia a donde acaba

for i in range(20, 25):
    print(i)
    
# Rango con 3 argumentos
# Rango del primer numero hasta el segundo, y el tercer numero es el alcanze o salto que hara enttre los dos numeros

for i in range(0, 20, 2):
    print(i)