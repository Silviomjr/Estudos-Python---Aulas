word = 'banana'
count = 0
for index, letter in enumerate (word) :
    is_anagram = word[index: index + 3]
    if is_anagram == 'ana' :
        count = count + 1
print ("Existe: ", count, "anagrama(s)")