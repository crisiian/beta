#Script description:
'''
1. Get 2 numbers (Float or integer)
2. Show main menu: (1). Add, (2). Sub, (3). Mul, (4). Div
3. Select an option
4. Create a function to get the result according with the opt
Other: Clear screen
'''
import os

def calc1(x, y, z):
    if (z == '1'):
        ans = x + y

    if (z == '2'):
        ans = x - y

    if (z == '3'):
        ans = x * y

    if (z == '4'):
        ans = x / y
    return ans

def calc2(x, y, z):
    if (z == '1'):
        ans = x + y
    else:
        if (z == '2'):
            ans = x - y
        else:
            if (z == '3'):
                ans = x * y
            else:
                if (z == '4'):
                    ans = x / y
    return ans

def calc3(x, y, z):
    if (z == '1'):
        ans = x + y
    elif (z == '2'):
        ans = x - y
    elif (z == '3'):
        ans = x * y
    elif (z == '4'):
        if y == 0:
            return "No se puede dividir entre 0"
        ans = x / y
    elif (z == '5'):
        if y == 0:
            division = "No se puede dividir entre 0"
        else:
            division = x / y
        return ("Suma: " + str(x + y) + "\n" +
                "Resta: " + str(x - y) + "\n" +
                "Multiplicación: " + str(x * y) + "\n" +
                "División: " + str(division) + "\n" +
                "Confirmación: operación realizada con éxito.")
    else:
        return "Error: opción no válida. Debe ser un valor entre 1 y 5."

    return str(ans) + "\nConfirmación: operación realizada con éxito."

##### Main #####
num1 = float(input('Press first number: '))
num2 = float(input('Press second number: '))

print("### MAIN MENU ###")
print("[1]. Add")
print("[2]. Sub")
print("[3]. Mult")
print("[4]. Div")
opt = input("::. Press any option: ")


res1 = calc1(num1, num2, opt)
print(f"The result is: {res1}") 

res2 = calc2(num1, num2, opt)
print(f"The result is: {res2}")

res3 = calc3(num1, num2, opt)
print(f"The result is: {res3}")