bienvenida = "Bienvenidos a la pizzeria"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print("Quiere una pizza vegetariana?")
respuesta = input("""1. Si
2. No
Coloque el numero corresponidente:""")
if respuesta == "1":
    print("Los ingrediente de la pizza vegetariana son los siguienttes: Pimiento y Tofu")
    respuesta1 = input("""Cual ingrediente prefiere? 
    1. Pimiento
    2. Tofu
    Ingrese el numero:""")
    if respuesta1 == "1":
        print("Excelente eleccion, su pizza sera vegetariana de Pimiento.")
    else:
      print("Excelente eleccion, su pizza sera vegetariana de Tofu.")   
else:
    print("Los ingredientes de la pizza no vegetariana son los siguientes: Peperoni, Jamon y Salmon")
    respuesta1 = input("""Cual ingrediente prefiere? 
    1. Peperoni
    2. Jamon
    3. Salmon
    Ingrese el numero:""")
    if respuesta1 == "1":
        print("Excelente eleccion, su pizza sera no vegetariana de Peperoni")
    elif respuesta1 == "2":
        print("Excelente eleccion, su pizza sera no vegetariana de Jamon")
    else:
      print("Excelente eleccion, su pizza sera no vegetariana de Salmon")
    

