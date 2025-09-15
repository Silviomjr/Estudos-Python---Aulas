string = 'X-DSPAM-Confidence: 0.8475'

apos = string.find(':')
apos = string[apos + 1:]
apos = float(apos)
print(apos)


string2 = '   Olá Mundo   '
string2 = string2.strip()
print(string2)

string3 = 'Olá Silvio Silvio Silvio'
string4 = string3.replace('Silvio', 'Rafael')
print(string3)
print(string4)