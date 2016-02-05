#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

'''Funciones str y repr'''
s = "Hola Mundo"
print("Funciones str y repr")
print(str(s))
print(repr(s))

print(str(1 / 7))
print(repr(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '...'
print(s)

print(repr((x, y, ('carne', 'huevos'))))

'''Aca hay dos maneras de escribir una tabla de cuadrados y cubos:'''

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ')
    # notar el uso de 'end' en la linea anterior
    print(repr(x * x * x).rjust(4))

'''otra forma de ahcer lo mismo'''
print('Otr aforma de ahcer lo mismo')
for i in range(1, 11):
    print ("{0:3d} {1:4d}{2:5d}".format(i, i * i, i * i * i))

'''usando format'''
print("\nUsando Formar()")
print("Usando formar, el valor de x es: {0} y su segunda potencia es {1}".format(5, 5 * 5))

print('Somos los {} quienes decimos "{}!".'.format('caballeros', 'No'))

print('Esta {comida} es {adjetivo}.'.format(comida = 'carne', adjetivo = 'espantosa'))

comidad = "sudado"
print("la comida {comida} es muy rica".format(comida = comidad))

'''Se pueden combinar arbitrariamente argumentos posicionales y nombrados:'''
print('La historia de {0}, {1}, y {otro}.'.format('Bill', 'Manfred', otro = 'Georg'))

'''Se pueden usar '!a' (aplica apply()), '!s' (aplica str()) y '!r' (aplica repr()) para convertir el valor antes de que se formatee.'''

print('El valor de Pi es aproximadamente {}.'.format(math.pi))
print('El valor de Pi es aproximadamente {!r}.'.format(math.pi))
'''Un ': y especificador de formato opcionales pueden ir luego del nombre del campo. Esto aumenta el control sobre cómo el valor es formateado. El siguiente ejemplo redondea Pi a tres lugares luego del punto decimal.'''
print('El valor de PI es aproximadamente {0:.3f}.'.format(math.pi))

'''Pasando un entero luego del ':' causará que que el campo sea de un mínimo número de caracteres de ancho. Esto es útil para hacer tablas lindas.'''
tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}'.format(nombre, telefono))
    
'''continuar en:
8.2. Leyendo y escribiendo archivos
'''