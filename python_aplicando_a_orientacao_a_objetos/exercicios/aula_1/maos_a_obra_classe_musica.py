class Musica: 
    nome = ''
    artista = ''
    duracao = int

musica_1 =  Musica()
musica_1.nome = 'Outubro'
musica_1.artista = 'Milton Nascimento'
musica_1.duracao = 5


musica_2 = Musica()
musica_2.nome = 'Wave'
musica_2.artista = 'Tom Jobin'
musica_2.duracao = 3

musica_3 = Musica()
musica_3.nome = 'Samurai'
musica_3.artista = 'Djavan'
musica_3.duracao = 2

musicas = [musica_1, musica_2, musica_3]
for i in len(musicas): 
    print(vars(musicas[i]))