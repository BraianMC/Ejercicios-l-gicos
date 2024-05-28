# /*
#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas
#  *   de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#  */

machine_products = {}
product_prices = {}
allowed_coins = [5, 10, 50, 100, 200]

def load_products():
    for i in range(4):
        name_product = input("Ingrese el nombre del producto:")
        machine_products[i] = name_product
        

def get_product(product_code, money):
    #Primero busco el producto
    if product_code not in machine_products:
        print("No existe el producto..")
        return money
    else:
        #Simulario que seleccina el producto
        product = machine_products[product_code]
        product_name = product['name']
        product_price = product['price']

        if all(coin in allowed_coins for coin in money):
            #calculo el precio
            print("Producto seleccionado: ", product_name)
            print("Precio del producto: ",product_price)
            #sumo las monedas que me da el cliente
            client_money = sum(money)
             
            
            if client_money < product_price:
                print("El dinero ingresado es insuficiente..")
                return money
            elif client_money == product_price:
                print("Pagaste el precio exacto. No hay cambio")
                return []
            else:
                change = client_money - product_price
                coins_to_return = []

                while change > 0:
                    for coin in sorted(allowed_coins, reverse = True):
                        if change >= coin:
                            coins_to_return.append(coin)
                            change -= coin
                            break
                print("Cambio devuelto:", coins_to_return)
                return coins_to_return

            #mando mensaje que las ingresadas no estan permitidas 
            #devuelvo su dinero
        else:
            print("Alguna moneda ingresada no esta permitida.")
            return money
        

#Menu principal-----------------------------------------------------------------

#Cargo la maquina con los productos
load_products()

#Elijo un producto de la maquina
money = get_product(40, 500)
print("Dinero devuelto: ", money)