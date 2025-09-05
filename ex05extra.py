dividendo = 10
divisor = 2

try:
    resultado = dividendo / divisor
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

entrada_usuario = input("Digite um número ou letra: ")

try:
    numero = int(entrada_usuario)
    print(f"Número digitado: {numero}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número.")

numero = [10, 20, 30]

try:
    print(numero[5])
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")

try:
    open("arquivo_inexistente.txt")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")

input_user = input("Faça um input: ")

try:
    input_user = float(input_user)
    input_user / 100
    print(f"Resultado: {input_user}")
    print(input_user[0])
except TypeError:
    print("Erro: Não é possível acessar um índice de um número.")
