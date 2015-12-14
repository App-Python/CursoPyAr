#! /usr/bin/env python3
# -*- coding: utf-8 -*-
print("6.1.1. Usando listas como pilas")
'''
Los métodos de lista hacen que resulte muy fácil usar una lista como una pila,
donde el último elemento añadido es el primer elemento retirado
(último en entrar, primero en salir!).
Para agregar un ítem a la cima de la pila, use append().
Para retirar un ítem de la cima de la pila, use pop() sin un índice explícito.
Por ejemplo:
'''

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print("Borramos el último elemento de la lista:", stack.pop())
print(stack)
stack.pop()
stack.pop()
print(stack)

print("\n6.1.2. Usando listas como colas¶")
'''
También es posible usar una lista como una cola,
donde el primer elemento añadido es el primer elemento retirado
(“primero en entrar, primero en salir”);
sin embargo, las listas no son eficientes para este propósito.
Agregar y sacar del final de la lista es rápido,
pero insertar o sacar del comienzo de una lista es lento
(porque todos los otros elementos tienen que ser desplazados por uno).
Para implementar una cola, usá collections.deque
el cual fue diseñado para agregar y sacar de ambas puntas de forma rápida.
Por ejemplo:
'''
from collections import deque
cola = deque(["Eric", "John", "Michael"])
print(cola)  # lista orifginal
cola.append("Terry")  # llega Terry
cola.append("Graham")  # llega Graham
print(cola.popleft())  # el primero en llegar ahora se va

print(cola.popleft())  # el segundo en llegar ahora se va

print(cola)  # el resto de la cola en órden de llegada
['Michael', 'Terry', 'Graham']

print("\n6.1.3. Comprensión de listas")
'''
Las comprensiones de listas ofrecen una manera concisa de crear listas.
Sus usos comunes son para hacer nuevas listas donde cada elemento
es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable,
o para crear una subsecuencia de esos elementos para satisfacer una condición determinada.
Por ejemplo, asumamos que queremos crear una lista de cuadrados, como:
'''
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)
    
print(cuadrados)
'''Podemos calcular la lista de cuadrados sin ningun efecto secundario haciendo:'''
cuadrado = list(map(lambda x: x ** 2, range(10)))
print(cuadrado)
'''o, un equivalente:'''
cua = [x ** 2 for x in range(10)]
print(cua)

# Lista con numeros de 0 hasta n
miLista = [x  for x in range(25)]
print(miLista)
# lista de numeros pares hasta n
n = 50
miLista2 = [x  for x in range(1, n) if x % 2 == 0]
print(miLista2)

# lista de numeros impares hasta n
miLista3 = [x  for x in range(1, n) if x % 2 == 1]
print(miLista3)

# Lista creada con los multiplos m hasta n
m = 3
multiplosDe = [y for y in range(1, n) if y % m == 0]
print(multiplosDe)
'''Una lista de comprensión consiste de corchetes rodeando una expresión seguida de la declaración for y luego cero o más declaraciones for o if'''

''' esta lista de comprensión combina los elementos de dos listas si no son iguales:'''
lis = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(lis)

vec = [-4, -2, 0, 2, 4]

# crear una nueva lista con los valores duplicados
l10 = [x * 2 for x in vec]

# filtrar la lista para excluir números negativos
l11 = [x for x in vec if x >= 0]

# aplica una función a todos los elementos
[abs(x) for x in vec]

# llama un método a cada elemento
frutafresca = ['  banana', '  mora de Logan ', 'maracuya  ']
[arma.strip() for arma in frutafresca]

# crea una lista de tuplas de dos como (número, cuadrado)
l12 = [(x, x ** 2) for x in range(6)]

# la tupla debe estar entre paréntesis, sino es un error
# l13= [x, x ** 2 for x in range(6)]
print(l10)
print(l11)
print(l12)

'''Las comprensiones de listas pueden contener expresiones complejas y funciones anidadas:'''
from math import pi
l13 = [str(round(pi, i)) for i in range(1, 10)]
print(l13)

print("\n6.1.4. Listas por comprensión anidadas¶")
'''La expresión inicial de una comprensión de listas puede ser cualquier expresión arbitraria,
incluyendo otra comprensión de listas.
Considerá el siguiente ejemplo de una matriz de 3x4 implementada como una lista de tres listas de largo 4:
'''
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
'''La siguiente comprensión de lista transpondrá las filas y columnas:'''
l20 = [[fila[i] for fila in matriz] for i in range(4)]
print(l20)
'''Como vimos en la sección anterior,
la lista de comprensión anidada se evalua en el contexto del for que lo sigue,
por lo que este ejemplo equivale a:'''
transpuesta = []
for i in range(4):
    transpuesta.append([fila[i] for fila in matriz])
print(transpuesta)

'''el cual, a la vez, es lo mismo que:'''
transpuesta = []
for i in range(4):
    # las siguientes 3 lineas hacen la comprensión de listas anidada
    fila_transpuesta = []
    for fila in matriz:
        fila_transpuesta.append(fila[i])
    transpuesta.append(fila_transpuesta)
print(transpuesta)

'''En el mundo real,
deberías preferir funciones predefinidas a declaraciones con flujo complejo.
La función zip() haría un buen trabajo para este caso de uso:'''

print("\rCon la funcion zip()\r", list(zip(*matriz)))
