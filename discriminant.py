from math import sqrt, pow

a, b, c = float(input()), float(input()), float(input())
D = pow(b, 2) - 4 * a * c
x1 = (-b - (D**0.5)) / (2 * a)
x2 = (-b + (D**0.5)) / (2 * a)
if D > 0:
    print(min(x1, x2), max(x1, x2), sep="\n")
elif D == 0:
    print(-b / (2 * a))
else:
    print("Нет корней")
