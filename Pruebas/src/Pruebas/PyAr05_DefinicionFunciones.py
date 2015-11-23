#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
5.6. Definiendo funciones
http://docs.python.org.ar/tutorial/3/index.html
Subido a GitHub
'''
def fib(n):  # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ', ')
        a, b = b, a + b
    else:
        print()
      
# Ahora llamamos a la funcion que acabamos de definir:
fib(2000)

# Todo los metodos tienen un retorno por defento, este es None
print(fib(2000))
# Otra forma de ahcer el llamado a la funcion
f = fib
f(2000)
print(f(2000))

fib(0)
print(fib(0))

def fib2(n):  # devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # ver abajo
        a, b = b, a + b
    return result

f100 = fib2(100)  # llamarla
print(f100)  # escribir el resultado


'''
También es posible definir funciones con un número variable de argumentos.
Hay tres formas que pueden ser combinadas.
'''
'''
5.7.1. Argumentos con valores por omisión
'''
def pedir_confirmacion(prompt, reintentos = 4, queja = 'Si o no, por favor!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'N', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise OSError('usuario duro')
        print(queja)

pedir_confirmacion('¿Realmente queres salir?', queja = 'Opción no validad. Sólo SI o NO ')
# Otros formas de llamar la misma función
# pedir_confirmacion('¿Realmente queres salir?', 2, 'Opción no validad. Sólo SI o NO ')
# pedir_confirmacion('¿Realmente queres salir?')


'''
Los valores por omisión son evaluados en el momento de la definición de la función,
en el ámbito de la definición, entonces: lo sigueinte retorna 5
'''
i = 5
def f(arg = i):
    print(arg)

i = 6
f()

'''
Advertencia importante:
El valor por omisión es evaluado solo una vez.
Existe una diferencia cuando el valor por omisión es un objeto mutable como una lista, diccionario, o instancia de la mayoría de las clases.
Por ejemplo, la siguiente función acumula los argumentos que se le pasan en subsiguientes llamadas:
'''
def fu(a, L = []):
    L.append(a)
    return L

print(fu(1))
print(fu(2))
print(fu(3))

'''
Si no se quiere que el valor por omisión sea compartido entre subsiguientes llamadas, se pueden escribir la función así:
'''
def fu2(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(fu2(1), end = '-')
print(fu2(2), end = '-')
print(fu2(3))
print()
print()

'''
5.7.2. Palabras claves como argumentos
'''

def loro(tension, estado = 'muerto', accion = 'explotar', tipo = 'Azul Nordico'):
    print("-- Este loro no va a", accion, end = ' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")
    
'''
multiples formas de llamar este metodo 
'''
loro(1000)  # 1 argumento posicional
loro(tension = 1000)  # 1 argumento nombrado
loro(tension = 1000000, accion = 'VOOOOOM')  # 2 argumentos nombrados
loro(accion = 'VOOOOOM', tension = 1000000)  # 2 argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar')  # 3 args posicionales
loro('mil', estado = 'viendo crecer las flores desde abajo')  # uno y uno

'''
Cuando un parámetro formal de la forma **nombre está presente al final, recibe un diccionario (ver Tipos integrados)
conteniendo todos los argumentos nombrados excepto aquellos correspondientes a un parámetro formal.
Esto puede ser combinado con un parámetro formal de la forma *nombre que recibe una tupla conteniendo
los argumentos posicionales además de la lista de parámetros formales.
(*nombre debe ocurrir antes de **nombre).
Por ejemplo, si definimos una función así:
'''
def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    claves = sorted(palabrasclaves.keys())
    for c in claves:
        print(c, ":", palabrasclaves[c])
        
'''Puede ser llamada así:'''

ventadequeso("Limburger", "Es muy liquido, sr.",
             "Realmente es muy muy liquido, sr.",
             cliente = "Juan Garau",
             vendedor = "Miguel Paez",
             puesto = "Venta de Queso Argentino")

'''
5.7.3. Listas de argumentos arbitrarios
'''
def concatenar(*args, sep = "/"):
    return sep.join(args)

print(concatenar("tierra", "marte", "venus"))
print(concatenar("tierra", "marte", "venus", sep = "-"))

'''
5.7.4. Desempaquetando una lista de argumentos
'''
'''
La situación inversa ocurre cuando los argumentos ya están en una lista o tupla pero necesitan ser desempaquetados para llamar a una función que requiere argumentos posicionales separados. Por ejemplo, la función predefinida range() espera los argumentos inicio y fin. Si no están disponibles en forma separada, se puede escribir la llamada a la función con el operador para desempaquetar argumentos de una lista o una tupla *::
'''

list1 = (range(3, 6))  # llamada normal con argumentos separados
args = [3, 6]
list2 = (range(*args))  # llamada con argumentos desempaquetados de la lista
list1
print(list1)
print(list2)

'''
Del mismo modo, los diccionarios pueden entregar argumentos nombrados con el operador **::
'''
def loro2(tension, estado = 'rostizado', accion = 'explotar'):
    print("-- Este loro no va a", accion, end = ' ')
    print("si le aplicás", tension, "voltios.", end = ' ')
    print("Está", estado, "!")

d = {"tension": "cinco mil", "estado": "demacrado",
     "accion": "VOLAR"}
loro(**d)
print()
'''
5.7.5. Expresiones lambda
'''
print("Hacer Incrementador, inicia en 42")
def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42)
print(f(0))
print(f(1))
print(f(1))
print(f(8))