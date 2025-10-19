# Crie uma classe chamada Sobremesa que herda de ItemCardapio, adicione atributos específicos como tipo,
# tamanho e descricao à classe Sobremesa. Ajuste a inicialização da classe para incluir esses novos atributos
# possibilitando a criação de um novo item ao cardápio do restaurante.
from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco): 
        self._nome = nome
        self._preco = preco 

    @abstractclassmethod
    def aplicar_desconto(self):
        pass

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao 

    def __str__(self):
        return  self._nome
    
    def aplicar_desconto(self): 
        self._preco -= self._preco * 0.075


# Atualize o método __str__ conforme necessário para refletir essas mudanças.

# Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio.
