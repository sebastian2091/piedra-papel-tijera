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
        resultado = "¡Ganaste!"
    elif eleccion == 2 and aleatorio == 1:
        resultado = "¡Ganaste!"
    elif eleccion == 3 and aleatorio == 2:
        resultado = "¡Ganaste!"
    elif eleccion == 3 and aleatorio == 1:
        resultado = "¡Perdiste!"
    elif eleccion == 1 and aleatorio == 2:
        resultado = "¡Perdiste!"
    elif eleccion == 2 and aleatorio == 3:
        resultado = "¡Perdiste!"
    else:
        resultado = "¡Empate!"
    print(resultado)
else:
    print("¡Opcion no valida!")