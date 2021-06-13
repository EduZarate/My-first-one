""" Implementar un algoritmo que calcule y muestre por pantalla el
valor final de la compra de un artículo. El algoritmo debe permitir
el ingreso del precio del  artículo  y la  cantidad  de  artículos.
Se  debe  considerar  la  aplicación  de impuestos por un valor de 21%
del subtotal."""

impuestos = 0.21
precio = float(input("Ingrese precio de producto: "))
cant = float(input("Ingrese cantidad: "))
subtotal = precio * cant
print ("El precio final es: ",subtotal + (subtotal * impuestos))
