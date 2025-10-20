def busca(lista, nome):
    listaCopia = []
    for index in range(len(lista)):
        listaCopia.append(lista[index].lower())

    if nome.lower() in listaCopia:
        posicao = listaCopia.index(nome.lower()) + 1
        return f"{nome} está na lista na posição {posicao}."
    else:
        return f"{nome} não está na lista."

entradas = []

while True:
    entrada = input("Digite um nome ou sair ").strip()
    if entrada.lower() == "sair":
        break
    entradas.append(entrada.lower())

buscaNome = input("Digite o nome que deseja buscar: ").strip()
resultado = busca(entradas, buscaNome)
print(resultado)

