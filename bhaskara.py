a = input("Digite a: ")
b = input("Digite b: ")
c = input("Digite c: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print("Insira Numeros validos")

delta = (b**2) - (4*a*c)

try:
    delta > 0
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)
    #Não tenho ideia de como prosseguir com Raiz em Python
    print("Δ:", delta)
    print("X1:", x1)
    print("X2:", x2)
    print("Raízes reais encontradas.")
except:
    print("Δ é menor que zero - a equação não possui raízes reais!")