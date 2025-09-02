import math

try:
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
except ValueError:
    print("Valor digitado é invalido!")


if a == 0:
    print("Não é uma equação de segundo gau")
else:
    delta = b**2 - (4 * a * c)
        
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / 2
        x2 = (-b - math.sqrt(delta)) / 2
        print("Delta: ", delta)
        print("Primeira raiz: ", x1)
        print("Segunda raiz: ", x2)
    else:
        print("Delta é menor que zero, equação não possui raizes reais.")
        


