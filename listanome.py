listaNome = ['marquard', 'zhen', 'cwen', 'csev', 'zhen','MARQUARD', 'Marquard']

# Loop para contar a ocorrência de cada nome na lista

def  count_nome(lista):
    #Instanciar Variavel de dicionario vazio na função
    dicionarioContagem = dict()

    for nome in lista:
        #Adicionar Lower
        nome = nome.lower()
        #Verficar se o nome já está no dicionário
        if nome not in dicionarioContagem:
            #Adiciona a primeira vez no dict() vazio
            dicionarioContagem[nome] = 1
        else:
            #Faz a contagem +1
            dicionarioContagem[nome] += 1
#Printar o dicionário com as contagens
    return dicionarioContagem

#Chamar Função printando listaNome original
print(count_nome(listaNome))

