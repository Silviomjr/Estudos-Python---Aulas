a= int(input('Qual o valor de a?: '))
b= int(input('Qual o valor de b?: '))
c= int(input('Qual o valor de c?: '))
Δ = b**2 - (4 * a * c)
if Δ > 0:
    print("Δ é igual: " , Δ)
else:
    print("Δ é menor que zero - a equação não possui raízes reais!")

x1 = (-b + (Δ ** 0.5))/ (2 * a)
print('x1=', x1)
x2 = (-b - (Δ ** 0.5))/ (2 * a)
print('x2= ', x2)

Bhaskara1 = (a * x1**2) + (b * x1) + c
print('Bhaskara1= ' , Bhaskara1)
Bhaskara2 = (a * x2**2) + (b * x2) + c
print('Bhaskara2= ' , Bhaskara2)