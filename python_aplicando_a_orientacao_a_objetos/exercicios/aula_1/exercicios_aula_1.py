# 1-Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# 2-Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# 3-Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# 4-Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# 5-Altere o valor do atributo nome para 'Bistrô'.
# 6-Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# 7-Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# 8-Mude o estado da instância restaurante_pizza para ativo.
# 9-Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurante: 
    nome = ''
    categoria = '' 
    ativo = False 

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'

#1
restaurante_praca.categoria = 'Italiana'

#2
print(restaurante_praca.categoria)

#3 
if restaurante_praca.ativo: 
    print('Esta ativo')
else:
    print('Inativo')

#4 
categoria = restaurante_praca.categoria
print(categoria)

#5 
restaurante_praca.nome = 'Bistro'
print(restaurante_praca.nome)

#6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = False

#7 
if restaurante_pizza.categoria == 'Fast Food': 
    print('Categoria correta')
else: 
    print('Nao é')

#8 
def altera_estado(objeto): 
    if objeto.ativo:
        objeto.ativo = False 
    else: 
        objeto.ativo = True 

    return objeto 

print(vars(restaurante_pizza))
altera_estado(restaurante_pizza)
print(vars(restaurante_pizza))

#9 
print(f'Nome: {restaurante_praca.nome}\nCategoria: {restaurante_praca.categoria}')