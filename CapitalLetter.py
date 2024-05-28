#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.

def convert_to_uppercase(words):
    
    result = ""
    for i in range(len(words)):
        
        if i == 0 or words[i-1] == " ":
            result += chr(ord(words[i]) - 32)
        else:
            result += words[i]
    
    return result 


#Main
words = input("Ingrese una oracion:")
result = convert_to_uppercase(words)
print("Resultado: ",result)