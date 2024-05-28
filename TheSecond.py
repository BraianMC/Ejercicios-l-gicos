# * Dado un listado de números, encuentra el SEGUNDO más grande


def get_second(array):
    sorted_array = sorted(array)
    print(sorted_array)
    lgth = len(array)
    print(lgth)
    largest_number = sorted_array[lgth-2]

    return largest_number

#Main
numbers = []
while True:
    n = input("Ingrese un numero o fin para terminar:")
    if n.isdigit():
        numbers.append(int(n))
    else:
        if n == "fin":
            break
        else:
            print("No ingreso un numero!.")

second = get_second(numbers)
print("El segundo numero mas grande es: ",second)