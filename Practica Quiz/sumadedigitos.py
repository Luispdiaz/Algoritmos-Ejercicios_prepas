bienvenida = "Bienvenido a la calculadora de sumas de digitos"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("La respuesta ser la suma de los digitos del numero que ingrese")
variable1 = input("Por favor, ingrese un numero:")
varible1 = list(variable1)
aux = 0
for i in variable1:
    i = int(i)
    aux = aux + i
print(f"El resultado es {aux}")