#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Lista com quatro nomes;

nomes = ['Kamala', 'Lola', 'Boris', 'Tusam']

#Lista com o ano que você nasceu e o ano atual.

ano = [1990, 2025]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

frutas = ['maça', 'banana', 'manga', 'abacaxi', 'morango']

for fruta in frutas:
    print('-' + fruta)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

num = 0

for i in range(1,11):
    if int(i)%2 != 0:
        num += i
print(num)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10,0,-1):
  print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero  = int(input('Escolha um número de 1 a 10: '))

print(f'A tabuada de {numero}:\n ')
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i} ')


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [2, 4, 6, 10, 12, 24]

soma_total = 0

try: 
  for numero in lista_numeros:
    soma_total += numero
  print(f'A soma de todos os números da lista é: {soma_total}')
except Exception as e:
  print('Ocorreu um erro {e}.')    


# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_numeros = [2, 4, 6, 10, 12, 24]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
        media = soma/len(lista_numeros)
    print(f'A média dos numeros é: {media}')
except ZeroDivisionError:
    print('Não foi possivel realizar a divisão.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')        