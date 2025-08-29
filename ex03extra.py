num = 1334

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

idade = 40

if idade >= 16:
    print("Voce já pode votar... Escolha bem")
else:
    print("Voce não pode votar... Apenas com 16 anos pivete")

compra_total = 1000

if compra_total >= 100:
    compra_total *= 0.9
    print(f"Você ganhou 10% de desconto! Total a pagar: R${compra_total:.2f}")
else:
    print("Valor da compra abaixo de R$100,00. Sem desconto.")

temperatura = 10
if temperatura < 20:
    print("Congelando... Use jaqueta... Senão for a Elsa")
else:
    print("Camiseta tá ótima... Só não abusa hein")

tamanho_usuario = 13

if tamanho_usuario == 3 and tamanho_usuario >=15:
    print("Nome de usuario é valido")
else:
    print("Nome de usuario é invalido")