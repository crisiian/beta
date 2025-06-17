'''
descripption
get player name
generate two random number into 2 dices 
dice 1: 1-6
dice 2: 1-6 

print dices values


'''
import os
from random import randint

os.system ('elear')
print ("welco parchis")
#player_name=("player name")
player_name= input("player name")

dices1 = randint(1,6)
dices2 = randint(1,6)

print(f"Dice1: {dice1}")
print(f"Dice2: {dice2}")