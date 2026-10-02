import random
opcion = int(input("elige piedra(1),papel(2) o tijera(3): "))
eleccion = ["piedra","papel","tijera"]
print("Tú elegiste: " + eleccion[opcion - 1])

     
aleatorio = random.randrange(1,4)
print("La Computadora eligio: " + eleccion[aleatorio - 1])

    
if opcion == 1 or opcion == 2 or opcion == 3:
    if opcion == 1 and aleatorio == 3:
        resultado = "¡Ganaste!"
    elif opcion == 2 and aleatorio == 1:
        resultado = "¡Ganaste!"
    elif opcion == 3 and aleatorio == 2:
        resultado = "¡Ganaste!"
    elif opcion == 3 and aleatorio == 1:
        resultado = "¡Perdiste!"
    elif opcion == 1 and aleatorio == 2:
        resultado = "¡Perdiste!"
    elif opcion == 2 and aleatorio == 3:
        resultado = "¡Perdiste!"
    else:
        resultado = "¡Empate!"
    print(resultado)
    
    
else:
    print("¡Opcion no valida!")