bienvenida = "Bienvenido a la calculadora de numeros amigos"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
aux = False
while aux==False:
    number1 = input("Ingrese el primer numero:")
    if number1.isnumeric():
        number1 = int(number1)
        aux2 = 0
        for i in range(1, number1):
            result= number1 % i
            if result == 0:
                aux2 += i
    else:
        print("El dato que ha ingresado no es valido")
    number2 = input("Ingrese el segundo numero:")
    if number2.isnumeric():
        number2 = int(number2)
        aux3 = 0
        for i in range(1, number2):
            result= number2 % i
            if result == 0:
                aux3 += i   
    else:
        print("El dato que ha ingresado no es valido")
    if aux3 == number1 and aux2 == number2:
        print("Los numeros son amigos")
    else:
        print("Los numeros no son amigos.")
    bucle = input("Si no quiere volver a intentarlo, ingrese 1, en caso contrario ingrese otro dato:")
    if bucle == "1":
        aux = True