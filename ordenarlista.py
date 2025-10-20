lista = [64, 34, 25, 12, 22, 11, 90, 5]
ordenada = sorted(lista, reverse = True)
print("Lista original:", lista)
print("Lista ordenada:", ordenada)

def acharMaior (listaSuporte):
    maior = listaSuporte[0]
    for i in range(1, len(listaSuporte)):
        if listaSuporte[i] > maior:
            maior = listaSuporte[i]
    return maior
print("O maior valor da lista é:", acharMaior(lista))

def funcaoOrdenar(lista):
    listaOrdenada = []
    listaCopia = lista.copy()
    for x in range(len(lista)):
        maiorvalor = acharMaior(listaCopia)
        listaOrdenada.append(maiorvalor)
        indexDeOcorrencia = listaCopia.index(maiorvalor)
        listaCopia.pop(indexDeOcorrencia)
    return listaOrdenada
print("Lista ordenada pela função:", funcaoOrdenar(lista))