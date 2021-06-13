""" Implementar un algoritmo que calcule y muestre por pantalla el
valor final de la compra de un artículo. El algoritmo debe permitir
el ingreso del precio del  artículo  y la  cantidad  de  artículos.
Se  debe  considerar  la  aplicación  de impuestos por un valor de 21%
del subtotal."""

precio = float(input("Ingrese precio de producto: "))
cant = float(input("Ingrese cantidad: "))
print ("El precio final es: ",precio * cant)


