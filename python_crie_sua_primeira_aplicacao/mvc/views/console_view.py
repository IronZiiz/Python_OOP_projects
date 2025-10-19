import os


def limpar_tela() -> None:
    """Limpa a tela do terminal conforme o sistema operacional.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    os.system("cls" if os.name == "nt" else "clear")


def exibir_subtitulo(texto: str) -> None:
    """Exibe um subtítulo formatado e uma linha de separação.

    Inputs:
        texto (str): Texto do subtítulo a ser exibido.

    Returns:
        None.
    """
    limpar_tela()
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)


