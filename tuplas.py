my_dict = {'apple': 2, 'banana': 3, 'orange': 1, 'grape': 4, 'kiwi': 2}

#VaLores Crescentes
sorted_items_asc = sorted(my_dict.items(), key=lambda item: item[1])
sorted_dict_asc = dict(sorted_items_asc)
print("Dicionário ordenado em ordem crescente:", sorted_dict_asc)

#Valores Descrescentes
sorted_items_desc = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
sorted_dict_desc = dict(sorted_items_desc)
print("Dicionário ordenado em ordem decrescente:", sorted_dict_desc)