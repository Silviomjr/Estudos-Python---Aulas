from enum import Enum

class Categoria(Enum):
    LIVRO = "Livro"
    AUDIOBOOK = "AudioBook"
    FILME = "Filme"

class Midia:
    def __init__(self, titulo, ano): #disponibilidade que é manipulado pelos métodos
        self.titulo = titulo
        self.ano = ano
        self.disponibilidade = True

    def obter_informacao(self):
        return self.ano, self.titulo, self.disponibilidade

class Book(Midia):
    def __init__(self, titulo, ano, autor, paginas, genero):
        super().__init__(titulo, ano)
        self.id = None
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
    
    def gerar_id(self, id):
        self.id = id

    def obter_informacao_do_book(self):
        (ano, titulo, disponibilidade) = self.obter_informacao()
        print(f'ID: {self.id}, Título: {titulo}, Ano: {self.ano}, Autor: {self.autor}, Páginas: {self.paginas}, Gênero: {self.genero}, Disponibilidade: {disponibilidade}')

class Movie(Midia):
    def __init__(self, titulo, ano, diretor, duracao_minutos, nota_de_avaliacao):
        super().__init__(titulo, ano)
        self.id = None
        self.diretor = diretor
        self.duracao_minutos = duracao_minutos
        self.nota_de_avaliacao = nota_de_avaliacao
    
    def gerar_id(self, id):
        self.id = id

    def obter_informacao_do_movie(self):
        (ano, titulo, disponibilidade) = self.obter_informacao()
        print(f'ID: {self.id}, Título: {titulo}, Ano: {self.ano}, Diretor: {self.diretor}, Duração: {self.duracao_minutos} minutos, Nota: {self.nota_de_avaliacao}, Disponibilidade: {disponibilidade}')

class AudioBook(Midia):
    def __init__(self, titulo, ano, narrador, duracao_horas):
        super().__init__(titulo, ano)
        self.id = None
        self.narrador = narrador
        self.duracao_horas = duracao_horas

    def gerar_id(self, id):
        self.id = id

    def obter_informacao_do_audiobook(self):
        (ano, titulo, disponibilidade) = self.obter_informacao()
        print(f'ID: {self.id}, Título: {titulo}, Ano: {self.ano}, Narrador: {self.narrador}, Duração: {self.duracao_horas} horas, Disponibilidade: {disponibilidade}')

class Library:
    def __init__(self):
        self.itens = dict()

    def adicionar_item(self, item, categoria):
        id = 0
        if categoria not in self.itens:
            self.itens[categoria] = []
            id = 1
        else:
            #[1, 4, 5]
            ultimoElemento = self.itens[categoria][-1]
            id = ultimoElemento.id + 1
        
        item.gerar_id(id)
        
        self.itens[categoria].append(item)

    def remover_item(self, item, categoria):
        if categoria not in self.itens:
            self.itens[categoria] = []
        self.itens[categoria].remove(item)

    def listar_itens(self):
        for categoria, itens in self.itens.items(): 
            for item in itens:
                if(categoria == Categoria.LIVRO):
                    item.obter_informacao_do_book()

                elif(categoria == Categoria.FILME):
                    item.obter_informacao_do_movie()

                else:
                    item.obter_informacao_do_audiobook()

    def buscar_item_por_titulo(self):
        resultados = []
        titulo = input("Digite o título do item que deseja buscar: ")
        for categoria, itens in self.itens.items():
            for item in itens:
                if item.titulo.lower() == titulo.lower():
                    resultados.append((categoria, item))
        return print("Resultados:", resultados[0][1].titulo if resultados else "Nenhum item encontrado com esse título.")

    def emprestar(self, titulo, disponibilidade):
        if(disponibilidade):
            print(f"Item '{self.titulo}' emprestado.")
            disponibilidade = False
        else:
            print(f"Item '{self.titulo}' já locado, não pode ser emprestado.")

    def devolver_item(self, titul, disponibilidade):
        if(not self.disponibilidade):
            print(f"Item '{self.titulo}' devolvido.")
            self.disponibilidade = True
        else:
            print(f"Item '{self.titulo}' já está disponível, não precisa ser retornado.")

    def mostrar_dicionario(self):
        for categoria, itens in self.itens.items():
            print(f"\nCategoria: {categoria.value}")
            for item in itens:
                if(categoria == Categoria.FILME):
                    print(f"{categoria}: {item.titulo} ({item.ano}) - Dirigido por {item.diretor}")
                elif(categoria == Categoria.LIVRO):
                    print(f"{categoria}: {item.titulo} ({item.ano}) - Escrito por {item.autor}")
                else:
                    print(f"{categoria}: {item.titulo} ({item.ano}) - Narrado por {item.narrador}")
                
    def historico_de_emprestimos(self):
        print("Histórico de Empréstimos:")
        for categoria, itens in self.itens.items():
            for item in itens:
                status = "Emprestado" if not item.disponibilidade else "Devolvido"
                print(f"{status} {categoria.value.lower()}: {item.titulo}")

# Exemplo de uso da classe Book
livro = Book('O Senhor dos Aneis', 1954, 'J.R.R. Tolkien', 1216, 'Fantasia Épica')
livro1 = Book('O Senhor dos Pasteis', 1954, 'J.L.R. Tolkien', 1217, 'Cozinha Épica')
filme = Movie('O Senhor dos Aneis - A Sociedade do Anel', 2001, 'Peter Jackson', 178, 8.8)
filme1 = Movie('O Senhor dos Pasteis: A Sociedade dos Pasteis', 2001, 'Peter Jickson', 178, 9.8)
audiobook = AudioBook('O Hobbit', 2020, 'Rob Inglis', 11)
audiobook1 = AudioBook('O Lobbit', 2022, 'Rob Inglis', 12)
audiobook2 = AudioBook('O Norbbit', 2022, 'Rob Inglis', 12)

biblioteca = Library()
biblioteca.adicionar_item(livro, Categoria.LIVRO)
biblioteca.adicionar_item(filme, Categoria.FILME)
biblioteca.adicionar_item(audiobook, Categoria.AUDIOBOOK)
biblioteca.adicionar_item(livro1, Categoria.LIVRO)
biblioteca.adicionar_item(filme1, Categoria.FILME)
biblioteca.adicionar_item(audiobook1, Categoria.AUDIOBOOK)
biblioteca.adicionar_item(audiobook2, Categoria.AUDIOBOOK)
biblioteca.remover_item(audiobook2, Categoria.AUDIOBOOK)



# biblioteca.listar_itens()
# biblioteca.historico_de_emprestimos() Input de usuario => 
biblioteca.listar_itens() 
biblioteca.buscar_item_por_titulo()
#biblioteca.emprestar(livro1.titulo, livro1.disponibilidade)