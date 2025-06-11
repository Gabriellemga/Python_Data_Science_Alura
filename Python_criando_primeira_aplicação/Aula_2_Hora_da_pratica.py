#1-Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Digite o número: '))

if numero%2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é impar.')

#2-Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Digite a sua idade: '))

if idade <= 12:
    print('Criança.')
elif idade  <= 18: 
    print('Adolescente')
else:
    print('Adulto')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome_usuario = input('Digite o nome de usuário: ')
senha_usuario = input('Digite a senha:')

usuario = 'python'
senha =  'python56'

if nome_usuario == usuario and senha_usuario == senha:
    print('O usuario e a senha estão corretos.')
else:
    print('Nome de usuário e senha incorretos.')

#4-4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")