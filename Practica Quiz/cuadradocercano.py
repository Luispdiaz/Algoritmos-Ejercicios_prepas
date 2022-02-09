bienvenida = "Bienvenido a la calculadora de potencias"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
variable1 = int(input("Ingrese un numero:"))
aux = 1
result = 0
while variable1 > aux**2:
    result = aux ** 2
    aux += 1
print(f"La potencia mas cercana por debajo es {result}")

while variable1 > result:
    result = aux ** 2
    aux += 1
print(f"La potencia mas cercana por arriba es {result}")    