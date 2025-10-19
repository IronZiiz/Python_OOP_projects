# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

# 1 
pessoa = {
    'nome':'Thiago',
    'idade':20,
    'cidade':'Curitiba'}
    
print(pessoa)

# 2
## Utilizando método update para modificar idade
pessoa.update({'idade': 30})

## Utilizando a key  para adcionar a profissao 
pessoa['profissao'] = 'Analista'

pessoa.pop('nome')
print(pessoa)

# 3
numeros_quadrados = {num: num**2 for num in range(1,6)}
print(numeros_quadrados)

# 4 
key = 'rat'
print('A chave existe' if key in pessoa else 'Nao existe')

# 5 

frase = "Oi tudo bem como voce ? eu estou bem e voce ?"
palavras = frase.split()

print(palavras)

dicionario_frequencias = {}
for i in palavras: 
    if i in dicionario_frequencias: 
        dicionario_frequencias[i] +=1
    else:
        dicionario_frequencias[i] = 1

print(dicionario_frequencias)