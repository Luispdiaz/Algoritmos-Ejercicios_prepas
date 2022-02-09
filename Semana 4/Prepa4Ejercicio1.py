print("Bienvenido")
variable = input("Ingresa un numero de tres digitos no iguales:")
if len(variable)==3 and variable.isnumeric:
    if int(variable[0]) < int(variable [1]) < int(variable[2]):
        print("Si")    
    else:
        print("No")
else:
    print("Error")

cedulas = "30,21,45,50"
listacedulas = cedulas.split(",")