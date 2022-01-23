from typing import final


bienvenida = "Bienvenido a la calculadora de Palindromos"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("Palindromo significa que una cadena especifica de caracteres se leen igual de izquierda a derecha")
numero = list(input("Por favor, ingrese una palabra o un numero:").lower())
if numero[0]==numero[-1] and numero[1]==numero[-2] and numero[2]==numero[-3]:
    print("El numero o la palabra que ha ingresado es Palindromo.")
else:
    print("El numero o la palabra que ha ingresado no es Palindromo.")