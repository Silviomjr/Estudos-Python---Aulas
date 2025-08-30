#Tarefa 1
nota = 40
if nota >= 90:
    print('Nota A')
elif nota >= 80 and nota <= 89:
    print('Nota B')
elif nota >= 70 and nota <= 79:
    print('Nota C')
elif nota >= 60 and nota <= 69:
    print('Nota D')
else:
    print('Nota F')

#Tarefa 2
idade = 61
if idade <= 12:
    print('Criança')
elif idade >= 13 and idade <=17:
    print('Adolescente')
elif idade >=18 and idade <=59:
    print('Adulto')
else:
    print('Idoso')

#Tarefa 3
cor_semaforo = "Rosa"
if cor_semaforo == "Vermelho":
    print('Pare!')
elif cor_semaforo == "Amarelo":
    print('Atenção!')
elif cor_semaforo == "Verde":
    print('Siga!')
else:
    print('Cor Inválida!')

#Tarefa 4
peso = 100
altura = 1.54
IMC = peso / (altura*altura)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >=18.5 and IMC <= 24.9:
    print('Normal')
elif IMC >= 25 and IMC <= 29.9:
    print('Sobrepeso')
else:
    print('Obeso')

#Tarefa 5
mes = 9
if mes == 12 or mes == 1 or mes == 2:
    print('Verão!')
elif mes == 3 or mes == 4 or mes == 5:
    print('Outono!')
elif mes == 6 or mes == 7 or mes == 8:
    print('Inverno!')
elif mes == 9 or mes == 10 or mes == 11:
    print('Primavera!')
else:
    print('Número Inválido!')