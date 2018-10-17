from  random import randint

graczX = randint(1,10)
graczY = randint(1,10)
skarbX = randint(1,10)
skarbY = randint(1,10)



print(f"szerokość na mapie:{graczX}")
print(f"wysokośc na mapie:{graczY}")
print(f"szerokość na mapie skarb:{skarbX}")
print(f"wysokośc na mapie skarb:{skarbY}")
while True:

    gracz = input("Podaj kierunek:")

    minkrokowprzed = abs(skarbX - graczX) + abs(skarbY -graczY)


    if gracz == "w":
        graczX = graczX + 1
    if gracz == "s":
        graczX = graczX - 1
    if gracz == "a":
        graczY = graczY - 1
    if gracz == "d":
        graczY = graczY + 1

    minkrokowpo = abs(skarbX - graczX) + abs(skarbY - graczY)

    print(f"szerokość na planszy:{graczX} wyskokość na planszy:{graczY}")
    print(f"minimalna ilość kroków do celu:{minkrokowprzed}")

    if 1 > graczX or graczX > 10 or 1 > graczY or graczY >10:
        print("wypadłeś z planszy")
        break

    if 1 > graczX or graczX >10 or 1 > graczY or graczY >10:
        print("wypadłeś z planszy")
        break

    if skarbX == graczX and skarbY == graczY:
        print("znalazłeś skarb")
        break

    if skarbX == graczX:
        print("skarb znajduje się na tej samej wysokości")
    if skarbY == graczY:
        print("Skarb znajduje się na tej samej szerokości")

    if skarbX == graczX and skarbY == graczY:
        h = minkrokowprzed+ minkrokowpo
        print(f"gracz wykonał{h} kroków")


