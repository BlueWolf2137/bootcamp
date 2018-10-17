a = float(input("Bok opakowania:"))
b = float(input("Głębokość opakowania:"))
h = float(input("wysokość opakowania:"))
c = a*b*h
print()
if c> 1000:
    print(f"W opakowaniu zmieści się więcej niż 1000 ml")
else:
    print(f"W opakowaniu nie zmieści się 1000 ml")
print()
print(f"w opakowaniu mieści się {c} ml")


