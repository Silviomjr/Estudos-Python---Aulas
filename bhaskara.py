import sys

a = input("Digite a: ")
b = input("Digite b: ")
c = input("Digite c: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print("Insira Numeros Validos")
    sys.exit()

if a == 0:
    print("Não é uma equaçao de segundo grau")
    sys.exit()
else:

    delta = (b**2) - (4*a*c)

    if delta >= 0:
        x1 = (-b + (delta**0.5)) / (2*a)
        x2 = (-b - (delta**0.5)) / (2*a)

        print("Δ:", delta)
        print("X1:", x1)
        print("X2:", x2)
        print("Raízes reais encontradas.")
    else:
        print("Delta é menor que zero, equação não possui raizes reais.")