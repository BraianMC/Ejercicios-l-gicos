# /*
#  * Crea una función que sume 2 números y retorne su resultado pasados
#  * unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que
#  *   debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#  *   asíncrona, es decir, sin detener la ejecución del programa principal.
#  *   Se podría ejecutar varias veces al mismo tiempo.
#  */
import asyncio
         
async def asynchronous_sum(num_1, num_2, seconds):
    await asyncio.sleep(seconds)
    result = num_1 + num_2
    return result


async def sum_of_numbres(number_1, number_2, seconds):
    print("Sumando ", number_1," y ", number_2)
    result = await asynchronous_sum(number_1, number_2, seconds)
    return result

async def main():
    result = await sum_of_numbres(4, 4, 10)
    print(result)

asyncio.run(main())