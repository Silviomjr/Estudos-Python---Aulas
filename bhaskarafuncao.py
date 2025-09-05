import sys

def bhaskara(valor1, valor2 ,valor3):
    delta = (valor2**2) - (4*valor1*valor3)

    if delta >= 0:
        x1 = (-valor2 + (delta**0.5)) / (2*valor1)
        x2 = (-valor2 - (delta**0.5)) / (2*valor1)
        print("Δ:", delta)
        print("X1:", x1)
        print("X2:", x2)
        print("Raízes reais encontradas.")
    else:
        print("Delta é menor que zero, equação não possui raizes reais.")


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
bhaskara(a, b, c)