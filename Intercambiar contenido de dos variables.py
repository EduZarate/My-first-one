### Realizar un  progrma  que  permita  intercambiar
### los valores de dos variables numéricas ingresadas por teclado.

a = 0
b = 0
aux = 0

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

aux = a
a = b
b = aux

print ("El primer número es: ", a, ". Y el segundo número es: ", b)
