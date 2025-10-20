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
        listaOrdenada.append(maior)
        indexDeOcorrencia = listaCopia.index(maiorvalor)
        listaCopia.pop(indexDeOcorrencia)
    return listaOrdenada
print("Lista ordenada pela função:", funcaoOrdenar(lista))


# lista = [64, 34, 25, 12, 22, 11, 90, 5]

# def double_selection_sort(lst):
#     start = 0
#     end = len(lst) - 1
#     while start < end:
#         min_idx = start
#         max_idx = start
#         for i in range(start, end + 1):
#             if lst[i] < lst[min_idx]:
#                 min_idx = i
#             if lst[i] > lst[max_idx]:
#                 max_idx = i
#         lst[start], lst[min_idx] = lst[min_idx], lst[start]
#         # Corrige o índice do maior se ele foi trocado
#         if max_idx == start:
#             max_idx = min_idx
#         lst[end], lst[max_idx] = lst[max_idx], lst[end]
#         start += 1
#         end -= 1

# lista_copia = lista.copy()
# double_selection_sort(lista_copia)
# print("Lista original:", lista)
# print("Lista ordenada:", lista_copia)

# for i in lista:
#     for x in range(i+1, len(lista)):
#         if lista[i] > lista[x]:
#             lista[i], lista[x] = lista[x], lista[i]