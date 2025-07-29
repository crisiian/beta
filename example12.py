import os
os.system('cls')

#listas (mutables)
my_list =[1,2,3,True,False,"apple",2j,3.14, ['mazda','ford','audi']]
for x in my_list:
    print(x)

    #print(my_list[8][1])
    #print(type(my_list))

    #Tuplas (inmutable)
    my_tupla = (1,2,3)
    print(type(my_tupla))
    print(my_tupla)
   # my_tupla[0] = 10
    #print(my_tupla)

    #diccionarios (mutables)

    my_data = {
        "firstname": "joan",
        "lastname": "ayala",
        "city": "COL"

    }
    print(my_data)
    print(my_data["lastname"])