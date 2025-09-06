# Tarefa 1: Classificação de notas
nota = 91
if nota >= 90 and nota <= 100:
    print("Classificação da nota: A")
elif nota >= 80 and nota <= 89:
    print("Classificação da nota: B")
elif nota >= 70 and nota <= 79:
    print("Classificação da nota: C")
elif  nota >= 60 and nota <= 69:
    print("Classificação da nota: D")
else:
    print("Classificação da nota: F")

# Tarefa 2: Categoria de idade
idade = 18
if idade > 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade invalida")

# Tarefa 3: Sistema de semáforo
cor_semaforo = 'vermelho'

if cor_semaforo == 'verde':
    print("SIGA!")
elif cor_semaforo == 'amarelo':
    print("ATENÇÃO!")
elif cor_semaforo == 'vermelho':
    print("PARE!!!!!!!!!")
else:
    print("Cor invalida!")

# Tarefa 4: Calculadora de IMC
peso = 70
altura = 1.79
imc = peso / (altura * altura)

if imc < 18.5:
    print("IMC: Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("IMC: Normal")
elif imc >= 25 and imc <= 29.9:
    print("IMC: Sobrepeso")
else:
    print("IMC: Obeso")

# Tarefa 5: Identificador de estação
mes = 10

if mes == 12 or mes == 1 or mes == 2:
    print("Verão")
elif mes >=3 and mes <= 5:
    print("Outono!")
elif mes >=6 and mes <= 8:
    print("Inverno")
elif mes >=9 and mes <= 11:
    print("Primavera")
else:
    print("Mes Invalido!")