"""Módulo que define a classe Prato."""

from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    """Representa um prato no cardápio de um restaurante.

    Herda de:
        ItemCardapio

    Atributos:
        descricao (str): Descrição detalhada do prato.
    """

    def __init__(self, nome, preco, descricao):
        """Inicializa um prato.

        Args:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição do prato.
        """
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        """str: Retorna o nome do prato."""
        return self._nome

    def aplicar_desconto(self):
        """Aplica um desconto de 5% ao preço do prato."""
        self._preco -= self._preco * 0.05
