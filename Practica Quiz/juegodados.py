bienvenida = "Bienvenidos al juego de los dados"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
aux=False
while aux==False:
    print("Elija un avatar:\n *1. Jugador 1 \n *2. Jugador 2")
    avatar = input("--->")
    if avatar == "1":
        print("A jugar jugador 1")
    elif avatar == "2":
        print("A jugar jugador 2")
    else:
        print("El dato que ha ingresado no es valido")
    dado = input("Pulsa 1 para lanzar los dados:")
    listdado = [1 , 2 , 3 , 4 , 5 , 6]
    import random 
    result = 0
    acum = 0
    if dado == "1":
        for i in range(1,9):
            dado2 = random.choice(listdado)
            result[i] = result
            if dado2 == 1:
                result= result + 10
            elif dado2 == 2:
                result= result + 20
            elif dado2 == 3:
                continue
            elif dado2 == 4:
                result= result * 2
            elif dado2 == 5:
                result= result + 40
            elif dado2 == 6:
                result = result / 2
            print(f"El dado ha marcado {dado2} y su puntuacion es de {result}")
    else:
        print("El dato ingresado no es valido")
    print(f"Su puntuacion final es de {acum}")
    print("Turno de su rival")
    result1 = 0
    for i in range(1,9):
        random.choice(listdado)
        if random.choice(listdado) == 1:
            result1+=10
        elif random.choice(listdado) == 2:
            result1+=20
        elif random.choice(listdado) == 3:
            continue
        elif random.choice(listdado) == 4:
            result1*=2
        elif random.choice(listdado) == 5:
            result1+=40
        else:
            result1 = result1 / 2
        print(f"El dado ha marcado {random.choice(listdado)} y su puntuacion es de {result1}")
    if avatar == "1":
        print(f"La puntuacion final del jugador 2 es de {result1}")
    elif avatar == "2":
        print(f"La puntuacion final del jugador 1 es de {result1}")
    if result < result1:
        print("Usted ha perdido")
    elif result > result1:
        print("Usted ha ganado")
    else:
        print("Han empatado")
    print("Gracias por jugar")
    variable = input("Si no quiere seguir jugando presione 1, en su defecto ingrese otro numero:")        
    if variable == "1":
        aux=True

        



