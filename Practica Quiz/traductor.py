bienvenida = "Bienvenidos al traductor"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
print(""" Observe la siguiente lista de palabras:
1. Perro
2. Gato
3. Pajaro
4. Pestañar
5. Pene
6. Bicho""")
variable1 = input("Ingrese el numero de la palabra que quiera traducir:")
if variable1 == "1":
    print("La traduccion es Dog.")
elif variable1 == "2":
    print("La traduccion es Cat.")
elif variable1 == "3":
    print("La traduccion es Bird.")
elif variable1 == "4":
    print("La traduccion es Blink.")
elif variable1 == "5":
    print("La traduccion es Penis.")
elif variable1 == "6":
    print("La traduccion es Cr7.")
else:
    print("El dato que ha ingresado no es valido.")


