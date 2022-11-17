import re

# Cadena de caracteres
cadena = "ORIGIN \
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed \
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn \
//"

# Si encuentra una doncidencia la va eliminando 
cadena = re.sub("[A-Z,0-9\s\/]", "", cadena)
print(cadena)

# Se agrega la nueva cadena
nuevaCadena = cadena

# Emprime la cadena con el cierta logitud [end, find]
print(nuevaCadena[0:20])
