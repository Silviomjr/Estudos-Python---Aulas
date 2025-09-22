import os
import sys

#file = open('C:\Projetos\Exercicios 1\SilvioAula.txt', 'r')
file = open('SilvioAula.txt', 'r')
mypath = os.path.abspath(os.path.dirname(__file__))

paragraphs = file.read().split('\n')
paragraphsWithoutSpaces = []

for line in paragraphs:
    if(line != ''):
        paragraphsWithoutSpaces.append(line)
    
print(len(paragraphsWithoutSpaces))
print(len(paragraphs))

file.close()
#print(file.read())
#file.close()