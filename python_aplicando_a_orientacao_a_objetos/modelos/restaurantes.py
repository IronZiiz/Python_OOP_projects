
class Restaurante:
    """Representa um restaurante com nome, categoria, estado e avaliações.

    Atributos:
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
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação curta para exibição."""
        return f"{self.nome} | {self.categoria}"

    @staticmethod
    def listar_restaurantes():
        """Imprime uma tabela com os restaurantes cadastrados.

        Mostra nome, categoria, média e status.
        """
        cabecalho = f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(10)} | {"Status"}'
        print(cabecalho)
        for restaurante in Restaurante.restaurantes:
            linha = f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(10)} | {restaurante.ativo}"
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
            return  # ignora valores não numéricos
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


if __name__ == "__main__":
    """Exemplos de uso dos métodos da classe no(s) objeto(s)."""
    # Criação de objetos
    restaurante_praca = Restaurante("praca", "gourmet")
    restaurante_pizza = Restaurante("pizza", "pizzaria")

    # Alternar estado de um restaurante
    restaurante_praca.alternar_estado()

    # Registrar avaliações
    restaurante_praca.receber_avaliacao(100)
    restaurante_praca.receber_avaliacao(3.5)
    restaurante_pizza.receber_avaliacao(4)

    # Exibir média de avaliações de um objeto específico
    print(f"Média {restaurante_praca.nome}: {restaurante_praca.media_avaliacoes}")

    # Listar todos os restaurantes
    Restaurante.listar_restaurantes()
