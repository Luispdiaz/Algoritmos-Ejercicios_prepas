print("Hola, por favor ingrese sus siguientes datos personales: \n")
dato1 = input("Nombre: ")
if (dato1.isnumeric()):
    print("El dato no es valido, reinicie el programa")    
else:
    dato7 = input("Apellido: ")
    if (dato7.isnumeric()):
        print("El dato no es valido, reinicie el programa")    
    else:
        dato8 = input("Deporte favorito: ")
        if (dato8.isnumeric()):
            print("El dato no es valido, reinicie el programa")
        else:
            dato2 = input("Cedula: ")
            if (not dato2.isnumeric()): 
                print("El dato no es valido, reinicie el programa")
            else:
                dato3 = input("Estatura (cm): ")
                if (not dato3.isnumeric()):
                    print("El dato no es valido, reinicie el programa")
                else:
                    dato4 = input("Peso: ")
                    if (not dato4.isnumeric()): 
                        print("El dato no es valido, reinicie el programa")
                    else:
                        dato5 = input("Ultimo promedio de calificaciones: ")
                        if (not dato5.isnumeric()): 
                            print("El dato no es valido, reinicie el programa")
                        else:
                            print(f""" Sus datos personales son los siguientes:
                            Su nombre es {dato1}
                            Su Apellido es {dato7}
                            Su Deporte Favorito es {dato8}
                            Su Cedula es {dato2}
                            Su Estatura es {dato3} cm
                            Su Peso es {dato4} Kg
                            Su ultimo promedio de calificaciones fue {dato5} """)
