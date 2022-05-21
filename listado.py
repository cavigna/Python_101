

listado_numero = range(1, 100) # 1,2,3...100

for numero in range(1,101):
    if numero == 50:
        print("Llegamos al 50")

    elif numero<= 10:
        print("estamos en la primera decena")

    elif numero>=10 and numero<50:
        print("este numero es mayor a 10")

    else:
        print("este numero es mayor a 50")





rango_numeros = range(1,101)

#for numero in rango_numeros:
    #if numero % 2 == 0:
        #print(f'El número {numero}: Es Par')

    #else:
        #print(f'El número {numero}: Es Impar')


#Liistado de palabras. Check si la plabra es mayor a 5 letras.

listado_palabras = ["mouse", "jarron", "auto", "pileta", "auto"]

p = "mesa"

for palabra in listado_palabras:
    if len(palabra)>= 5:
        print(f'{palabra} tiene más 5 letras o más')







    