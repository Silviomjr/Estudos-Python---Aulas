Nome = "Aliny"
idade = 29
altura = 1.54
eh_estudante = True

print('Nome: ', Nome)
print('idade: ', idade)
print('altura: ', altura)
print('eh_estudante: ', eh_estudante)

ano_nascimento = 2025 - idade
idade = idade + 5
eh_estudante = not eh_estudante
altura_cm = int(altura * 100) 

print('Minha idade daqui 5 anos: ', idade) 
print('Novo valor do estudante: ', eh_estudante)
print('Ano do Nascimento: ', ano_nascimento)
print('Minha altura em cm é: ', altura_cm)