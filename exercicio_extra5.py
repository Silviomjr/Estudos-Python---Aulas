# Tarefa 1: Proteção contra divisão por zero
dividendo = 100.50
divisor = 2

try:
    calculo = dividendo / divisor
    print(f"{dividendo}/{divisor}= {calculo}")

except ZeroDivisionError:
    print("Não é possível dividir por zero")

# Tarefa 2: Conversão para inteiro
entrada_usuario = "123"

try:
    entrada_usuario = int(entrada_usuario)
    print("Tipo: ", type(entrada_usuario))
    print("entrada usuario: ", entrada_usuario)
except ValueError:
    print("Formato de número inválido")

# Tarefa 3: Acesso a índice de lista
numeros = [10, 20, 30]

try:
    indice = 0

    print(f"Valor do indice {indice}: ", numeros[indice])
except IndexError:
    print("Indice fora do alcance")

# Tarefa 4: Simulação de operação com arquivo

arquivo = "arquivoInexistente.txt"
try:
    open(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")

# Tarefa 5: Tratamento de múltiplas exceções
entrada = "200"

try:
    entrada = float(entrada)
    print("Tipo: ", type(entrada))
    print("entrada usuario: ", entrada)
except ValueError:
    print("Formato de número inválido")



try:
    calculo = entrada / 100
    print(f"{entrada}/100= {calculo}")

except ZeroDivisionError:
    print("Não é possível dividir por zero")


resultado  = [5, 15, 100, 200, 1234, 1500]

try:
    i = 0

    print(f"Valor do indice {i}: ", resultado[i])
except IndexError:
    print("Indice fora do alcance")