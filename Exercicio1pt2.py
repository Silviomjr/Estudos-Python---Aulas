import sys
try: 
    a= float (input ('Valor de A: '))
    b= float (input ('Valor de B: '))
    c= float (input ('Valor de C: '))
except :
    print ("Campo  e diferente de 0, favor corrigir")
    sys.exit()

delta = (b**2) - (4*a*c)

if (delta) < 0 :
    print ("Δ é menor que zero - Equação não possui raízes reais")
else :
    print ("Δ possui raizes reais")
    x1 = (-b + (delta**0.5)) / (2*a)
    x2 = (-b - (delta**0.5)) / (2*a)
    print ("Raiz 1: " , x1, "\nRaiz 2: " , x2)