"""
Las funciones son una de las herramientas indispensables a la hora de programar.
Nos permiten automatizar tareas, modularizar el código, evitar repeticiones y hacerlo
reusable.
Podemos pensar en ellas como pequeños porgramas que tienen como objetivo realizar 
una tarea determinada.
"""

"""
Una función siempre se define con la palabra clave def seguido del nombre de la función
en minúsculas, parentesis y dos puntos. Finalmente debe tener un return. 
El return, es el valor que nos dará la función una vez que sea ejecutada.
Dentro de los parentesis, van los argumentos. Estos son los componentes que precisa
una función para cumplir su cometido

"""

"""
Pongamos el siguiente ejemplo. Si necistamos el porcentaje de un  número, probablemente
en muchas líneas estaremos repitiendo la misma formula = (numero * porcentaje)/100.
Para eso viene la vieja y confiable..., función. Para calcular un porcentaje necesitamos
dos elementos (argumentos):
   * El número
   * El porcentaje

Finalmente necesitamos que nos devuelva (return) el procentaje.
"""

def porcentaje(numero:int, porcentaje:float): 
    resultado = (numero * porcentaje)/100
    return resultado

print(porcentaje(90, 5))


"""
Ejemplo: Constantemente queremos saber cual es la posición (indice) de
"""

def fizzBuzz(first_n:int, last_n:int):
    for i in range(first_n, last_n):
        if (i %3 == 0) and (i % 5 == 0):
             print("FizzBuzz")
        elif i % 3 == 0:
             print("Fizz")
        elif i % 5 == 0:
             print("Buzz")

        else:
            print(i)


def only_divisible_by_3(first_n:int, last_n:int):
    resultado = []
    for i in range(first_n, last_n):
        if i % 3== 0:
            resultado.append(i)

    return resultado


fizzBuzz(1, 30)

print(only_divisible_by_3(1,30))