a = input ('Valor de A: ')
b = input ('Valor de B: ')
c = input ('Valor de C: ')

if type(a and b and c) == int :
    print ("Calculando...")
else :
    print ("Campo numerico, favor corrigir")

delta = (b**2) - (4*a*c)
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

if (delta) > 0 :
    print ("Δ é menor que zero - Equação não possui raízes reais")
else :
    print (x1) and print (x2)