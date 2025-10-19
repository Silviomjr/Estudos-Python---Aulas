lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 29]
print ('lista:', lista)
procurar = input ("O que você quer procurar?")
try:
    elemento = int(procurar)
    print(elemento in lista)
except:
    print("você não digitou valor válido")
    exit()

