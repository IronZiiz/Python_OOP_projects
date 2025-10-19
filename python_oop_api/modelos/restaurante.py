"""Módulo que define a classe Restaurante e exemplos de uso.

Inclui funcionalidades de cadastro de restaurantes, avaliações e
gerenciamento de cardápio.
"""

from modelos.avaliação import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    """Representa um restaurante com nome, categoria, estado e avaliações.

    Atributos de classe:
        restaurantes (list[Restaurante]): lista de todas as instâncias criadas.

    Propriedades de instância:
        nome (str): nome formatado com título (somente leitura).
        categoria (str): categoria em maiúsculas.
        ativo (str): indicador de status '✅' ou '❌'.
        media_avaliacoes (str | float): média das avaliações ou '-' se não houver.
    """

    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa um Restaurante.

        Args:
            nome (str): nome do restaurante.
            categoria (str): categoria do restaurante.
        """
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []  # lista de notas numéricas (0 a 5)
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """str: Representação curta do restaurante para exibição."""
        return f"{self.nome} | {self.categoria}"

    @staticmethod
    def listar_restaurantes():
        """Imprime uma tabela com os restaurantes cadastrados.

        Mostra nome, categoria, média e status.
        """
        cabecalho = (
            f'{"Nome do restaurante".ljust(25)} | '
            f'{"Categoria".ljust(25)} | '
            f'{"Avaliação".ljust(10)} | '
            f'{"Status"}'
        )
        print(cabecalho)
        for restaurante in Restaurante.restaurantes:
            linha = (
                f"{restaurante.nome.ljust(25)} | "
                f"{restaurante.categoria.ljust(25)} | "
                f"{str(restaurante.media_avaliacoes).ljust(10)} | "
                f"{restaurante.ativo}"
            )
            print(linha)

    @property
    def nome(self):
        """str: Nome do restaurante (somente leitura)."""
        return self._nome

    @property
    def ativo(self):
        """str: Ícone indicando se o restaurante está ativo."""
        return "✅" if self._ativo else "❌"

    def alternar_estado(self):
        """Alterna o estado ativo/inativo do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, nota):
        """Registra uma avaliação numérica de 0 a 5.

        Valores fora do intervalo serão ajustados para os limites.

        Args:
            nota (int | float): nota atribuída ao restaurante.
        """
        try:
            valor = float(nota)
        except (TypeError, ValueError):
            return
        valor = max(0.0, min(5.0, valor))
        self._avaliacoes.append(valor)

    @property
    def media_avaliacoes(self):
        """float | str: Média das avaliações com 1 casa decimal, ou '-' se vazio."""
        if not self._avaliacoes:
            return "-"
        soma_das_notas = sum(self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        """Adiciona um item ao cardápio, se for válido.

        Args:
            item (ItemCardapio): item a ser adicionado.
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        """Imprime todos os itens do cardápio formatados."""
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = (
                    f'{i}. Nome:{item._nome} | '
                    f'Preço: R${item._preco} | '
                    f'Descrição: {item.descricao}'
                )
                print(mensagem_prato)
            else:
                mensagem_bebida = (
                    f'{i}. Nome:{item._nome} | '
                    f'Preço: R${item._preco} | '
                    f'Descrição: {item.tamanho}'
                )
                print(mensagem_bebida)


if __name__ == "__main__":
    """Exemplos de uso dos métodos da classe Restaurante."""

    restaurante_praca = Restaurante("praca", "gourmet")
    restaurante_pizza = Restaurante("pizza", "pizzaria")

    restaurante_praca.alternar_estado()

    restaurante_praca.receber_avaliacao(100)
    restaurante_praca.receber_avaliacao(3.5)
    restaurante_pizza.receber_avaliacao(4)

    print(f"Média {restaurante_praca.nome}: {restaurante_praca.media_avaliacoes}")

    Restaurante.listar_restaurantes()
