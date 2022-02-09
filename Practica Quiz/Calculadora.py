bienvenida = "Bienvenido a la calucladora"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("""En esta calculadora podra realizar las siguientes operaciones:
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Potencia
6. Modulo 
7. Comparar Mayor y Menor que
8. Valor absoluto""")
aux = False
while aux == False:
    number = input("Ingrese el numero correspondiente a la operacion que quiera realizar:")
    print("Presione = si quiere obtener el resultado") 
    if number == "1":
        aux2 = False
        variable2 = 0
        while aux2 == False:
            variable1 = input("Ingrese el numero:")
            if variable1 == "=":
                aux2 = True
                print("El resultado es" , resultado)
            else:
                variable1 = int(variable1)
                variable2 += variable1
                resultado = variable2
    elif number == "2":
        aux2 = False
        variable2 = 0
        while aux2 == False:
            variable1 = input("Ingrese el numero:")
            if variable1 == "=":
                aux2 = True
                print("El resultado es" , resultado)
            else:
                variable1 = int(variable1)
                variable2 = - (variable2) - variable1
                resultado = variable2
    elif number == "3":
        aux2 = False
        variable2 = 1
        while aux2 == False:
            variable1 = input("Ingrese el numero:")
            if variable1 == "=":
                aux2 = True
                print("El resultado es" , resultado)
            else:
                variable1 = int(variable1)
                variable2 = variable1 * variable2
                resultado = variable2
    elif number == "4":
            variable1 = int(input("Ingrese el dividendo:"))
            variable2 = int(input("Ingrese el divisor: "))
            resultado = variable1 / variable2
            print("El resultado es" , resultado)        
    elif number == "5":
        aux2 = False
        variable2 = 1
        while aux2 == False:
            variable1 = input("Ingrese el numero:")
            if variable1 == "=":
                aux2 = True
                print("El resultado es" , resultado)
            else:
                variable1 = int(variable1)
                variable2 = variable1 ** variable2 
                resultado = variable2  
    elif number == "6":
        variable1 = int(input("Ingrese el dividendo:"))
        variable2 = int(input("Ingrese el divisor: "))
        resultado = variable1 % variable2
        print("El resultado es", resultado) 
    elif number == "7":
        aux2 = False
        variable2 = 0
        while aux2 == False:
            variable1 = input("Ingrese el numero:")
            if variable1 == "=":
                aux2 = True
                print("El resultado es" , resultado)
            else:
                variable1 = int(variable1)
                variable2 = variable2 ** variable1
                resultado = variable2
    elif number == "8":
            variable1 = int(input("Ingrese el numero:"))
            if variable1 > 0:
                print("Su resultado es", variable1)
            else:
                resultado = -(variable1)
                print(resultado)
    salida = input("Ingrese 1 si quiere continuar y en su defecto ingrese otro numero:")
    if salida == "1":
        aux = False
    else:
        aux = True
print("Gracias por utilizar la calculadora.")