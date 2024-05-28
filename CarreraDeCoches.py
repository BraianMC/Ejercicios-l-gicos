# /*
#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  * 
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  */

import random

def create_race_track(track_length):
    created_track = "🏁"

    for i in range(track_length):
        created_track += "_" 

    return created_track


def assign_trees(race_track, numbers_of_trees):
    print("Asignando arboles aleatoriamente!")
    trck_length = len(race_track)-1
    # print("longitud de la pista a poner arboles:", trck_length-1)
    trees_positions = []

    #Debo ver el tema de que no se repita la posicion de los arboles
    for i in range(numbers_of_trees):
        random_position = random.randint(1, trck_length)
        #En el caso de que la posicion del arbol ya se encuentre en el array
        while random_position in trees_positions:
            random_position = random.randint(1, trck_length)
        trees_positions.append(random_position)
    
    return trees_positions


def car_race(race_track, trees_positions):
    
    lost_green_turn = False
    lost_red_turn = False
    green_car_win = False
    red_car_win = False
    green_car_position = len(race_track)
    red_car_position = len(race_track)
    print("posicion inicial del auto:", green_car_position)
    turn = 0
    green_turn = 50
    red_turn = 50

    while True:
        print("Ronda: ", turn)
        track_leng = len(race_track)
        print("longitud pista:", track_leng)

        if not lost_green_turn:
            if turn == 0:
                print("Pista de carrera:", race_track)
            else:
                print("Pista de carrera:", green_track)

            green_car_steps = int(input("🟩 Turno verde - Ingrese la cantidad de pasos a avanzar:"))
            next_pos = green_car_position - green_car_steps

            #!Falta agregar una funcion o codigo para verificar que la cantidad de pasos no sean mas de 3
            #!Falta verificar que la cantidad de pasos no exceda los que le quedan por dar 
            #!Osea que si le quedan 2 pasos para la meta no ponga 3 pasos
            if next_pos < 0:
                next_pos = 0  # Evita exceder la pista

            new_track = list(race_track)
            if green_car_steps > 1:
                if turn == 0:
                    green_car_position -= 1
                new_track[green_car_position] = "_"  # Limpia la posición actual
                
            if next_pos in trees_positions:
                new_track[next_pos] = "💥"
                lost_green_turn = True
                green_turn = turn
                print("❌ El auto verde pierde un turno ❌")
            else:
                new_track[next_pos] = "🚙"
                if next_pos == 0:
                    green_car_win = True #Indico que gano pero si el auto rojo esta igual entonces empate

            green_car_position = next_pos  # Actualiza la posición del auto
            green_track = "".join(new_track)
            print("Pista verde actualizada:", green_track)


        #Recorrido del auto rojo
        if not lost_red_turn:
            if turn == 0:
                print("Pista de carrera:", race_track)
            else:
                print("Pista de carrera:", red_track)

            red_car_steps = int(input("🟥 Turno rojo - Ingrese la cantidad de pasos a dar:"))
            next_pos_red = red_car_position - red_car_steps
            new_track_red = list(race_track)

            if red_car_steps > 1:
                if turn == 0:
                    red_car_position -= 1
                new_track_red[red_car_position] = "_"  # Limpia la posición actual
            
            if next_pos_red in trees_positions:
                new_track_red[next_pos_red] = "💥"
                lost_red_turn = True
                red_turn = turn
                print(" ❌ El auto rojo pierde un turno ❌")
            else:
                new_track_red[next_pos_red] = "🚗"
                if next_pos_red == 0:
                    red_car_win = True #Indico que gano pero si el auto rojo esta igual entonces empate

            red_car_position = next_pos_red  # Actualiza la posición del auto
            red_track = "".join(new_track_red)
            print("Pista roja actualizada:", red_track)
            
       
        #* Verficio si perdieron el turno para habilitarlos
        #! Falta revisar este codigo porque puede que se este pasando de largo algo
        if lost_green_turn or lost_red_turn:
            print("ingreso para verifica si perdio un turno")
            print("Valor del turno:", turn)
            print("Valor del turno verde:", green_turn)
            if turn > green_turn:
                lost_green_turn = False
                print("Habilito el turno verde..")

            if turn > red_turn:
                lost_red_turn = False
                print("Habilito el turno rojo...")

        #* Verifico si alguien gano o ambos sino incremento la siguiente ronda
        if red_car_win or green_car_win:
            if red_car_win and not green_car_win:
                print("🏆 El auto rojo gano!!!!!")
            elif green_car_win and not red_car_win:
                print("🏆 El auto verde gano!!!!")
            else:
                print("🤝 Empate!!!!!")
            break
        else:
            turn += 1
        
        

#* Menu principal
track_length = int(input("Ingrese la longitud de la pista de carrera:"))

race_track = create_race_track(track_length)

print("Pista de carrera:", race_track)
numbers_of_trees = 2
trees_positions = []
trees_positions = assign_trees(race_track, numbers_of_trees)

print("Posiciones de los arboles en la pista:")
print(trees_positions)
car_race(race_track, trees_positions)



# print("Posicionamiento de los autos...!")
#         print(red_track)
#         print(green_track)

#Observaciones: los arboles no se mostraran para que los usuarios no sepan cuantos pasos tiene que dar.

#Tendria que tener un metodo que me cree la pista (listo) 
#Luego otro metodo donde me agregue los arboles de forma aleatoria en la pista tambien me tendra que 
#retornar las posiciones donde se encuentran los arboles para que al ultimo muestra la pista con los arboles
#Luego el ultimo metodo donde se realiza la carrera donde coloco los autos en las pistas
#Haria una copia de la pista y pondria los autos en sus posiciones e ire mostrando como avanzan
#Debo cambiar el arbol por el caracter 💥 y pierde el turno
#Debo ver como hacer para que cuando pierda el turno como sigue el auto en el siguiente turno

# ! Tengo el error de que la cantidad de pasos que le indico no se si deberia restarle -1 o no
# ! La variable new_track en el if primero ingresa en el primer bloque de codigo donde no cree la variable
# ! entonces por eso tira error.
# ! Revisar la forma de avanzar porque puede que este haciendolo mal porque la cantidad de pasos si me guio 
# ! con el indice no seria buena idea. 
# ! Al indicar la cantidad de pasos me esta posicionando mal osea supongamos que la cantidad de pasos es 3
# ! entonces se posiciona en la posicion 2 y de ahi va avanzando pero para abajo y eso no deberia pasar
# ! deberia avanzar desde el final y los pasos la cantidad que se indique 
# ! Revisar lo del turno perdido porque en el caso de que ninguno pierda turno me tiraria error porque 
# ! las variables del turno no estarian inicializadas y lo mejor seria poner un if para verifica si perdieron el turno