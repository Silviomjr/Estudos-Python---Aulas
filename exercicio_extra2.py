# Tarefa 1: Verificação de idade
idade = 17

if idade >= 18:
    print("Voce é maior de idade!")
else:
    print("Você não é maior de idade!")

# Tarefa 2: Verificação de número positivo
numero = -10

if numero > 0:
    print(f"O numero {numero} é positivo!")
elif numero == 0:
    print("Zero é um numero neutro! Não é positivo e nem negativo!")
else:
    print(f"O numero {numero} é negativo!")



# Tarefa 3: Verificação do comprimento da senha
senha = 'abc123a'

if senha.__len__() >= 8: 
    print("Senha é forte o suficiente")
else:
    print("Senha fraca!")



# Tarefa 4: Verificação de temperatura
temperatura = 31

if temperatura > 30:
    print("Está quente lá fora!")
else:
    print("Não esta tão quente la fora!")

# Tarefa 5: Verificação de nota
nota = 50

if nota >= 60:
    print("Parabéns! Você passou!")
else:
    print("Você nao atingiu a média! Reprovado")