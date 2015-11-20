# -*- coding: utf-8 -*-

from _ast import Str
print ((50 - 5 * 6) / 4)  # la misma prioridad en las operaciones
print (8 / 5)  # /retorna siempre un float
print (8 // 5)  # elimina la parte fraccionaria
print (8 % 5)  # devuelve le modulo

# potencias
print (2 ** 5)  # potencias

# mostrar comillas
print ("\"Hola, como estas?\"")
print ('\"Hola, como estas?\"')

print ('doesn\'t')
print ("doesn\'t")
print ('"Si," le dijo.')

print('"Isn\'t," she said.')

print("-Primera linea\r\n-Segunda linea")

print('C:\algun\nombre')  # aquí \n significa nueva línea!
print(r'C:\algun\nombre')  # nota la r antes de la comilla

print("""\
cadena de 
varias 
lineas  """)

# Las cadenas de texto pueden ser concatenadas (pegadas juntas) con el operador + y repetidas con *:

var = "Mundo"
print ("Hola " + var)
print("Hola. "*3 + var)
# Dos o más cadenas literales (aquellas encerradas entre comillas) una al lado de la otra son automáticamente concatenadas:
print("Py""thon")
# Esto solo funciona con dos literales, no con variables ni expresiones:

texto = ('Poné muchas cadenas dentro de paréntesis '
             'para que ellas sean unidas juntas.')
print(texto)

palabra = 'Python'
print(palabra[0])  # caracter en la posición 0
print(palabra[5])  # caracter en la posición 5
print(palabra[-1])  # último caracter

# rebanadas o subcadenas
print(palabra[2:5])  # caracteres desde la posición 2 (incluída) hasta la 5 (excluída)

print(palabra[:3] + palabra[3:])
print(palabra[3:] + palabra[:3])

# cambiando una letra
otraPalabra = "J" + palabra[1:]
print(otraPalabra)

# La función incorporada len() devuelve la longitud de una cadena de texto:
s = 'supercalifrastilisticoespialidoso'
print("la palabra " + s + " contiene " + str(len(s)) + " caracteres.")
