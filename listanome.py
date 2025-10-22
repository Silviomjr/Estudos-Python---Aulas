ListaNome = ['marquard', 'zhen', 'cwen', 'csev', 'zhen','MARQUARD', 'Marquard']

dicionarioContagem = dict()

# Loop para contar a ocorrência de cada nome na lista
for nome in ListaNome:
    #Adicionar Lower
    nome = nome.lower()
    #Verficar se o nome já está no dicionário
    if nome not in dicionarioContagem:
        dicionarioContagem[nome] = 1
    else:
        dicionarioContagem[nome] += 1
#Printar o dicionário com as contagens
print(dicionarioContagem)