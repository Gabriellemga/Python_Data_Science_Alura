#1-Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
#Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

def calcula_idade( ano_nascimento, ano_atual):
    idade_atual = ano_atual - ano_nascimento
    print(f'A idade atual é de {idade_atual} anos.')
    return idade_atual


calcula_idade(ano_nascimento, ano_atual)

#2-Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
#Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

palavra = input('Digite uma palavra: ')

def conta_caracteres(palavra):
    caractere = len(palavra)
    print(f' Essa palavra tem {caractere} caracteres.')
    return caractere

conta_caracteres(palavra)

#3-Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
# Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
# O sistema deverá ter a seguinte regra:
#Se for antes das 12h, exibir "Bom dia";
#Entre 12h e 18h, exibir "Boa tarde";
#Após 18h, exibir "Boa noite".

nome = input('Digite o seu nome: ')
hora = int(input('Digite a hora atual (0-23): '))

def saudacao_hora(hora):
    if hora < 12:
        print(f'Bom dia {nome} !!')
    elif hora >= 12 and hora < 18:
        print(f'Boa tarde {nome} !!')
    elif hora >= 18:
        print(f'Boa noite {nome} !!')
    return hora

saudacao_hora(hora)

#4-Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings.
#  No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
#Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def texto_inteiro(telefones):
    tel_inteiro  = list(map(int, telefones))
    return tel_inteiro

def verificar_inteiro(tel_inteiro):
    inteiro =all(True if isinstance(inteiro, int) else False for inteiro in tel_inteiro )
    return inteiro

tel_inteiro = texto_inteiro(telefones)
inteiro = verificar_inteiro(tel_inteiro)

if inteiro == True: 
     print('Os números forão convertidos de maneira  correta.')
else:
     print('Os números não forão convertidos de maneira correta.')
  
#5-Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
# As vendas são informadas em uma única linha separadas por espaços.
#Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

vendas = input('Digite os valores das vendas separados por espaço: ').split(' ')

def vendas_total(vendas):
    texto_numero = map(float,vendas)
    soma = sum(texto_numero)
    print(f'A soma de todas as vendas: R$ {soma} reais.')

vendas_total(vendas)

#6-Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
#Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

numeros = input('Digite os números separados por espaço: ').split(' ')

def pares (numeros):
    numeros = map(int,numeros)
    num_pares = list(filter(lambda x :  x%2 == 0, numeros))
    print(f' Números pares: { ", ".join(map(str,(num_pares)))}')

pares(numeros)

#7-Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços.
#  Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
#Crie um programa que junte as listas e exiba o resultado no formato produto: preço

produtos = input('Digite o nome dos produtos separados por vírgula: ').lower().split(',')
precos = input('Digite os preços separados por vírgula: ').lower().split(',')

def produto_preco(produtos, precos):
    for i in range(len(produtos)):
     print(f'{produtos[i].strip()}: {precos[i].strip()}')


produto_preco(produtos, precos)

#8-Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
#Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (+, -, *, /): ")

operacoes = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
}

resultado = operacoes.get(operador, lambda x, y: "Operação inválida")(num1, num2)
print(f"Resultado: {resultado}")

#9-Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
#Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

valor = float(input('Digite o valor da compra: '))  
desconto = float(input('Digite a porcentagem de desconto: '))  


def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       preco_desconto = valor - (valor * (porcentagem / 100))
       return   preco_desconto

   return calcular_preco 


calcular_preco_final = criar_desconto(desconto) 

print(f'Preço final com desconto: {calcular_preco_final(valor)} reais') 

#10-Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. 
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
#Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

num = int(input('Digite um número: '))

def soma (n):
    if n <= 1 :
        return 1
    else:
        return n + soma(n - 1)

soma_total = soma(num)

print(f'A soma de todos os inteiros de {num} até 1 é {soma_total}')