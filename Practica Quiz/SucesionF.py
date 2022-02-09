bienvenida = "Bienvenido a la sucesion de fibonacci"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
n = int(input("Por favor, ingrese un numero el cual sera el limite de la sucesion:"))
x = 0
y = 1
z = 1
resultados = []
while z <= n :
    resultados.append(str(z))
    z = x + y
    x = y 
    y = z
    
print(",".join(resultados))



