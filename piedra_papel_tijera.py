import random
eleccion = int(input("elige piedra(1),papel(2) o tijera(3): "))

if eleccion == 1 or eleccion == 2 or eleccion == 3:
    if eleccion == 1:
        print("Tú elegiste: piedra")
    elif eleccion == 2:
        print("Tú elegiste: papel")
    elif eleccion == 3:
        print("Tú elegiste: tijera")
     

     
    aleatorio = random.randrange(1,4)
    if aleatorio == 1:
        print("Computadora eligió: piedra")
    elif aleatorio == 2:
        print("Computadora eligió: papel")
    elif aleatorio == 3:
        print("Computadora eligió: tijera")
    

    if eleccion == 1 and aleatorio == 3:
        print("¡Ganaste!")
    elif eleccion == 2 and aleatorio == 1:
        print("¡Ganaste!")
    elif eleccion == 3 and aleatorio == 2:
        print("¡Ganaste!")
    elif eleccion == 3 and aleatorio == 1:
        print("¡Perdiste!")
    elif eleccion == 1 and aleatorio == 2:
            print("¡Perdiste!")
    elif eleccion == 2 and aleatorio == 3:
            print("¡Perdiste!")
    else:
        print("¡Empate!")
else:
    print("¡Opcion no valida!")