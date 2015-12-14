#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("\n6.2. La instrucción del.")
'''Hay una manera de quitar un ítem de una lista dado su índice en lugar de su valor:
la instrucción del. Esta es diferente del método pop(), el cual devuelve un valor.
La instrucción del también puede usarse para quitar secciones de una lista
o vaciar la lista completa (lo que hacíamos antes asignando una lista vacía a la sección).
Por ejemplo:'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

'''del puede usarse también para eliminar variables:'''
del a