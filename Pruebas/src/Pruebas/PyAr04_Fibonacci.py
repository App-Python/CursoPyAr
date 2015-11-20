# -*- coding: utf-8 -*-
'''
Created on 19/11/2015

@author: hernan
'''
print ("Secuencia Fibonacci del 1 hasta el 1000")
a, b = 0, 1
lista = [a]
while b < 1000:
    lista.append(b)
    a, b = b, a + b
    
print(lista)


