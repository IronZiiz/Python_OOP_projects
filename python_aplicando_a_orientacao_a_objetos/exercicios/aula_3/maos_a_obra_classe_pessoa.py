# Crie uma nova classe chamada Pessoa com atributos como nome, 
# idade e profissão. Adicione um método especial __str__ para 
# imprimir uma representação em string da pessoa. Implemente
# também um método de instância chamado aniversario que aumenta a 
# idade da pessoa em um ano. Por fim, adicione uma propriedade 
# chamada saudacao que retorna uma mensagem de saudação personalizada 
# com base na profissão da pessoa.

# Adcionei verificações de tipos de valores
class Pessoa: 
    def __init__(self, nome = '', idade = int, profissao = ''):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        if not isinstance(idade, int) or idade < 0:
            raise ValueError("A idade deve ser um número inteiro não negativo.")
        if not isinstance(profissao, str):
            raise ValueError("A profissão deve ser uma string.")
        
        self.nome = nome.strip()
        self.idade = idade
        self.profissao = profissao.strip()

    def __str__(self):
        return f'Pessoa: {self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self): 
        self.idade += 1 

    @property
    def saudacao(self): 
        if self.profissao: 
            return f'Eu me chamo {self.nome} e trabalho com {self.profissao}'
        else: 
            return f'Eu me chamo {self.nome}'
        

