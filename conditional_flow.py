#En Python tenemos las siguientes estructuras de control:
# If - else - elif -  while


#If. Si la condición es verdadera se ejecutará el el contenido dentro del if. Por ejemplo

numero = 42
string = "hola"

if numero == 42:
    print("Se cumplió la condición")


# Else: Viene seguido de un If. Si la condición del if no se ciumple se ejecuta la el
# bloque del else:

if numero == 42 and string== "chau":
    print("Se cumplió la condición")
else:
    print("No se cumplió la condición")

# Elif: Else If. Es un else intermedio. Siempre el orden de una extructura condicional
# Comienza por el if, luego elif(o varios) y finalmente else.
numero = 9
if numero>42:
    print("Numero mayor a 42")
elif numero>10:
    print("Numero mayor a 10")
else:
    print("El numero es no es menor a 42 ni mayor a 10")


#While: La condición siempre se ejecutará mientras sea verdadera la premisa.
# IMPORTANTE: Si nunca se cumple la función el bucle se ejecutará eternamente. Siempre
#Se debe aplicar un mecanismo para evitar la ejecución infinita.

while numero >= 0:
    print(numero)
    numero -= 10 # numero = numero - 10






