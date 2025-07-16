import os 
from random import randint

os.system('clear')

i = 1
status = True
while status :
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print(f"Lanzamiento {i}: ")
    print(f"Dices 1: {d1}")
    print(f"Dices 2: {d2}")
    print("\n")
    i+=1

    status_try_again = True
    while status_try_again:
        try_again = input("¿Try again? [s/S/n/N]: ")
        if try_again == 's' or try_again == 'S' or try_again == 'n' or try_again == 'N':
            status_try_again = False
        else :
            print("Invalid option, please press s/S/n/N")

    if try_again == 'n' or try_again == 'N':
        break
    