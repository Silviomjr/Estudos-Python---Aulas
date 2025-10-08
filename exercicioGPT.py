def busca(lista, nome):
    if nome in lista:
        posicao = lista.index(nome) + 1
        return f"{nome} está na lista na posição {posicao}."
    else:
        return f"{nome} não está na lista."

entradas = []

while True:
    entrada = input("Digite um nome ou sair ").strip()
    if entrada.lower() == "sair":
        break
    entradas.append(entrada)

buscaNome = input("Digite o nome que deseja buscar: ").strip()
resultado = busca(entradas, buscaNome)
print(resultado)

