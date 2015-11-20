#! /usr/bin/env python3
# -*- coding: utf-8 -*-


print("La sentencia if")
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print("Negativo cambiado a cero (0)")
elif x == 0:
    print("Cero (0)")
elif x == 1:
    print("Uno (1)")
else:
    print("Numero positivo")

#*******************************************
print("\nLa sentencia for")
# Midiendo cadenas de texto
palabras = ['gato', 'ventana', 'defenestrado', 'oso', 'cangrejo']
for p in palabras:
    print(p, len(p))
'''
Si necesitás modificar la secuencia sobre la que estás iterando mientras estás adentro del ciclo (por ejemplo para borrar algunos ítems), se recomienda que hagas primero una copia.
Iterar sobre una secuencia no hace implícitamente una copia. La notación de rebanada es especialmente conveniente para esto:
'''
    
for p in palabras[:]:  # hace una copia por rebanada de toda la lista
    if len(p) > 6:
        palabras.insert(0, p)
        
print(palabras)

print("La función range()")
for i in range(5):
    print (i)
    
for i in range(5, 10):
    print ("-", i)
    
for i in range(0, 10, 3):
    print("De 0 a 10, de 3 en 3:", i)
    
for i in range(-20, 11, 5):
    print("-De -20 a 10, de 5 en 5:", i)

# Para iterar sobre los índices de una secuencia, podés combinar range() y len() así:
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print (i, a[i])

print(range(100))
print()

'''La función list() es otra; crea listas a partir de iterables:
'''
l = list(range(0, 15))
print(l)
print(list(range(5, 21)))

'''Las sentencias break, continue, y else en lazos

La sentencia break, como en C, termina el lazo for o while más anidado.

'''
for i in range(5):
    print ("El valor de i:", i)
else:
    print ("El ciclo termino")
    print ("El valor de i sin ciclo:", i)

print ("El valor de i sin ciclo:", i)

print()

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n / x)
            break
    else:
        # sigue el bucle sin encontrar un factor
        print(n, 'es un numero primo')

# EJEMPLO. contar los letras "a" en una frase
frase = "Quien no vive para servir, no sirve para vivir"
letra = "v"

contador = 0
for i in range(len(frase)):
    if frase[i] == letra:
        contador = contador + 1
print("la cantidad de \"" + letra + "\" es", contador)

'''5.5. La sentencia pass'''

# while True:
    # pass  # Espera ocupada hasta una interrupción de teclado (Ctrl+C)

