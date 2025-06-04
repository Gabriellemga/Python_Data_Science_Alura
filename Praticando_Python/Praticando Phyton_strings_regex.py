#1-Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que estão sendo cadastrados pelos lojistas. 
# Esses nomes geralmente vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.
#Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas as letras minúsculas e removendo os espaços extras.

produto = input('Digite o nome do produto: ')
produto_padronizado = produto.lower().strip()

print(produto_padronizado)

#2-Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes. 
# Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.
#Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

cliente = input('Digite o nome do cliente: ')
cidade = input('Digite a cidade do cliente: ')

print(f'Olá {cliente}! Bem-vinda ao sistema da cidade de {cidade}.')

#3-Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. 
# Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.
#Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

palavra  = input('Digite uma palavra: ')
letras_inicio = palavra[:3]
letras_fim = palavra[-3:]

print(f'As três primeiras letras são: {letras_inicio}')
print(f'As três ultimas letras são: {letras_fim}')

#4-Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. 
# Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.
#Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?

url = input('Digite a URL para validação: ')
if url.startswith('https://') and url.endswith('.com'):
  print('A URL é válida!')
else:
  print('A URL é inválida.')

#5-João é atendente em uma farmácia e precisa verificar se um cliente forneceu um número de receita válido em uma descrição. 
# O número da receita é sempre o único número presente no texto fornecido pelo cliente. 
# Ele quer um programa que extraia esse número diretamente e confirme se o texto está correto, sem a necessidade de trabalhar com listas ou loops.
#Com base nesse cenário, crie um programa que receba um texto com uma descrição e exiba uma mensagem com o número encontrado.

import re
numero_receita = input('Digite a descrição da receita: ')

numero_encontrado = re.search(r'\d+', numero_receita)

if numero_encontrado:
    print(f'O número da receita é: {numero_encontrado.group()}')
   
#6-Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". 
# Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.
#Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. 
# O programa deve exibir o texto com as alterações aplicadas.

texto = input('Digite o texto a ser revisado: ')
palavra = input('Qual palavra deseja substituir ? ')
palavra_nova = input('Qual é a palavra nova ?')
substituição = texto.replace(palavra, palavra_nova)

print(substituição)

#7-Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. 
# O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). 
# Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.
#Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

import re

cliente = input('Digite o nome do cliente para validação: ')
padrao = r'([A-Z]{1})([a-z]{1,})$'
resultado = re.search(padrao, cliente)

if  resultado:
    print('Nome válido!')
else :
    print('Nome inválido!')    

#8-Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando seus números de CPF no formato correto antes de registrar os dados no sistema.
#O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).
#Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.

import re 

cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
padrao = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'

resultado = re.search(padrao, cpf)
if resultado:
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")

#9-Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas.
# Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.
#Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

import re

livro = input('Digite o título do livro: ')
letra = input('Digite a letra inicial para pesquisa: ')

padrao = rf'\b{letra}[a-zA-Z]+'

palavras = re.findall(padrao,livro)

print(palavras)

#10-Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". 
# Por exemplo, “Monalisa Silva - 1994”.
#Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.
#Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

import re

dados = input('Digite o nome completo e o ano de nascimento do paciente: ')

nome = re.findall(r'[a-zA-Z]+', dados)
ano  = re.findall(r'\d+',dados)

print(f'Primeiro nome: {nome[0]}\n Sobrenome:{nome[1]}\n Ano de nascimento: {ano[0]}')
