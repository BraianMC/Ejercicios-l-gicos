#   Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.

def create_dictionary_letters():
    letter_values = {}

    #Asignar valores tanto a las letras minusculas como mayusculas
    for i in range(26):
        capital_letter = chr(ord('A') + i)
        lowercase_letter = chr(ord('a') + i)
        letter_values[capital_letter] = letter_values[lowercase_letter] = i + 1
    
    return letter_values


def calculate_word_value(word, dictionary_letters):
    
    word_value = 0

    for letter in word:
        letter_value = dictionary_letters[letter]
        word_value += letter_value 
    

    return word_value



#Principal
dictionary_letters = create_dictionary_letters()

total_amount = 0

while True:
    word = input("Ingrese una palabra:")
    total_amount = calculate_word_value(word, dictionary_letters)
    if total_amount == 100:
        print("La suma de las letras de la palabra "+word+" suma 100 puntos.")
        break
    else:
        print("La suma de las letras de la palabra no suma 100.")
        total_amount = 0
        break


