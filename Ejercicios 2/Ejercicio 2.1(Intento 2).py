bienvenida = "Hola, por favor ingresa los siguientes datos:"
bienvenida1 = bienvenida.center(50,"-")
print(bienvenida1)
nombre = input("Nombre:")
apellido = input("Apellido:")
cedula = input("Cedula:")
if not (cedula.isnumeric()):
    print("El dato no es valido, reinicie el programa")
else:
    peso = input("Peso:")
    if (peso.isnumeric()) or (peso.count(".")==1):
        estatura = input("Estatura:")
        if (estatura.isnumeric()) or (estatura.count(".")==1):
            deporte = input("Deporte favorito:")
            notas = input("Ultimo promedio de calificaciones:")
            if (notas.isnumeric()) or (notas.count(".")==1):
                print(f"""Gracias, sus datos han sido recopilados y son los siguientes:
                Su nombre es {nombre}
                Su apellido es {apellido}
                Su cedula es {cedula}
                Su peso es {peso} Kg
                Su estatura es {estatura} M
                Su indice de masa corporal es {float(peso) / float(estatura) ** 2}
                Su deporte favorito es el {deporte}
                Y su ultimo promedio de notas fue de {notas}""" )
            else:
                print("El dato no es valido,reinicie el programa")
        else:
            print("El dato no es valido,reinicie el programa")
    else:
        print("El dato no es valido,reinicie el programa")
    
        

        
    
    
    
    