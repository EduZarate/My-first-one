### Realizar  un  programa  que  permita  el  ingreso  de  10 números  enteros
### y muestre  por  pantalla  solamente  los  números  positivos que se hayan ingresado.

# Algoritmo Números_Positivos

cantidad = 1

for cantidad in range (10):
        num = int(input("Ingresa un número: "))
        if num > 0:
                print (num)
        cantidad ++ 1


