#Una variable es un contenedor de información. Como su nombre la define, es variable,
#implicando la mutablidad de la misma. La buena y mala noticia, es que en Python solo existen
#variables. No Hay constantes. Otros lenguajes como Kotlin se define una constante con el
#identificador val.

#Siempre se define una variable con un nombre que debe empezar con una letra, todo en minuscula, 
#los espacios deben ser llenados con _ y al final debe tener un =. A la izquierda va el nombre
# y seguido del igual su valor

variable_demostracion = "demostración"
# nombre_en_minuscula = valor


## Otro punto importante a destacar, es que una variable en Python puede ser de cualquier tipo de
# dato, es decir puedo definir una con un número pero en otra linea la puedo asignar a una String

este_es_un_numero = 42
este_es_otro_numero = 21

esta_es_una_palabra = "palabra"

print(f'esto es un número: {este_es_un_numero}') #42
print(f'esto es un palabra: {esta_es_una_palabra}') #palabra


# Como son variables y se pueden pisar, yo puedo asignar el valor de la palabra al número

esta_es_una_palabra = este_es_un_numero

print(f'esto es un número: {este_es_un_numero}') #42
print(f'esto es un palabra: {esta_es_una_palabra}')#42

#Lo que pasó fue que re escribí el valor de la palabra por el del número.

# nombre variable = valor
# este_es_un_numero = 21
este_es_un_numero = este_es_otro_numero

este_es_otro_numero = este_es_un_numero

print(este_es_un_numero)

print(este_es_otro_numero)

n1 = 42
n2 = 21

print(n1, n2)

n2 = n1

print(n1, n2)

n1 = n2
print(n1, n2)






