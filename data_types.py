## Vamos a usar el comando print para ver en la terminal los resultados.

## Existen los siguientes tipos de datos en Python

# Número ==> Entero o Flotante(con coma)

numero_entero = 42

numero_flotante = 0.23

print(" ")
print("*** Números ***")
print(type(numero_entero)) #<class 'int'>
print(type(numero_flotante)) #<class 'float'>
print(" ")


#Caracteres y cadena de caracteres. En Python no existe una clase para los caracteres, sino que posee una única clase para la cadena de carácteres llamda str. Str
# viene de String. Podemos entenderlo como una palabra o una letra. 
# Para definir una STRING siempre se debe comenzar con comillas simples (') y/o dobles. ("") y terminar de la misma manera.

este_es_un_caracter = 'a'
esta_es_una_palabra = "Una palabra"

print(" ")
print("*** Palabras ***")
print(type(este_es_un_caracter)) #<class 'str'>
print(type(esta_es_una_palabra)) # <class 'str'>
print(" ")


# Booleans. Este tipo de dato tiene dos estados posibles: Verdadero o Falso.

esto_es_falso = False #<class 'bool'>

esto_es_verdadero = True #<class 'bool'>

print(" ")
print("*** Booleans ***")
print(type(esto_es_falso))
print(type(esto_es_verdadero))
print(" ")

