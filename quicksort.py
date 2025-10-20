lista = [64, 34, 25, 12, 22, 11, 90, 5]

def acharMenor(listaSuporte):
    menorValorLista = float('inf')
    for i in listaSuporte:
        if i < menorValorLista:
            menorValorLista = i
    return menorValorLista

def acharMaior(listaSuporte):
    maiorValorLista = float('-inf')
    for i in listaSuporte:
        if i > maiorValorLista:
            maiorValorLista = i
    return maiorValorLista

def funcaoOrdenarLista(listaDaFuncao):
    listaOrdenada = []
    listaOrdenadaDesc = []

    listaCopia = listaDaFuncao.copy()
    listaCopia2 = listaDaFuncao.copy()

    for item  in range(len(listaDaFuncao)):
        menorValorListaOriginal = acharMenor(listaCopia)
        maiorValorListaOriginal = acharMaior(listaCopia2)

        listaOrdenada.append(menorValorListaOriginal)
        listaOrdenadaDesc.insert(len(listaOrdenadaDesc), maiorValorListaOriginal)
        #listaOrdenadaDesc.insert(0, menorValorListaOriginal)
        indexDeOcorrencia  = listaCopia.index(menorValorListaOriginal)
        indexDeOcorrencia2 = listaCopia2.index(maiorValorListaOriginal)

        listaCopia.pop(indexDeOcorrencia)
        listaCopia2.pop(indexDeOcorrencia2)

        #maior = acharMaior(lista)
        #listaOrdenadaDesc.append(maior)
        #lista.remove(maior)

    return print("Lista  Ordenada Crescente" , listaOrdenada), print("\nLista Ordenada Descrescente", listaOrdenadaDesc)


funcaoOrdenarLista(lista)