from mvc.controllers.menu_controller import (
    cadastrar_restaurante_controller,
    listar_restaurantes_controller,
    alternar_estado_controller,
    excluir_restaurante_controller,
)
from mvc.views.console_view import (
    limpar_tela,
    )

from mvc.views.menu_view import( 
    exibir_opcoes_do_menu,
    mostrar_opcao_invalida,
    exibir_nome_do_programa)

def run() -> None:
    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes_do_menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            mostrar_opcao_invalida()
            input("\nPressione Enter para continuar...")
            continue

        if opcao == 1:
            cadastrar_restaurante_controller()
        elif opcao == 2:
            listar_restaurantes_controller()
        elif opcao == 3:
            alternar_estado_controller()
        elif opcao == 4:
            excluir_restaurante_controller()
        elif opcao == 5:
            limpar_tela()
            print("Finalizando o programa...")
            break
        else:
            mostrar_opcao_invalida()

        input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    run()
