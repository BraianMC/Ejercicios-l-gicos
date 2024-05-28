
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en


word_for_morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',
    'd': '-..',   'e': '.',     'f': '..-.',
    'g': '--.',   'h': '....',  'i': '..',
    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',
    's': '...',   't': '-',     'u': '..-',
    'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..'
}

morse_for_word = {
    '.-': 'a', '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i',
    '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u',
    '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z'
}

def morse_to_text(word):
    text = ""
    for letter in word:
        if letter in morse_for_word:
            text += morse_for_word[letter] + "  " 
    text = text.rstrip()

    return text


def text_to_morse(word):
    text = ""
    for letter in word:
        if letter in word_for_morse:
            text += word_for_morse[letter] + "  "
    text = text.rstrip()

    return text


def is_morse_word(word):
    return word[0] in word_for_morse



#El usuario ingresa la palabra
while True:
    word = input('Ingrese una palabra ya sea en codigo morse o normal:')
    if len(word) == 0:
        print('No ingreso ninguna palabra todavia....')
    else:
        break


#Determino si la palabra esta en morse o no
result = is_morse_word(word)


#En funcion del resultado lo convierto en morse o no
if not result:
    print('La palabra ingresada por el usuario ',word,' es morse..')
    text = morse_to_text(word)
    print('Palabra en codigo morse traducida a texto: ', text)
else:
    print('La palabra ingresada por el usuario ', word, 'es texto..')
    morse_word = text_to_morse(word)
    print('Palabra convertida en codigo morse:' , morse_word)
