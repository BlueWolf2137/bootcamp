# to jest komentarz
"""
Utwórz zmienne, a i b, przypisz im wartości liczbowe


utworz zmienna
Pole prostokąta i przypisz do niej formułę licząca te pole
pole prostokata o bokach 2 i 4 wynosi:8

Wypisz tekst na konsoli dokładnie jak poniżej
"to jest tekst w cudzysłowie"


ctrl/ zamienia linie w komentarze

ctrl+alt+l = dostosowanie kodu
"""
a = 2
b = 4
pole_prostokata = a * b
print(f"pole prostokata o bokach {a},{b} wynosi:{pole_prostokata}")

print('"to jest tekst w cudzysłowie"')
# print('"to jest\n tekst w cudzysłowie"')
# print('"to jest\n tekst w \ncudzysłowie"')

a = input("Podaj bok a")
a = int(a)
b = input("Podaj bok b")
b = int(b)
pole_prostokata = a * b
print(f"pole prostokata o bokach {a},{b} wynosi:{pole_prostokata}")
