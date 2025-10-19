# Exercícios
# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# 1 
# lista_numeros_1_a_10 = list(range(1, 11))
list_numeros_1_a_10 = []
for i in range(1, 11):
    list_numeros_1_a_10.append(i)

lista_nomes = ['Alice', 'Bob', 'Charlie', 'Diana']
lista_anos = [2004, 2023]

# 2
lista_percorrida = ['Thiago', 'Maria', 'José', 'Ana']
for nome in lista_percorrida:
    print(nome)

# 3 
list_numeros_1_a_10

soma = 0
for i in list_numeros_1_a_10:
    if list_numeros_1_a_10[i-1] % 2 == 0:
        soma += list_numeros_1_a_10[i-1]

print(f'Soma dos números pares de 1 a 10: {soma}')

# 4 
for i in range(10, 0, -1):
    print(i)

# 5 
input_numero = int(input('Digite um número para ver a tabuada: '))
for i in list_numeros_1_a_10:
    print(f'{input_numero} x {i} = {input_numero * i}')

# 6
lista_numeros = [1, 2, 3, None, 5]
soma = 0
for num in lista_numeros:
    try:
        soma += num
    except TypeError:
        continue
print(f'Soma dos números na lista: {soma}')


# 7 
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")