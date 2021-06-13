### Realizar un programa que determine y muestre por pantalla los
### números pares entre 2 y 100 (inclusives).


contador = 0
for contador in range (0,100):
    if contador % 2 == 0:
        print (contador)
    contador +=1
