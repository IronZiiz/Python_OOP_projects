from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)

restaurante_mexicano = Restaurante('MexicanFood', 'Mexicano')
restaurante_mexicano.alternar_estado()
restaurante_japones = Restaurante('Japa', 'Japonesa')



def main():
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__': 
    main()