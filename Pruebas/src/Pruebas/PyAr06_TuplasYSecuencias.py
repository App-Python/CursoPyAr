#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("\n6.3. Tuplas y secuencias¶")
'''Una tupla consiste de un número de valores separados por comas, Son Inmutables, por ejemplo:'''
t = 12345, 54321, 'hola!'
print(t[0])

print(t)

# Las tuplas pueden anidarse:
u = t, (1, 2, 3, 4, 5)
print(u)

# Las tuplas son inmutables:
# t[0] = 88888

# pero pueden contener objetos mutables:
v = ([1, 2, 3], [3, 2, 1])
print(v)

'''Un problema particular es la construcción de tuplas que contengan 0 o 1 ítem:
la sintaxis presenta algunas peculiaridades para estos casos.
Las tuplas vacías se construyen mediante un par de paréntesis vacío;
una tupla con un ítem se construye poniendo una coma a continuación del valor
(no alcanza con encerrar un único valor entre paréntesis).
Feo, pero efectivo. Por ejemplo:'''
vacia = ()
singleton = 'hola',  # <-- notar la coma al final
print(len(vacia))
print(len(singleton))
print(singleton)

'''La declaración t = 12345, 54321, 'hola!' es un ejemplo de empaquetado de tuplas:
los valores 12345, 54321 y 'hola!' se empaquetan juntos en una tupla.
La operación inversa también es posible:'''
print("\nDesempaquetado")
x, y, z = t  # las 3 variables reciben los 3 valores de la tupla
print(x, y, z)