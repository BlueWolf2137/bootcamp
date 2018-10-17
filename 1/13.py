dzien = d = 1
suma  = 0
a = int(input(f"ilość dni:"))
while d < 7:

    t = (int(input(f"Podaj temperaturę dnia {d}: ")))
    d = d + 1
    suma = suma + t
sr = suma / a


print(f"Średnia temperatura w tym tygodniu wynosiła = {sr}")

