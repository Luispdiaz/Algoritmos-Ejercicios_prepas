def main():
    bienvenida = "Bienvenido a la calculadora de numeros primos"
    bienvenida = bienvenida.center(50,"*")
    print(bienvenida)
    number = int(input("Por favor, ingrese un numero:"))
    auxiliar = number - 1
    contador = 0
    
    if number == 1:
        print("El numero no es primo.")
    else:
        while auxiliar > 1:
            if number % auxiliar == 0:
                contador += 1
            auxiliar -= 1    
        if contador == 0:
            print("El numero es primo.")
        else:
            print("El numero no es primo.")
main()
