numeros = '1 2 3 4 5 6 46 87 94 64 8974 11 512 23 1 68 7 4 2 0 56 6 5'
letras = ' '

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
