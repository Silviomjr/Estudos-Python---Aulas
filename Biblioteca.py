class Biblioteca:
    def __init__(self):
        self.itens_biblioteca = {"Livros": [], "Filmes": [], "AudioBooks": []}
    
    #função para gerenciar itens           
    def gerenciar_item(self):
        acao = input("Digite a ação desejada (Adicionar, Remover, Emprestar, Devolver, Listar ou Histórico): ").casefold() #Adicionar novos itens
        if acao == "adicionar":
            self.adicionar_item()
        elif acao == "remover":
            self.remover_item()
        elif acao == "emprestar":
            self.emprestar_item()
        elif acao == "devolver":
          self.devolver_item()
        elif acao == "listar": 
            self.listar_itens()
        else:
            print("Ação inválida.")
    
    #ação de adicionar itens
    def adicionar_item(self):
        tipo_item = input("Digite o tipo de item (Livro, Filme, Audiobook): ").casefold()
        if tipo_item == "livro":
            titulo = input("Digite o título do livro: ").casefold()
            autor = input("Digite o autor do livro: ").casefold()
            ano = input("Digite o ano de publicação do livro: ").casefold()
            paginas = int(input("Digite o número de páginas do livro: "))
            genero = input("Digite o gênero do livro: ").casefold()
            self.itens_biblioteca["Livros"].append(Livro(1, titulo, ano, autor, paginas, genero))
        elif tipo_item == "filme":
            titulo = input("Digite o título do filme: ").casefold()
            diretor = input("Digite o diretor do filme: ").casefold()
            ano = input("Digite o ano de lançamento do filme: ").int()
            duracao_minutos = input("Digite a duração do filme em minutos: ").int()
            nota_de_avaliacao = input("Digite a nota de avaliação do filme: ").float()
            self.itens_biblioteca["Filmes"].append(Filme(1, titulo, ano, diretor, duracao_minutos, nota_de_avaliacao))
        elif tipo_item == "audiobook":
            titulo = input("Digite o título do audiobook: ").casefold()
            narrador = input("Digite o narrador do audiobook: ").casefold()
            ano =input("Digite o ano de lançamento do audiobook: ").int()
            duracao_horas = input("Digite a duração do audiobook em horas: ").float()
            self.itens_biblioteca["Audiobook"].append(AudioBook(1, titulo, ano, narrador, duracao_horas))
        else:
            print("Ação inválida.")
                
        #função de remover itens (ainda estou buscando uma forma de usar o pop)
    def remover_item(self):
            tipo_item = input("Digite o tipo de item (Livro, Filme, Audiobook): ").casefold()
            titulo_item = input("Digite o titulo do item a ser removido: ").casefold()
            item = tipo_item.capitalize() + "s"
            if item in self.itens_biblioteca:
                self.itens_biblioteca[item] = [titulo for titulo in self.itens_biblioteca[item] if titulo != titulo_item]
            else:
                print("Ação inválida.")
                
        #função de emprestar itens
    def emprestar_item(self):
        tipo_item = input("Digite o tipo de item (Livro, Filme, Audiobook): ").casefold()
        titulo_item = input("Digite o titulo do item a ser emprestado: ").casefold()
        item = tipo_item.capitalize() + "s"
        if item in self.itens_biblioteca:
            for item in self.itens_biblioteca[item]:
                if item.titulo == titulo_item:
                    if item.disponibilidade:
                        item.disponibilidade = False
                        print(f"O item '{titulo_item}' foi emprestado com sucesso.")
                    else:
                        print(f"O item '{titulo_item}' não está disponível para empréstimo.")
                        
        #função de devolver itens
    def devolver_item(self):
        tipo_item = input("Digite o tipo de item (Livro, Filme, Audiobook): ").casefold()
        titulo_item = input("Digite o titulo do item a ser devolvido: ").casefold()
        item = tipo_item.capitalize() + "s"
        if item in self.itens_biblioteca:
            for item in self.itens_biblioteca[item]:
                if not item.disponibilidade:
                    item.disponibilidade = True
                    print(f"O item '{titulo_item}' foi devolvido com sucesso.")
                else:
                    print(f"O item '{titulo_item}' já está disponível na biblioteca.")
                        
        #função de listar itens
    def listar_itens(self):
        for categoria, itens in self.itens_biblioteca.items():
            print(f"\n{categoria}:")
            for item in itens:
                disponibilidade = "Disponível" if item.disponibilidade else "Indisponível"
                if categoria == "Livros":
                    print(f"Título: {item.titulo}, Ano: {item.ano}, Autor: {item.autor}, Páginas: {item.paginas}, Gênero: {item.genero}, Disponibilidade: {disponibilidade}")
                elif categoria == "Filmes":
                    print(f"Título: {item.titulo}, Ano: {item.ano}, Diretor: {item.diretor}, Duração (minutos): {item.duracao_minutos}, Nota de Avaliação: {item.nota_de_avaliacao}, Disponibilidade: {disponibilidade}")
                elif categoria == "AudioBooks":
                    print(f"Título: {item.titulo}, Ano: {item.ano}, Narrador: {item.narrador}, Duração (horas): {item.duracao_horas}, Disponibilidade: {disponibilidade}")
        else:
            print("Ação inválida.")

class Midia:
    def _init_(self, titulo, ano): #disponibilidade
        self.titulo = titulo
        self.ano = ano
        self.disponibilidade = True

            
class Livro(Midia):
    def _init_(self, titulo, ano, autor, paginas, genero):
        super()._init_(titulo, ano)
        super().itens_biblioteca["Livros"].append(self)
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
               
class Filme(Midia):
    def _init_(self, titulo, ano, diretor ,duracao_minutos, nota_de_avaliacao):
        super()._init_(titulo, ano)
        super().itens_biblioteca["Filmes"].append(self)
        self.diretor = diretor
        self.duracao_minutos = duracao_minutos
        self.nota_de_avaliacao = nota_de_avaliacao
    
class AudioBook(Midia):
    def _init_(self, titulo, ano, narrador ,duracao_horas):
        super()._init_(titulo, ano)
        super().itens_biblioteca["AudioBooks"].append(self)
        self.narrador = narrador
        self.duracao_horas = duracao_horas
        
if __name__ == "__main__":
    Biblioteca().gerenciar_item()   
    
    # def obter_informaçao_filme(self): #listagem para o filme
    #      super()._init_(titulo, ano, disponibilidade) == self.obter_informaçao()
    # print(f'Titulo: {titulo}, Ano: {ano}, Disponibilidade: {disponibilidade}, Diretor: {self.diretor}, Duração (minutos): {self.duracao_minutos}, Nota de Avaliação: {self.nota_de_avaliacao}')  
     # def obter_informaçao_livro(self): #listagem para o livro
    #     super()._init_(titulo, ano, disponibilidade) == self.obter_informaçao()
    # print(f'Titulo: {titulo}, Ano: {ano}, Disponibilidade: {disponibilidade}, Autor: {self.autor}, Paginas: {self.paginas}, Genero: {self.genero}')
    # def obter_informaçao_audiobook(self): #listagem para o audiobook
    #      super()._init_(titulo, ano, disponibilidade) == self.obter_informaçao()
    # print(f'Titulo: {titulo}, Ano: {ano}, Disponibilidade: {disponibilidade}, Narrador: {self.narrador}, Duração (horas): {self.duracao_horas}')
    
