#Tarefa 1
numero = 49
if numero %2==0:
    print('Número Par')
else:
    print('Número Ímpar')

#Tarefa 2
idade = 14
if idade >= 16:
    print('Você pode votar!')
else:
    print('Você ainda não pode votar!')

#Tarefa 3
compra_total = 110
if compra_total >= 100:
    compra_total = compra_total * 0.90
    print('Valor final com desconto: ', compra_total)
else:
    print('Valor sem desconto: ', compra_total)

#Tarefa 4
temperatura = 40
if temperatura < 20:
    print('Use uma Jaqueta!')
else:
    print('Camiseta está bom!')

#Tarefa 5
tamanho_usuario = "Al"
if len(tamanho_usuario) >=3 and len(tamanho_usuario)<= 15: 
    print('Nome de usuário é válido!')
else:
    print('Nome de usuário é inválido!')