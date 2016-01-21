#! /usr/bin/env python3
# -*- coding: utf-8 -*-


print("9.3. Manejando excepciones")

while True:
    try:
        x = int(input("Por favor ingrese un numero:"))
        print("La segunda potencia de {} es {}.".format(x, x ** 2))    
        break
    except ValueError:
        print("El valor no es un numero valido.")
    except:
        print("Se presento un error.")


'''las excepciones pueden agruparse de la siguinente manera:
    except (RuntimeError, TypeError, NameError):'''
print("\n")

import sys
try:
    f = open('miarchivo.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("Error OS: {0}".format(err))
except ValueError:
    print("No pude convertir el dato a un entero.")
except:
    print("Error inesperado:", sys.exc_info()[0])
    raise

'''Las declaraciones try ... except tienen un bloque else opcional,
    el cual, cuando esta presente, debe seguir a los except.
    Es util para aquel c�digo que debe ejecutarse si el bloque try no genera una excepci�n.'''

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('no pude abrir', arg)
    else:
        print(arg, 'tiene', len(f.readlines()), 'lineas')
        f.close()

print("\n9.4. Levantando excepciones")

# raise NameError('Hola')


print("\n9.5. Excepciones definidas por el usuario")


class MiError(Exception):
    def __init__(self, valor):
            self.valor = valor
    def __str__(self):
        return repr(self.valor)
    
try:
    raise MiError(2 * 2)
except MiError as e:
    print('Ocurrió mi excepción, valor:', e.valor)

raise MiError('oops!')


'''Una cláusula finally siempre es ejecutada antes de salir de la declaración try,
ya sea que una excepción haya ocurrido o no. Cuando ocurre una excepción en la cláusula try
y no fue manejada por una cláusula except (o ocurrió en una cláusula except o else),
es relanzada luego de que se ejecuta la cláusula finally.
El finally es también ejecutado “a la salida” cuando cualquier otra cláusula de la declaración
try es dejada via break, continue or return.'''

'''En aplicaciones reales, la cláusula finally es útil para liberar recursos externos
(como archivos o conexiones de red), sin importar si el uso del recurso fue exitoso.'''
    
print("\n9.7. Acciones predefinidas de limpieza")
'''Algunos objetos definen acciones de limpieza estándar que llevar a cabo cuando el objeto
no es más necesitado, independientemente de que las operaciones sobre el objeto hayan sido
exitosas o no. Mirá el siguiente ejemplo, que intenta abrir un archivo e imprimir su contenido en la pantalla.:'''

for linea in open("miarchivo.txt"):
    print(linea, end = "")

'''El problema con este código es que deja el archivo abierto por un periodo
de tiempo indeterminado luego de que esta parte termine de ejecutarse.
Esto no es un problema en scripts simples, pero puede ser un problema en aplicaciones más grandes.
La declaración with permite que objetos como archivos sean usados de una forma
que asegure que siempre se los libera rápido y en forma correcta.'''

with open("miarchivo.txt") as f:
    for linea in f:
        print(linea, end = "")
