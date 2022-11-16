"""
    Loop from Cloud9
"""

# Loop for and lista

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    # Todo lo que vata en este bloque se va repetir.
    print(item)
    print(f"El elemento {item} es de tipo {type(item)}")