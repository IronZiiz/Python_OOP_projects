"""Módulo principal para gerenciamento de restaurante e cardápio.

Este script cria um restaurante, adiciona itens ao cardápio
(bebida e prato) e exibe o cardápio final.
"""


from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0 , 'grande')
bebida_suco.aplicar_desconto()

prato_pao = Prato('Pao', 2.00, 'O melhor pao')
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    """Executa o fluxo principal da aplicação.

    Exibe o cardápio completo do restaurante configurado.
    """
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()