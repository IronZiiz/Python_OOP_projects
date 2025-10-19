class Musica: 
    def __init__(self, nome, artista, duracao):
        if not isinstance(duracao, (int, float)):
            raise ValueError("A duração deve ser um número (inteiro ou float).")
 
        self.nome = nome
        self.artista = artista
        self.duracao = duracao 

    def __str__(self): 
        return f'{self.nome} | {self.artista} | {self.duracao}'
    

musica_1 =  Musica('Outubro','Milton Nascimento',5)
musica_2 = Musica('Wave','Tom Jobin',3)
musica_3 = Musica('Samurai', 'Djavan',2)


print(musica_1)