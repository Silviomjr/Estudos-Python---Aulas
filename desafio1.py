import math

try:
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    if a < 0:
        print("Δ é menor que zero - a equação não possui raízes reais!")
    else:
        delta = (b * b) - 4 * a * c
        x1 = (-b + math.sqrt(delta)) / 2
        x2 = (-b - math.sqrt(delta)) / 2
        print("Delta: ", delta)
        print("Primeira raiz: ", x1)
        print("Segunda raiz: ", x2)
except ValueError:
    print("Valor digitado é invalido!")
        


