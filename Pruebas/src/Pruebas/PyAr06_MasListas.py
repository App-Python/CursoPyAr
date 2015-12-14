#! /usr/bin/env python3
# -*- coding: utf-8 -*-

b = []
print("\nlist.append(x)")
''' list.append(x)
Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].

'''
b.append(1)
b[len(b):] = [2]
print(b)

''' list.extend(L)
Extiende la lista agregándole todos los ítems de la lista dada. Equivale a a[len(a):] = L
'''
print("\nlist.extend(L)")
l = [4, 5, 6]
l2 = [1, 2, 3]
print(l2)
l2.extend(l)
print(l2)

''' list.insert(i, x)
    Inserta un ítem en una posición dada.
    El primer argumento es el índice del ítem delante del cual se insertará,
    por lo tanto a.insert(0, x) inserta al principio de la lista,
    y a.insert(len(a), x) equivale a a.append(x)
'''
print("\nlist.insert(i, x)")
l2.insert(6, 7)
print(l2)
l2.insert(len(l2), 8)
print(l2)


'''list.remove(x)
Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.
'''
print("\nlist.remove(x)")
l2.remove(6)
print(l2)

'''list.pop([i])
Quita el ítem en la posición dada de la lista, y lo devuelve.
Si no se especifica un índice, a.pop() quita y devuelve el último ítem de la lista.
(Los corchetes que encierran a i en la firma del método denotan que el parámetro es opcional, no que deberías escribir corchetes en esa posición. Verás esta notación con frecuencia en la Referencia de la Biblioteca de Python.)
'''
print("\nlist.pop([i])")
l2.pop(len(l2) - 1)  # elimina el ultimo
l2.pop()  # elimina el ultimo
print(l2)

'''list.clear()
Quita todos los elementos de la lista. Equivalente a del a[:]
'''
print("\nlist.clear()")
l2.clear()
del l2[:]  # eqivale a la anterior
print(l2)

'''list.index(x)
Devuelve el índice en la lista del primer ítem cuyo valor sea x. Es un error si no existe tal ítem.
'''
print("\nlist.index(x)")
l2.extend(l)
print(l2)
print(l2.index(6))  # devuelve la posicion del valor dado
print(l2.index(l2[len(l2) - 1]))  # devuelve la posicion del ultimo valor

'''list.count(x)
Devuelve el número de veces que x aparece en la lista.
'''
print("\nlist.count(x)")
l2.append(5)
print("el 5 aparece", l2.count(5), "veces en la lista")
l2.pop()  # borramos para que la lista queda como antes de este metodo

'''list.reverse()
Invierte los elementos de la lista in situ.
'''
print("\nlist.reverse()")
l2.reverse()
print(l2)

'''list.sort(key=None, reverse=False)
Ordena los ítems de la lista in situ
(los argumentos pueden ser usados para personalizar el orden de la lista, ver sorted() para su explicación).
'''
print("\nlist.sort(key=None, reverse=False)")
l2.sort(key = None, reverse = False)  # puede usarse sin parametros sort()
print(l2)

'''list.copy()
Devuelve una copia superficial de la lista. Equivalente a a[:].
'''
print("\nlist.copy()")
l3 = []
print(l3)

'''Un ejemplo que usa la mayoría de los métodos de lista:'''
print("\nUn ejemplo que usa la mayoría de los métodos de lista")
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
a

a.index(333)

a.remove(333)
a

a.reverse()
a

a.sort()
a

a.pop()

a
