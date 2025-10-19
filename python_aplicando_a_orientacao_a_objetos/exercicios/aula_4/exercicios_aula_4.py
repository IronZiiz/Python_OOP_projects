# 1-Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
# Inicie um atributo chamado disponivel como True por padrão.

# 2-Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título,
# autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

# 3-Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# 4-Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e
# retorna uma lista dos livros disponíveis publicados nesse ano.

# 5-Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6-No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima 
# se o livro está disponível ou não após o empréstimo.

# 7-No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter
#  a lista de livros disponíveis publicados em um ano específico.

# 8-Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos
#  da classe Livro e exiba a mensagem formatada utilizando o método str.

# 1
class Livro: 
    def __init__(self, titulo='', autor='', ano_publicacao = int): 
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self.disponivel = True


livro_1 = Livro('teste', 'teste autor', 1999)

# 2 
class Livro: 
    def __init__(self, titulo='', autor='', ano_publicacao = int): 
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def __str__(self):
         return f'O autor é {self._autor} do livro {self._titulo}. Ano de publicacao: {self._ano_publicacao}'

livro_1 = Livro('teste', 'teste autor', 1999)
livro_2 = Livro('teste2', 'teste autor2', 2000)

# 3
class Livro: 
    def __init__(self, titulo='', autor='', ano_publicacao = int): 
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def __str__(self):
         return f'O autor é {self._autor} do livro {self._titulo}. Ano de publicacao: {self.ano_publicacao}'
    
    def emprestar_a_classe(self):
        self._disponivel = not self._disponivel

# 4 
class Livro: 
    livros = []

    def __init__(self, titulo='', autor='', ano_publicacao = int): 
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
         return f'O autor é {self._autor} do livro {self._titulo}. Ano de publicacao: {self._ano_publicacao}'
    
    def emprestar_a_classe(self):
        self._disponivel = not self._disponivel

    @staticmethod 
    def vericar_disponibilidade(ano = int): 
        for livro in Livro.livros:             
            if livro._disponivel == True and livro._ano_publicacao == ano:
                 print(f"Titulo: {livro._titulo.ljust(25)}Disponível:✅")
    
            

livro_1 = Livro('Livro 1', 'teste autor', 1999)
livro_1.emprestar_a_classe()
livro_2 = Livro('Livro 2', 'teste autor2', 1999)
