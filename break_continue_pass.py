# break: Es una palabra clave que nos permite finalizar la ejecución de un bucle.
#Por ejemplo, si del 1 al 100 buscamos el número 8, una vez encontrado no es 
#necesario que siga con el bucle hasta el 100 para ello usamos el breake

rango = range(1, 101)

for i in rango:
    if i == 8: 
        print(f'Se encontró el número 8')
    else:
        print("Buscando....")

# Esto hara que imprima 99 veces buscando y una se encontró el 8. Lo lógico, es que
# una vez encontrado el número detengamos la ejecución con el break
print()
print()
print()
print("Usando el break.....")
for i in rango:
    if i == 8: 
        print(f'Se encontró el número 8')
        break
    else:
        print("Buscando....")


# Continue: Si se cumple la condición, ese bloque no se ejecuta y se continua a la 
# siguiente iteración:

print()
print()
print()
print("Usando el continue.....")

for i in [1,2,3,4,5,6]:
    if i == 5:
        continue
    else:
        print(i)

# PASS. Probablemente una de las mejores herramientas que podés usar.
# Pass significa pasar, se usa habitualmente cuando estas definiendo una función o
# una estructura de control, pero todavía no decidiste la lógica. Esto te permite
#desarrollar sin necesidad de implementar código para esa sección

print()
print()
print()
print("Usando el pass.....")

for i in [1,2,3,4,5,6]:
    if i != 5:
        pass # si i es distinto a 5 NO HAGAS NADA.
    else:
        print(i) #imprimime el 5


