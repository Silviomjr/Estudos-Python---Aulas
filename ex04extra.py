nota = 60  

if nota >= 90 and nota <= 100:
    print("Aprovado com A")
elif nota >= 80 and nota <= 89:
    print("Aprovado com B")
elif nota >= 70 and nota <= 79:
    print("Aprovado com C")
elif nota >= 60 and nota <= 69:
    print("Aprovado com D")
else:
    print("Reprovado com E")


idade = 89  

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")

cor_semaforo = "verde"

if cor_semaforo == "verde":
    print("Siga")
elif cor_semaforo == "amarelo":
    print("Atenção")
elif cor_semaforo == "vermelho":
    print("Pare")
else:
    print("Cor Invalida")

peso = 77
altura = 176

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidade")

mes = 12

if mes == 12 or mes == 1 or mes == 2:
    print("Verão") 
elif mes == 3 or mes == 4 or mes == 5:
    print("Outono")
elif mes == 6 or mes == 7 or mes == 8:
    print("Inverno")
elif mes == 9 or mes == 10 or mes == 11:
    print("Primavera")
else:
    print("Mês inválido")
