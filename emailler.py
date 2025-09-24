import os
import sys

file = open('C:\Projetos\Exercicios 1\Email.txt', 'r')
#file = open("Email.txt", "r")
#mypath = os.path.abspath(os.path.dirname(__file__))+'\Email.txt'
#print(mypath)
emails = [] 

for palavra in file:
    if "vale" in palavra.lower():
        emails.append(palavra)

print(emails)
file.close()