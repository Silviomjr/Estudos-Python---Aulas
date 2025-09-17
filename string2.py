numeros = '1 2 3 4 5 6 46 87 94 64 8974 11 512 23 1 68 7 4 2 0 56 6 5'
letras = ' '

#substituir = {
#    '1': 'A',
#    '2': 'B',
#    '3': 'C',
#    '4': 'D', 
#    '5': 'E',
#    '6': 'F',  
#    '7': 'G',
#    '8': 'H', 
#    '9': 'I',
#    '0': 'J',
#    '' : ''
#}

#for numero in numeros:
#    letras += substituir.get(numero, numero)

#print(letras)


#Minha Resposta
#for numero in numeros:
#    letras = numero.replace('1', 'A')
#    letras = numero.replace('2', 'B') 
#    letras = numero.replace('3', 'C')
#    letras = numero.replace('4', 'D')
#    letras = numero.replace('5', 'E')
#    letras = numero.replace('6', 'F')
#    letras = numero.replace('7', 'G')
#    letras = numero.replace('8', 'H')
#    letras = numero.replace('9', 'I')
#    letras = numero.replace('0', 'J')
#print(letras)

arrNumeros = numeros.split(' ')

print(arrNumeros)

for numero in arrNumeros:
    if(numero == '1'):
        letras = letras + 'A'
    elif(numero == '2'):
        letras = letras + 'B'
    elif(numero == '3'):
        letras = letras + 'C'
    elif(numero == '4'):
        letras = letras + 'D'
    elif(numero == '5'):
        letras = letras + 'E'
    elif(numero == '6'):
        letras = letras + 'F'
    elif(numero == '7'):
        letras = letras + 'G'
    elif(numero == '8'):
        letras = letras + 'H'
    elif(numero == '9'):
        letras = letras + 'I'
    elif(numero == '0'):
        letras = letras + 'J' 
    elif(numero == ''):
        letras = letras + ''
    else:
        letras = letras + numero + " "

print(letras)
