#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("6.6. Técnicas de iteración")
'''Cuando iteramos sobre diccionarios,
se pueden obtener al mismo tiempo la clave y su valor correspondiente usando el
método items().'''

print("\nCuando iteramos sobre diccionarios,")
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.items():
    print(k, v)

print("\nCuando se itera sobre una secuencia.")
'''Cuando se itera sobre una secuencia,
se puede obtener el índice de posición junto a su valor correspondiente usando la
función enumerate().'''
for i, v in enumerate(['ta', 'te', 'ti']):
    print(i, v)

print("\nPara iterar sobre dos o más secuencias al mismo tiempo.")
'''Para iterar sobre dos o más secuencias al mismo tiempo,
los valores pueden emparejarse con la
función zip().'''
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print('Cual es tu {0}?  {1}.'.format(p, r))

print("\nPara iterar sobre una secuencia en orden inverso.")
'''Para iterar sobre una secuencia en orden inverso,
se especifica primero la secuencia al derecho y luego se llama a la
función reversed().'''
for i in reversed(range(1, 10, 2)):
    print(i)

'''Para iterar sobre una secuencia ordenada,
se utiliza la función sorted()
la cual devuelve una nueva lista ordenada dejando a la original intacta.'''
    
print("\nPara iterar sobre una secuencia ordenada.")
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
for f in sorted(set(canasta)):
    print(f)
    
'''Para cambiar una secuencia sobre la que estás iterando mientras estás adentro del ciclo
(por ejemplo para duplicar algunos ítems),
se recomienda que primera hagas una copia.
Ciclar sobre una secuencia no hace implícitamente una copia.
La notación de rebanadas es especialmente conveniente para esto:'''

print("\nPara cambiar una secuencia sobre la que estás iterando mientras estás adentro del ciclo.")
palabras = ['gato', 'ventana', 'defenestrar']
for p in palabras[:]:  # ciclar sobre una copia de la lista entera
    if len(p) > 6:
       palabras.insert(0, p)
print(palabras)

