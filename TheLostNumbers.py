#  * Dado un array de enteros ordenado y sin repetidos,
#  * crea una función que calcule y retorne todos los que faltan entre
#  * el mayor y el menor.
#  * - Lanza un error si el array de entrada no es correcto.



def verify_Array():
    array = []
    while True:
        try:
            number = input("Ingrese un numero o fin para finalizar:")
            if number.lower() == 'fin':
                break
            num = int(number)
            if num in array:
                return None, "Error: El numero ya esta presente en el array."
            if array and num < array[-1]:
                return None, "Error: Los numeros no estan ordenados."
            array.append(num)
        except ValueError:
            return array, "Error: ingrese solo numeros enteros."
    return array, "Numeros ordenados correctamente."
    

def lost_numbers(array):
    if not array:
        return "No hay numeros en el array"
    
    min_num = min(array)
    max_num = max(array)

    numbers = ""
    for num in range(min_num + 1, max_num):
        if num not in array:
            numbers += str(num) + " "

    if not numbers:
        return "No faltan numeros entre el minimo y el maximo en el arreglo."
    else:
        return numbers





#Programa principal
array = []
array, msj = verify_Array()

if array is not None:
    print(msj)
    print("Array:", array)
    result = lost_numbers(array)
    print("Numeros perdidos:", result)
else:
    print(msj)
            


