# * Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#  *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#  *   o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#  *   automáticamente.
# # 

def sort_list(array, order_type):
    n = len(array)
    
    if order_type == "asc":
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
    else:
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

    return array

#Menu principal---------------------------------------------------
numbers = []

#Carga de numeros
while True:
    n = input("Ingrese un numero o fin para finalizar:")
    if n == "fin":
        break
    else:
        numbers.append(n)

parameter = input("Ingrese asc o desc para ordenar los numeros:")
sorted_array = sort_list(parameter)
print("Array ordenado de forma ",parameter,":",sorted_array)