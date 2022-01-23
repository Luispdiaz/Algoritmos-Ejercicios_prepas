bienvenida = "Calculadora de numeros de Mersanne"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
numero = int(input("Por favor, ingrese un numero:"))
resultado = 1
auxiliar = 0 
while auxiliar < numero:
    resultado *= 2
    auxiliar += 1
print(resultado)
