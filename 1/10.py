a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = input("Podaj rodzaj operacji: ")


if int(c == "/") and b == 0:
   print("Nie można wykonać obliczeń.")
elif int(c == "+"):
   w = a + b
   print(f"Wynik: {w}")
elif int(c == "-"):
   w = a - b
   print(f"Wynik: {w}")
elif int(c == "*"):
   w = a * b
   print(f"Wynik: {w}")
elif int(c == "/"):
   w = a / b
   print(f"Wynik: {w}")
else:
    print("Błędne dane")

