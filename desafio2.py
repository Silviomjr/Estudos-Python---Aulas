contAna = 0


for index, letra in enumerate(palavra):
    anagrama = palavra[index: index + 3]
    if anagrama == 'ana':
        print(f'áchei {anagrama} na ')
        contAna = contAna + 1

print(contAna)
        