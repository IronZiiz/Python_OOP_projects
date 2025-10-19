from mvc.views.console_view import exibir_subtitulo
from mvc.views.menu_view import (
    listar_restaurantes_view,
    mostrar_mensagem_status,
    mostrar_nao_encontrado,
    mostrar_mensagem_exclusao,

)
from mvc.models import repository
from mvc.views.menu_view import  mostrar_mensagem_cadastro_duplicado  

def cadastrar_restaurante_controller() -> None:
    """Fluxo de cadastro via CLI.

    Inputs:
        Nenhum (solicita dados via input()).

    Returns:
        None.
    """
    exibir_subtitulo("Cadastrar Restaurante")
    while True:
        nome = input("Digite o nome do restaurante: ").strip()
        if not nome:
            print("Nome não pode ser vazio. Tente novamente.")
            continue
        if repository.buscar_por_nome(nome) is not None:
            mostrar_mensagem_cadastro_duplicado(nome)
            continue
        break

    categoria = input(f'Digite a categoria do restaurante {nome}: ').strip()
    repository.adicionar(nome, categoria)
    print(f'Restaurante "{nome}" cadastrado com sucesso!')


def listar_restaurantes_controller() -> None:
    """Fluxo de listagem via CLI.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    exibir_subtitulo("Listando Restaurantes")
    listar_restaurantes_view(repository.listar())


def alternar_estado_controller() -> None:
    """Fluxo para alternar estado (ativo/inativo) via CLI.

    Inputs:
        Nenhum (solicita nome via input()).

    Returns:
        None.
    """
    exibir_subtitulo("Alterando o estado do restaurante")
    nome = input("Digite o nome do restaurante que deseja alterar o estado: ")
    if repository.alternar_status(nome):
        r = repository.buscar_por_nome(nome)
        mostrar_mensagem_status(nome, bool(r and r.get("ativo")))
    else:
        mostrar_nao_encontrado(nome)

def excluir_restaurante_controller() -> None:
    """Fluxo para excluir um restaurante via CLI.

    Inputs:
        Nenhum (solicita nome via input()).

    Returns:
        None.
    """
    exibir_subtitulo("Excluir Restaurante")
    nome = input("Digite o nome do restaurante que deseja excluir: ")
    if repository.excluir(nome):
        mostrar_mensagem_exclusao(nome)
    else:
        mostrar_nao_encontrado(nome)