
print("Bienvenido a la isla, tu misión será encontrar el tesoro")
print("hay 2 caminos")

camino= input("Derecha o Izquierda ? (D/I)") .upper()
if camino == ("I"):
    print(" te encuentras un lago")
    noe= input ("Nadar o Esperar ? (N/E)").upper()
    if noe =="E":
        print("ves una cabaña, entras y ves varias puertas")

        puerta=input("Cual puerta? Roja-Azul-Verde  (R/A/V)").upper()
        if puerta=="A":
            print("Haz ganado, FELICIDADES")
        elif puerta=="R":
             print("eres quemado, GAME OVER")
        elif puerta=="V":
            print("eres devorado por bestias, GAME OVER")
        else :
            print("elije una de las opciones que se te pide")
            print("vuelve a empezar")
            exit()

    if noe =="N":
        print("atacado por una tribu, GAME OVER")
if camino == "D":
        aoa= input("Arriba o Abajo ? (ARRIBA/ABAJO)").upper()
        if aoa== ("ARRIBA"):
            print("atacado por una tribu, GAME OVER")
        elif aoa == ("ABAJO"):
            print("caiste en un agujero, GAME OVER")
    
