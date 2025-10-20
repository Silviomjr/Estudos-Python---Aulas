ListaNome = ['marquard', 'zhen', 'cwen', 'csev', 'zhen','MARQUARD', 'Marquard']

dicionarioContagem = dict()

# Loop para contar a ocorrência de cada nome na lista
for nome in ListaNome:
    #Adicionar Lower
    nome = nome.lower()

    if nome not in dicionarioContagem:
        dicionarioContagem[nome] = 1
    else:
        dicionarioContagem[nome] += 1

print(dicionarioContagem)