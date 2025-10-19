# Exercícios
# 1-Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

# 2-Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e 
# crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

# 3-Modifique a classe Restaurante adicionando um construtor que aceita nome
# e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância
#  utilizando o construtor.

# 4-Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma
# instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa
# mensagem para uma instância de restaurante.

# 5-Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie
# 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

# 1 
class Carro:
    def _init__(self,modelo,cor,ano): 
        if not isinstance(ano,int): 
            raise ValueError('O ano deve ser um numero inteiro')
        
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo}|{self.cor}|{self.ano}'
    
# 2 
class Restaurante:
    def __init__(self, nome, categoria, ativo, ano_de_inauguracao, localizacao): 
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo 
        self.ano_de_inauguracao = ano_de_inauguracao
        self.localizacao = localizacao

    def __str__(self): 
        return f'{self.nome} | {self.ativo}'
    
restaurante_1 = Restaurante('Elvis', 'Comida arabe', True, 1998, 'rua dos gnomos 777')
print(restaurante_1) # impressão mais palatavel da referencia do objeto 
print(vars(restaurante_1)) # impressão do dicionario contendo chave-valor de cada atributo

# 3 
class Restaurante:
    def __init__(self, nome, categoria, ativo = False): 
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo 
    def __str__(self): 
        return f'{self.nome} | {self.ativo}'
    
restaurante_2 = Restaurante('Elvis2', 'Comida arabe')
print(restaurante_2)
print(vars(restaurante_2))

# 4
# Acabei por aplicar o método especial desde o inicio 
class Restaurante:
    def __init__(self, nome, categoria, ativo = False): 
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo 
    def __str__(self): 
        return f'{self.nome} | {self.categoria}'
    
restaurante_3 = Restaurante('Elvis2', 'Comida arabe')
print(restaurante_3)
print(vars(restaurante_3))

# 5 
from datetime import datetime

class Cliente: 
    def __init__(self, nome, email, categoria, data_de_registro): 
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("O email deve ser uma string válida contendo '@'.")
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("A categoria deve ser uma string não vazia.")
        if isinstance(data_de_registro, str):
            try:
                data_de_registro = datetime.strptime(data_de_registro, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("A data de registro deve estar no formato 'YYYY-MM-DD'.")
        elif not isinstance(data_de_registro, datetime.date):
            raise ValueError("A data de registro deve ser uma instância de 'datetime.date' ou uma string no formato 'YYYY-MM-DD'.")
        
        self.nome = nome.strip()
        self.email = email.strip()
        self.categoria = categoria.strip()
        self.data_de_registro = data_de_registro

# Exemplo de uso
cliente_1 = Cliente('Thiago', 'thiago@gmail.com', 'pessoa fisica', '2004-10-10')
print(vars(cliente_1))