"""Módulo que define a classe abstrata ItemCardapio."""

from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    """Classe base abstrata para representar um item do cardápio.

    Atributos:
        _nome (str): Nome do item.
        _preco (float): Preço do item.
    """

    def __init__(self, nome, preco):
        """Inicializa um item do cardápio.

        Args:
            nome (str): Nome do item.
            preco (float): Preço do item.
        """
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        """Aplica um desconto ao item do cardápio.

        Este método deve ser implementado pelas subclasses.
        """
        pass
