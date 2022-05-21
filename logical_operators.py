# Los operadores lógicos son and, or, not

# And: Necesita que ambas partes sean verdaderas para cumplir con el requisito
# 10 == 10 and "hola" == "hola" . Esto es Verdadero
# VERDADERO Y VERDADERO = VERDADERO

condicion_verdadera_1 = 10 == 10
condicion_verdadera_2 = "barcelona" == "barcelona"
condicion_falsa_1 = "hola" == "chau"
condicion_falsa_2 = 10 != 10

premisa = condicion_verdadera_1 and condicion_verdadera_2 #True

print(f'10 es igual a 10 Y barcelona es igual a barcelona: {premisa}')

#Pero si una de las condiciones es falsa, la premisa es falsa.
# 10 == 10 and "hola" == "chau" . Esto es Falso
# VERDADERO Y FALSO = FALSO

premisa = condicion_verdadera_1 and condicion_falsa_1
print(f'10 es igual a 10 Y hola es igual a chau: {premisa}') #False


# Or. Con que una de las partes sea verdadera, la premisa es verdadera
# 10 == 10 or "hola" == "chau" . Esto es VERDADERO
# VERDADERO O FALSO = VERDADERO

premisa = condicion_verdadera_1 or condicion_falsa_1
print(f'10 es igual a 10 O hola es igual a chau: {premisa}') #True

#Pero si las dos condiciones son falsas entonce es falso

premisa = condicion_falsa_1 or condicion_falsa_2
print(f'10 NO es igual a 10 O hola es igual a chau: {premisa}') #False

# Las operaciones lógicas se pueden encadenar como si fueran operaciones matemáticas

premisa = condicion_verdadera_1 and condicion_verdadera_2 or condicion_falsa_1
#            TRUE                Y TRUE                   O FALSE == True
print(premisa) #TRUE

premisa = (condicion_verdadera_1 or condicion_falsa_1) and condicion_falsa_2
#               TRUE              O FALSE               Y FALSE 
#           (       TRUE                            )   Y FALSE == FALSE
print(premisa)



premisa = (condicion_verdadera_1 and condicion_falsa_1) or condicion_falsa_2
#               TRUE              Y   FALSE               Y FALSE 
#           (       FALSE                            )   Y FALSE == FALSE

print(premisa)

#NOT. Niega la condición original. Si es Verdadero lo vuelve falso y viceversa

premisa = not condicion_falsa_1 and condicion_verdadera_1
#             VERADERO          Y VERDADERO == VERDADERO

print(premisa)

# Esta premisa estaba unas lineas antes. Si le agregamos el not, cambia de falso a
#verdadero
premisa =  not(condicion_verdadera_1 and condicion_falsa_1) or condicion_falsa_2
#               TRUE              Y   FALSE               Y FALSE 
#       NOT    (       FALSE                            )   Y FALSE == FALSE
#             (       TRUE                            )   Y FALSE == TRUE

print(premisa)

