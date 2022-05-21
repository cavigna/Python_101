#En Python se pueden hacer comparaciones lógicas. Como por ejemplo mayor, menor o igual.
#Toda comparación lógica nos va a devoler un Boolean. Es decir Verdadero o Falso.

# Mayor o Menor(<>)

n1 = 10 
n2 = 5


print(f'n1 menor a n2 {n1 < n2}') #False 10 es mayor que 5
print(f'n1 mayor a n2 {n1 > n2}') #True 10 es mayor que 5

#Mayor o Igual que (<=, >=)

n3 = 10
print(f'n1 menor a n3 {n1 < n3}') # Falso por que son iguales
print(f'n1 menor o igual que n3 {n1 <= n3}') # Verdader por que son iguales
print(f'n1 mayor o igual que n3 {n1 <= n3}') # Verdader por que son iguales

#Igualdad. Para comprobar igualdad se utilizan dos signos iguales seguidos ==.

print(f'n1 igual a n3 {n1 == n2}')

#Desigualdad o Distinto. !=

print(f'una manzanda igual a una pera {"manzana" == "pera"}')
print(f'una manzanda no es igual a una pera {"manzana" != "pera"}')





