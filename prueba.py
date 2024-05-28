palabra = "Python"  # Ejemplo de palabra de 5 letras
cantidad = int(input("Ingrese la cantidad de caracteres desde el final: "))

# Verificar si la cantidad ingresada es válida
if cantidad > len(palabra):
    print("La cantidad ingresada es mayor que la longitud de la palabra.")
else:
    print(f"Los últimos {cantidad} caracteres son:")
    for i in range(1, cantidad + 1):
        print(palabra[-i])