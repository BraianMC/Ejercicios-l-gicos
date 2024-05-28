# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

def balanced(string_1, string_2):
    out_1 = ""
    out_2 = ""

    for lt in string_1:
        if  lt not in string_2:
            out_1 += lt

    for lt in string_2:
        if lt not in string_1:
            out_2 += lt
    
    print("Cadena 1: ", out_1)
    print("Cadena_2: ",out_2) 


def validate_string(word):
    while not word:
        word = input("No ingreso nada. Por favor ingrese una palabra:")
    return word



#Programa principal

string_1 = validate_string(input("Ingrese una palabra:"))

string_2 = validate_string(input("Ingrese una segunda palabra:"))

balanced(string_1, string_2)