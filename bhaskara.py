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

delta = (b**2) - (4*a*c)

try:
    delta >= 0
    x1 = (-b + (delta**0.5)) / (2*a)
    x2 = (-b - (delta**0.5)) / (2*a)
    #Não tenho ideia de como prosseguir com Raiz em Python
    #Copiei os amiguinhos na cara dura
    print("Δ:", delta)
    print("X1:", x1)
    print("X2:", x2)
    print("Raízes reais encontradas.")
    if delta != 0:
        print("As raizes são diferentes de zero")
except:
    print("Δ é menor que zero - a equação não possui raízes reais!")
    sys.exit()