# Una lista es un conjunto de elementos que estan agrupados dentro de un contenedor
# denominado list. Siempre se definen con corchetes[].
#Dentro de la misma podemos tener números, palabras, booleans.

#Al ser un conjunto de elementos, estos poseen una posición para ubicarlos, llamado
#indice
#Por ejemplo

listado = ["uganda", 23, "convento", False]
# Indices    0       1    2          3

print(type(listado))
# Con el indice podemos ubicar y extraer la información basado en su posición.
# Para acceder a un elemento ponemos el nombre de la lista junto a corchetes y su,
#ubicación

print(listado[2])

#for 



for i in listado:
    if i == False:
        print("False")
    else:
        print("No es falso")