import sys

def soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def sub(valor1, valor2):
    resultado = valor1 - valor2
    return resultado

def mult(valor1, valor2):
    resultado = valor1 * valor2
    return resultado

def divisao(valor1, valor2):
    if valor2 == 0:
        print("Divisão por zero não é permitida.")
        return
    resultado = valor1 / valor2
    return resultado

def raiz(valor):
    if valor < 0:
        print("Raiz quadrada de numero negativo não existe")
        return
    resultado = valor ** 0.5
    return resultado

a = input("Digite Valor 1: ")
b = input("Digite Valor 2: ")

try:
    a = float(a)
    b = float(b)
except:
    print("Insira Numeros Validos")
    sys.exit()

resultadoSoma = soma(a, b)
print("Soma:", resultadoSoma)

resultadoSub  = sub(a, b)
print("Subtração:", resultadoSub)

resultadoMult = mult(a, b)
print("Multiplicação:", resultadoMult)

resultadoDiv = divisao(a, b)
print("Divisão:", resultadoDiv)

resultadoRaiz = raiz(a)
print("Raiz Quadrada de", a, "é:", resultadoRaiz)