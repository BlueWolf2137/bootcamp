x = int(input("Podaj pierwsza współżędną: "))
y = int(input("Podaj drugą współżędną: "))
if x <= 10 and y <= 10:
    print("Pozycja gracza to lewy dolny róg.")
elif (x > 100 or y > 100) and (x < 100 or y >100) and (x > 100 or y < 100):
    print("Gracz znajduje sie poza planszą")
elif x > 10 and x <= 90 and y <= 10:
    print("Pozycja gracza to dolna krawędź.")
elif x > 90 and y <= 10:
    print("Pozycja gracza to prawy dolny róg.")
elif x <= 10 and y > 10 and y <= 90:
    print("Pozycja gracza to lewa krawędź.")
elif x > 90 and y > 10 and y <= 90:
    print("Pozycja gracza to prawa krawędź.")
elif x <= 10 and y > 90:
    print("Pozycja gracza to lewy górny róg.")
elif x > 10 and x <= 90 and y > 10:
    print("Pozycja gracza to górna krawędź.")
elif x > 90 and y > 10:
    print("Pozycja gracza to prawy górny róg.")

else:
    print("Gracz znajduje się w pozycji centralnej.")