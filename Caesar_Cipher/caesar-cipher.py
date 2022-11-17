
"""
    Use of functions to implement a Caesar Cipher.
"""
# Funcion para difinir usuarios.    
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Función que definirá al usario un mensaje para cifrar.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Función para solicitar una clave de cifrado al usario.    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

"""
    This is a javadoc style.

    @param param1: menssage.
    @param param2: clave de cifrado.
    @param param3: alfabeto.
    @for: recorrer cada letra del mensaje.
    @para una letra específica, busca su posición.
    @si la letra actual está en el alfabeto, agregue la nueva lerra al mensaje cifrado.
    @si la letra actual no está en el alfabeto, añada la letra actual.
    @ Devuelva el mensaje cifrado tras agotar todas las letras del mensaje.
"""
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
# Desencripta la llave con -menos negativo dependiendo del valor puesto en la llave    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# Función main 
runCaesarCipherProgram()
