"""Módulo que define a classe Avaliacao."""


class Avaliacao:
    """Representa uma avaliação feita por um cliente a um restaurante.

    Atributos:
        cliente (str): Nome do cliente que avaliou.
        nota (int | float): Nota atribuída (esperado entre 0 e 5).
    """

    def __init__(self, cliente, nota):
        """Inicializa uma avaliação.

        Args:
            cliente (str): Nome do cliente que avaliou.
            nota (int | float): Nota atribuída ao restaurante.
        """
        self._cliente = cliente
        self._nota = nota
