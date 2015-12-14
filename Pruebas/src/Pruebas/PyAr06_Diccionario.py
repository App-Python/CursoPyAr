#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from _ast import List

print("6.5. Diccionarios")
'''Lo mejor es pensar en un diccionario como un conjunto no ordenado de pares clave: valor,
con el requerimiento de que las claves sean únicas.

Hacer list(d.keys()) en un diccionario devuelve una lista de todas las claves usadas en el diccionario, en un orden arbitrario 
(si las querés ordenadas, usá en cambio sorted(d.keys()).
Para controlar si una clave está en el diccionario, usá el in.
Un pequeño ejemplo de uso de un diccionario:'''

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127  # agregamos un nuevo par
print(tel)

print(tel['jack'])  # consultamos por la clave
print(tel['sape']) 
tel['irv'] = 4127  # agregamos nuevo par
print(tel)

print(list(tel.keys()))  # mostramos la lista desordenada

print(sorted(tel.keys()))  # mostramos la lista ordenada

print('guido' in tel)  # preguntamos si esta

print('jack' not in tel)  # preguntamos si no esta

'''El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:'''

d = dict([(1, "Uno"), (2, "Dos"), (3, "Tres"), (4, "Cuatro")])
print(d)
print(list(d.keys()))  # mostrar las claves
print(list(d.values()))  # mostrar los valores

print(sorted(d.keys()))  # mostrar las claves ordenados
print(sorted(d.values()))  # mostrar los valores ordenados

'''Además,
las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias de clave y valor:'''
myDc = {x: x ** 2 for x in (2, 4, 6, 8, 10)}
print(myDc)
