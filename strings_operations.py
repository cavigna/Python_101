

#Para saber la cantidad de letras de una palabra podemos aplicar la función len()

palabra = "arquitectura"

cantidad_letras_arquitectura = len(palabra)

print(f'arquitectura tiene {cantidad_letras_arquitectura} letras')

# Si quiseramos saber la cantidad de veces que aparece una letra determinada en 
# una string podemos utilizar la función count.
cantidad_de_t = palabra.count("t")
print(f'la letra t se repite {cantidad_de_t} veces')

#Si queremos convertir toda la palabra en mayuscula podemos usar upper
print(palabra.upper())

#La primera en mayúscula:
print(palabra.capitalize())

#Las cadenas de caracteres en Python son interpretadas como listas de letras. Por ende,
#podemos aplicar todas las funciones propias de un listado como también aquellas
#inherentes a una palabra:

# si queremos acceder a la primera letra de una palabra podemos hacerlo como si fuera
#una lista. 
print(palabra[0])

# Las primeras 3
print(palabra[0:3])

# En el caso inverso, si queremos saber la ubicación de un letra, podemos hacer
# usar index
print(palabra.index("a"))

#Hasta ahora vimos solamente como una palabra se separa en letras. Pero si quisieramos
#Separar un frase en palabras usamos split

frase = "Un conjunto de letras conforman una palabra"

frase_separada_en_palabras = frase.split()

print(frase_separada_en_palabras)

#Esto nos permite ver cada una de las palabras, y realizar acciones en las mismas.


#Ejercicio: Dada la frase, contar la cantidad de palabras que son menores o iguales
#a 3.