def ahorcado():
    palabra = "Andrea"
    adivinacion_equivocada = 0
    pasos = ["","________  ","|    |    ","|    0","|   /|\    ","|   / \   ","|     "]
    letras_izquierda = list(palabra)
    puntuacion_tablero = ["___"]* len(palabra)
    ganar = False
    print("Bienvenido al Ahorcado")

    while adivinacion_equivocada < len(pasos) -1:
        print("\n")
        adivina = input("Adivina un letra ")
        if adivina in letras_izquierda:
            caracter_indice = letras_izquierda.index(adivina)
            puntuacion_tablero[caracter_indice] = adivina
            letras_izquierda[caracter_indice] = "$"
        else:
            adivinacion_equivocada += 1
            print("".join(puntuacion_tablero))
            print("\n".join(pasos[0:adivinacion_equivocada +1]))
        if "___" not in puntuacion_tablero:
            print("Ganaste! La palabra era {}".format(palabra))
            print("".join(puntuacion_tablero))
            ganar = True
            break
    if not ganar:
        print("\n".join(pasos[0:adivinacion_equivocada + 1]))
        print("Perdiste! La palabra era {}".format(palabra))

ahorcado()
