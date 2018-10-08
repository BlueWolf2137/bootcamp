a = input('Miasto A')
b = input("Miasto B")
c = int(input("Dystans między miastami:"))
d = float(input("Cena paliwa:"))
e = float(input("Spalanie na 100km:"))
f = round(((c/100) * e) * d)
print()

print(f"Miasto A:{a}\nMiasto B:{b}\nDystans między{a}{b}:{c}\nCena paliwa:{d}\nSpalanie na 100km:{e}\nKoszt przejazdu {a}-{b} wynosi {f} PLN")