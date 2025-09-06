# Tarefa 1: Número par ou ímpar
numero = 9

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

# Tarefa 2: Elegibilidade para votar
idade = 15
if idade >= 16:
    print("Você pode votar")
else:
    print("Você ainda não pode votar")

# Tarefa 3: Desconto no preço
compra_total = 750

if compra_total >= 100:
    compra_total = compra_total - (compra_total*0.10)
    print(f"Preço final com desconto: {compra_total}")
else:
    print(f"Preço final sem desconto: {compra_total}")

# Tarefa 4: Roupa para o clima
temperatura = 19

if temperatura < 20:
    print("Use uma jaqueta")
else:
    print("Camiseta está bom")

# Tarefa 5: Disponibilidade de nome de usuário
tamanho_usuario = 'ri'
if tamanho_usuario.__len__() >= 3 and tamanho_usuario.__len__() <= 15:
    print("Nome de usuário é válido!")
else:
    print("Nome de usuário é inválido!")