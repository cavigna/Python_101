# En Python se pueden hacer todas las operaciónes artimeticas, como suma, resta, multiplicación, división
#potencias y raices.

from cmath import sqrt


n1 = 20
n2 = 22

suma = n1 + n2 
resta = n1 -n2
multiplicación = n1*n2
division = n1 / n2 
potencia = n1 ** n2
raiz = sqrt(n1)


print(suma)
print(resta)
print(multiplicación)
print(division)
print(potencia)
print(raiz)

# También se pueden hacer operaciones encadenadas. Siguiendo las reglas aritméticas

operacion_normal = 55 * 23 + 66

print(f'operación normal: {operacion_normal}')

operación_encadenada = 55 * (23 + 66)

print(f'operación encadenada: {operación_encadenada}')


## Hay dos conceptos que no usamos mucho en la Matemáticas del día a día, pero son muy útiles en la programación.
# Uno es la división entera. y el otro es el módulo.

# División Entera: La división entera, devuelve el número real entera más proxima al resultado. Esto se hace con //
# Por ejemplo 3 dividido 2 es 1,5, pero con la división entera el resultado es 1, es el número entero más próximo.

div_entera = 3 // 2
div_flotante = 3 / 2

print(f'division entera 3 //2: {div_entera}')
print(f'division flotante 3 /2: {div_flotante}')

#Módulo: El módulo es el resto de una división. se utiliza el simbolo del prcentaje

este_es_un_modulo = 3 % 2
print(f'módulo de 3 %2 = {este_es_un_modulo}')
print(f'módulo de 3 %3 = {3%3}')

