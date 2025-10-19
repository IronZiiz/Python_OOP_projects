"""Módulo que define a classe Bebida."""

from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """Representa uma bebida no cardápio de um restaurante.

    Herda de:
        ItemCardapio

    Atributos:
        tamanho (str): Tamanho da bebida (ex.: pequeno, médio, grande).
    """

    def __init__(self, nome, preco, tamanho):
        """Inicializa uma bebida.

        Args:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            tamanho (str): Tamanho da bebida.
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        """str: Retorna o nome da bebida."""
        return self._nome

    def aplicar_desconto(self):
        """Aplica um desconto de 8% ao preço da bebida."""
        self._preco -= self._preco * 0.08
