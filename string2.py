numeros = '1 2 3 4 5 6 46 87 94 64 8974 11 512 23 1 68 7 4 2 0 56 6 5'
letras = ' '

substituir = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D', 
    '5': 'E',
    '6': 'F',  
    '7': 'G',
    '8': 'H', 
    '9': 'I',
    '0': 'J',
    '' : ''
}

for numero in numeros:
    letras += substituir.get(numero, numero)

print(letras)

#Minha Resposta
#for numero in numeros:
#    letras = letras.replace('1', 'A')
#    letras = letras.replace('2', 'B') 
#    letras = letras.replace('3', 'C')
#    letras = letras.replace('4', 'D')
#    letras = letras.replace('5', 'E')
#    letras = letras.replace('6', 'F')
#    letras = letras.replace('7', 'G')
#    letras = letras.replace('8', 'H')
#    letras = letras.replace('9', 'I')
#    letras = letras.replace('0', 'J')
#print(letras)

 