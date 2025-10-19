from typing import Dict, List


def exibir_nome_do_programa() -> None:
    """Exibe o título do programa no terminal.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    print("Sabor Express - Sistema de Gestão de Restaurantes")


def exibir_opcoes_do_menu() -> None:
    """Mostra as opções disponíveis do menu principal.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    print("Menu de Opções:")
    print("----------------")
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Excluir restaurante")
    print("5. Sair\n")


def listar_restaurantes_view(restaurantes: List[Dict[str, object]]) -> None:
    """Exibe a lista de restaurantes.

    Inputs:
        restaurantes (List[Dict[str, object]]): Registros a serem exibidos.

    Returns:
        None.
    """
    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status')
    for r in restaurantes:
        status = "ativado" if r.get("ativo") else "desativado"
        print(f'- {str(r.get("nome", "")).ljust(20)} | {str(r.get("categoria", "")).ljust(20)} | {status}')


def mostrar_mensagem_status(nome: str, ativo: bool) -> None:
    """Mostra mensagem de ativação/desativação de um restaurante.

    Inputs:
        nome (str): Nome do restaurante.
        ativo (bool): Estado atual após a alteração.

    Returns:
        None.
    """
    msg = "ativado" if ativo else "desativado"
    print(f'O restaurante "{nome}" foi {msg} com sucesso')


def mostrar_nao_encontrado(nome: str) -> None:
    """Exibe mensagem quando um restaurante não é encontrado.

    Inputs:
        nome (str): Nome consultado.

    Returns:
        None.
    """
    print(f'Restaurante "{nome}" não encontrado.')


def mostrar_opcao_invalida() -> None:
    """Exibe mensagem para opção inválida do menu.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    print("Opção inválida. Tente novamente.")

def mostrar_mensagem_exclusao(nome: str) -> None:
    """Exibe mensagem de exclusão de um restaurante.

    Inputs:
        nome (str): Nome do restaurante excluído.

    Returns:
        None.
    """
    print(f'Restaurante "{nome}" excluído com sucesso')

def mostrar_mensagem_cadastro_duplicado(nome: str) -> None:
    """Exibe mensagem de cadastro duplicado de um restaurante.

    Inputs:
        nome (str): Nome do restaurante cadastrado.

    Returns:
        None.
    """
    print(f'Restaurante "{nome}" já cadastrado.Tente novamente.')