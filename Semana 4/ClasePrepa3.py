print("Bienveido ingresa un numero")
validacion=True
option=0
while option == 0:
    while validacion:
    num=int(input("ingresa un numero:"))
    if num.isnumeric():
        validacion=False
    else:
        print("Error el numero no es valido")
    num=int(num)
    suma = 0
    for x in range(1,(num//2)+1):
        if num%x==0:
        suma+=x
    if suma == num:
    print("Es perfecto")
    else:
    print("no es perfecto")
    option=input("ingresa 0 para saber si otro numero es perfecto, ingresa cualquier otro para salir:")
    while not(option.isnumeric()):
        option=input("Error. ingresa 0 para saber si otro numero es perfecto, ingresa cualquier otro para salir")
option=int(option)

