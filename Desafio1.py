from sys import exit
import numpy
from math import sqrt

try:
    a= float(input('Qual o valor de a?: '))
    b= float(input('Qual o valor de b?: '))
    c= float(input('Qual o valor de c?: '))
except:
    print("Erro: Por favor, insira valores numéricos válidos.")
    exit()



delta = b**2 - (4 * a * c)
if delta >= 0: # Tentar executar a parte do cálculo das raízes apenas se o delta for maior do que zero.
    xtest = sqrt(delta)
    print("delta é igual: " , delta)
    x1 = (-b + (delta ** 0.5))/ (2 * a)
    print('x1=', x1)
    x2 = (-b - (delta ** 0.5))/ (2 * a)
    print('x2= ', x2)

    Bhaskara1 = (a * x1**2) + (b * x1) + c
    print('Bhaskara1= ' , Bhaskara1)
    Bhaskara2 = (a * x2**2) + (b * x2) + c
    print('Bhaskara2= ' , Bhaskara2)
else:
    print("delta é menor que zero - a equação não possui raízes reais!")