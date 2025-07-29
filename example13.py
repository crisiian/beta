def main():
    N = []
    max_numeros = 100
    
    print("Ingrese números enteros. Para terminar, ingrese un valor no numérico.")
    
    while len(N) < max_numeros:
        try:
           
            num = input(f"Ingrese el número {len(N)+1}: ")
            num = int(num)
            
           
            if len(N) >= 2:
                suma_ultimos = N[-1] + N[-2]
                
                
                while num == suma_ultimos:
                    print(f"NO es posible agregar {num} porque es igual a la suma de los dos últimos números ({N[-2]} + {N[-1]} = {suma_ultimos})")
                    num = input("Ingrese otro número: ")
                    num = int(num)
            
           
            N.append(num)
            
        except ValueError:
            
            print("Entrada no válida. Terminando la entrada de números.")
            break
    
    
    print("\nVector final:")
    print(N)

if __name__ == "__main__":
    main()