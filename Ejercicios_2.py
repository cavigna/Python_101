# *********** Ejecicio 1 **************
# Borrar todos los números 31 de un listado


treinta_uno = [23, 31,6, 31, 95, 4, 31, 2, 33, 3, 31] 
# Expected : [23, 6, 95, 4, 2, 33, 3]


# *********** Ejecicio 2 **************
# Encontrar el valor máximo de un listado de numeros. NO USAR max()
# Encontrar el valor mínimo de un listado de numeros. NO USAR min()

maximo_minimo = [7, 93, 2, 8, 425, 1099901, 9, 1101000193, 393934, 3]

# Expected ==> Máximo: 1101000193
# Expected ==> Mínimo: 2

# *********** Ejecicio 3 **************
#Encontrar dentro de una string, aquella palabra con la mayor cantidad de letras.

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis facilisis molestie. In sed elit ut mauris iaculis porttitor. Vestibulum ac justo lobortis, rhoncus eros sed, feugiat ante. Nunc interdum, nunc at pellentesque facilisis, urna libero venenatis purus, sed dignissim orci diam id urna. Aenean placerat leo eget felis efficitur."

#Expected ==> La palabra más grande es: pellentesque con 12 letras

# *********** Ejecicio 4 **************
#Encontrar los calores repetidos en una lista y mostrarlos en una nueva lista

repetidos = [12, 23, 4, 6, 22,99,37, 52, 12, 65, 99, 33, 37]

unicos = []

# Excpected ==> [12, 99, 37]

# *********** Ejecicio 5 **************
#Dada una lista, imprimir la suma de los números pares e imapres.
#Consejo: Ver en el repo, el uso de break

listado_pares_e_impares= [22, 32, 42, 13, 35, 13, 6, 42, 13, 25, 28, 15, 14, 
30, 42, 32, 46, 0, 47, 46]

#Expected:
# Expected ==> Pares 382, 161
# Expected ==> Impares 161

# *********** Ejecicio 6 **************
# Encontrar si en un listado dos números hacen la sumatoria 42. Devolver todos los 
# Pares de números en una lista


listado_suma_42 = [3, 94, 20, 22, 33, 9, 33, 12, 5, 11, 31]

# Expected ==> [20, 22, 33, 9, 9, 33, 11, 31]

# *********** Ejecicio 7 **************
# HARD: Definir una función que diga si una palabra es palíndrome o no.
# Devolvera lo siguiente: La palabra {nombre palabra} {es / no es} palíndrome.

def palindrome(string: str)->str:
    pass

print(palindrome("hola")) # Expected : La palabra hola NO es palíndrome.
print(palindrome("neuquen"))#Expected: La palabra neuquen es palíndrome.




