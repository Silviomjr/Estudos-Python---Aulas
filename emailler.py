import os
import sys

file = open('C:\Projetos\Exercicios 1\Email.txt', 'r')
#file = open("Email.txt", "r")
#mypath = os.path.abspath(os.path.dirname(__file__))

for palavra in file.read().split():
    if "@br.ey.com" in palavra:
        print(palavra)
    else:
        print("Não é um email")
    
print(file.read())
file.close()