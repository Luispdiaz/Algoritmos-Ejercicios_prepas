bienvenida = "Bienvenido a la calculadora de numeros deficientes"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("Un numero deficiente es un numero que cumple que la suma de sus divisores propios es menor a el")
number = input("Ingrese un numero:")
if number.isnumeric():
    number = int(number)
    aux = 1
    aux2= 0
    if number==1:
        print("El numero no es deficiente")
    else:
        while number > aux:
            result = (number % aux)
            if result == 0:
                aux2+=aux 
            aux+=1
        if aux2 < number:
            print("El numero es deficiente")
        else:
            print("El numero no es deficiente")
else:
    print("El dato que ha ingresado no es valido")