from exercicios_aula_4 import Livro

livro3 = Livro('Livro 3', 'Autor 3', 1900)
livro3.emprestar_a_classe()
print(vars(livro3))
Livro.vericar_disponibilidade(1900)