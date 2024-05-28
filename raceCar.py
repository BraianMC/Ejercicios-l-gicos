import time

# String inicial que representa el camino
camino = "🏁_________🚙"

# Mostrar el estado inicial del camino
print(camino)

# Iterar a través del camino en reversa
for i in range(len(camino) - 1, 0, -1):
    # Esperar un poco para simular el avance
    time.sleep(1)
    if camino[i-1] == "🌲":
        print(nuevo_camino[:i-1] + "💥" + "_"* (len(camino) - i - 1))
        break
    else:
    # Crear una nueva cadena con el auto moviéndose
        nuevo_camino = camino[:i-1]+ "🚙" + "_" * (len(camino) - i - 1)  # Imprimir el nuevo estado del camino
        print(nuevo_camino)
