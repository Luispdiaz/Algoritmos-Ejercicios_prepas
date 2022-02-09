bienvenida = "Bienvenido a los dados"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("El dado arrojara las combinaciones que suman el numero que ingrese")
variable1 = int(input("Ingrese un numero:"))
combinaciones = []
for i in range(1,7):
    for j in range(1,7):
        if (i + j == variable1):
            if sorted([i,j]) in combinaciones:
                continue
            else:
                combinaciones.append([i,j])
print("Las combinaciones posibles son:")
combinaciones = enumerate(combinaciones)
for i,combinacion in combinaciones:
    print(f"\t*{combinacion[0]}-{combinacion[1]}" )                 

