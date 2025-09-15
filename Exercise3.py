str_value = 'X-DSPAM-Confidence: 0.8475'
colonpos = str_value.find (':') # encontrar a posição do caractere ':'
host = str_value[colonpos+1:].strip() # pega a substring após ':' e remove espaços em branco
strtofloat = float(host) # converte a string para float
print (strtofloat)