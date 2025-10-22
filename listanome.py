listaNome = ['marquard', 'zhen', 'cwen', 'csev', 'zhen','MARQUARD', 'Marquard']

# Loop para contar a ocorrência de cada nome na lista

def  count_nome(lista):

    dicionarioContagem = dict()

    for nome in lista:
        #Adicionar Lower
        nome = nome.lower()
        #Verficar se o nome já está no dicionário
        if nome not in dicionarioContagem:
            dicionarioContagem[nome] = 1
        else:
            dicionarioContagem[nome] += 1
#Printar o dicionário com as contagens
    return dicionarioContagem

print(count_nome(listaNome))

