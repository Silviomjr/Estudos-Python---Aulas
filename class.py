class Carro:
    # Método construtor (__init__)
    def __init__(self, cor, modelo, preco):
        self.cor = cor
        self.modelo = modelo
        self.preco = preco
    
    # Método para ligar o carro
    def ligar_carro(self):
        print(f"Ligando o carro {self.modelo}...")

# Exemplo de uso da classe Carro
meu_carro = Carro("vermelho", "Sedan", 50000.000)
print(f"Meu carro é um {meu_carro.modelo} de cor {meu_carro.cor} e custa R${meu_carro.preco}.")
meu_carro.ligar_carro()