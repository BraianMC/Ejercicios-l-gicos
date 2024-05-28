
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

def isAnagram(word_1, word_2):
    #Vuelve las mayusculas a minusculas
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    #Ordeno la letras de cada palabra y comparo para decidir si son anagramas
    return sorted(word_1) == sorted(word_2)



#Programa principal
wrd_1 = input("Ingrese la primer palabra:")
wrd_2 = input("Ingrese la segunda palabra:")

if isAnagram(wrd_1, wrd_2):
    print("Las palabras ",wrd_1," y ",wrd_2," son anagramas!")
else:
    print("No son anagramas las palabras ",wrd_1," y ",wrd_2,)

