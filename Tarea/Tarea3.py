bienvenida = "Calculadora de numeros de Mersanne"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("""Quiere usted calcular el primer numero de Mersanne?
1. Si
2. No""")
respuesta = input("Ingrese el número correspondiente a su respuesta:")
base = 2
exponente = 1
if respuesta == "1":
    number = base ** exponente
    print(f"El primer numero de Mersanne es {number}.")
    print("""Quiere usted calcular el siguiente numero de Mersanne?
1. Si
2. No""")
    respuesta = input("Ingrese el número correspondiente a su respuesta:")
    while respuesta == "1":
        exponente += 1
        number = base ** exponente
        print(f"El siguiente numero de Mersanne es {number}.")
        print("""Quiere usted calcular el siguiente numero de Mersanne?
1. Si
2. No""")
        respuesta = input("Ingrese el número correspondiente a su respuesta:")
    print("Gracias por probar la calculadora de Mersanne.")    
else:
    print("Para que ingreso en la calculadora? :-/ ")
