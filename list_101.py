# Podemos inicializar una lista vacia definiendo el nombre= []

import random


listado = []

#Si quremos agregar un elemento usamos la función append. Esta insertará el elemnto
# al final de la lista

print(f'listado vacio: {listado}')

listado.append("elemento agregado") 

print(listado)


# Podemos agregar varios elementos con un loop:

elementos_a_insertar = [16, 34, 23, 10, 26, 44, 48, 33, 74]

for i in elementos_a_insertar:
    listado.append(i)

print(listado)

# Se puede insertar un elemento en una posición determinada con insert
# list.insert(posición, elemento a insertar)

listado.insert(3, "nuevo elemento")

print(listado)

# Podemos eliminar algún elemento en función a su valor. 

listado.remove("elemento a borrar")

print(listado)

# Si deseamos eliminar un elemento según su posición usamos pop

listado.pop(3)
print(listado)

# Si queremos que mostrar los elementos en el orden inverso usamos revrse

ordenado = [i for i in range(1,11)] 
ordenado = [i for i in range(1,11)] 

print(f'listado en orden: {ordenado}')

ordenado.reverse()
print(f'listado en orden inverso: {ordenado.reverse()}')


#Si queremos saber el menor o elm mayor elemento usamos min o max

print(f'el menor elemento es: {min(ordenado)}')
print(f'el mayor elemento es: {max(ordenado)}')


# Se accede  a un elemnto por medio de su indice. Por ejemplo: 
#Imprimir el numero anterior de una lista 

for i in range(0, len(ordenado)+1):
    print(ordenado[i-1])


# Ejercicio: Remover elementos duplicados de una lista:

duplicados =[]