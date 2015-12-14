#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("\n6.4. Conjuntos¶")
'''Python también incluye un tipo de dato para conjuntos.
Un conjunto es una colección no ordenada y sin elementos repetidos.
Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.
Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.
Las llaves o la función set() pueden usarse para crear conjuntos.
Notá que para crear un conjunto vacío tenés que usar set(), no {};
esto último crea un diccionario vacío.
Una pequeña demostración:'''
canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print (canasta)

print('naranja' in canasta)  # verificación de pertenencia rápida
print('aguacate' in canasta)  # verificación de pertenencia rápida

'''veamos las operaciones para las letras únicas de dos palabras'''
a = set('abracadabra')
b = set('alacazam')
print(a)
print("letras en a pero no en b", a - b) 
print("letras en a o en b", a | b)  # letras en a o en b
print("letras en a y en b", a & b)  # letras en a y en b
print("letras en a o b pero no en ambos", a ^ b)  # letras en a o b pero no en ambos
palabra = "mañana"
print("la cantidad de letras en la palabra", palabra, "es", len(palabra), "y las letras sin repetir son: ", set(palabra))

'''De forma similar a las comprensiones de listas, está también soportada la comprensión de conjuntos:'''
print("\nComprensión de Conjuntos")
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
