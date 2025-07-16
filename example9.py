'''
Generar una lista de numeros teniendo en cuenta un numero de inicio (li) y un numero de fin (ls).

Los numeros deben ser ingresados por el usuario.

Si el primer numero es mayor que el segundo, la ista se debe imprimir en orden descendente.
'''

import os

os.system('clear')
li = int(input("Ingresa limite inferior: "))
ls = int(input("Ingresa limite superior: "))

i = li
if li <= ls :
    while i <= ls :
        print(i)
        i+=1
else :
    while i >= ls:
        print(i)
        i-=1