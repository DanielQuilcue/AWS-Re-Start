# Abriendo archivo txt y darle permiso rt
cadena = open("preproinsulin-seq-clean.txt", "rt")

# Abrriendo archivo con permiso de wt
linsulin = open("linsulin-seq-clean.txt","wt")
binsulin = open("binsulin-seq-clean.txt","wt")
cinsulin = open("cinsulin-seq-clean.txt","wt")
ainsulin = open("ainsulin-seq-clean.txt","wt")

# Función para abrir archivo
with open("preproinsulin-seq-clean.txt", "rt") as lectura:
    # Leyendo cadena
    cadena = lectura.read()
    print(cadena)

    # Formateando la cadena y cortando con []
    print("logintud cadena 1: {}".format(len(cadena[0:24])))
    print("logintud cadena 2: {}".format(len(cadena[24:54])))
    print("logintud cadena 3: {}".format(len(cadena[54:89])))
    print("logintud cadena 4: {}".format(len(cadena[89:110])))

    # Agregando la cadena al archivo con el corte []
    linsulin.write(cadena[0:24])
    binsulin.write(cadena[24:54])
    cinsulin.write(cadena[54:89])
    ainsulin.write(cadena[89:110])
    
# Cerrando los archivos modificados
linsulin.close()
binsulin.close()
cinsulin.close()
ainsulin.close()