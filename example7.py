'''
script description
crear un script python que lance dos dados N veces y visualice por pantalla los resultados 

la cantidad o numeros de veces debe ser ingrsada por el usuario 
deben lanzar dos dados 
usar funcion
'''

import os 
from random import randint

lan = int(input('cuantas veces deceas lanzar los dados:'))

i=1
while i <= lan :

    d1 = randint(1,6)
    d2 = randint(1,6)
     
    print(f"dice 1: {d1}")
    print(f"dice 2: {d2}")

    print("\n")

    i+=1
    