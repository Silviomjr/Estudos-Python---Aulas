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

def raiz(valor1):
    if valor1 < 0:
        print("Raiz quadrada de numero negativo não existe")
        return
    resultado = valor1 ** 0.5
    return resultado



def bhaskara(a, b ,c):

    primeirotermo = mult(b,b)
    segundotermo = mult(4, mult(a,c))
    delta = sub(primeirotermo, segundotermo)
 

    if delta >= 0:

        primeiroTermo = raiz(delta)
        segundoTermo = mult(2,a)
        terceiroTermo = divisao(primeirotermo, segundoTermo)
        quartoTermo = soma(-b, terceiroTermo)
        quintoTermo = sub(-b, terceiroTermo)
        x1 = quartoTermo
        x2 = quintoTermo
        print("Δ:", delta)
        print("X1:", x1)
        print("X2:", x2)
        print("Raízes reais encontradas.")
    else:
        print("Delta é menor que zero, equação não possui raizes reais.")


a = input("Digite a: ")
b = input("Digite b: ")
c = input("Digite c: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print("Insira Numeros Validos")
    sys.exit()
    
bhaskara(a, b, c)