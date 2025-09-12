palavra = 'banana'
#contar = palavra.split("ana")
#total = len(contar)
#print(total)

count = 0
for index, letra in enumerate(palavra):
    anamagrama = palavra[index: index + 3]
    if anamagrama.lower() == 'ana':
        print(f"Achei {anamagrama} na posição {index}")
        count = count + 1

print(count)