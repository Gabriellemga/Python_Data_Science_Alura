# 1-Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. 
# Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
# Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

lista_convidados = set() 
  
while True: 
    nome = input('Digite o nome do convidado ou "sair" para encerrar: ') 

    if nome == 'sair': 
        break 

    lista_convidados.add(nome) 

print(f"Convidados confirmados: {lista_convidados}") 


#2-Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. 
# Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

texto_1 = input('Escreva o primeiro texto:')
texto_2 = input('Escreva o segundo texto:')

conjunto_1 = set(texto_1.lower().split())
conjunto_2 = set(texto_2.lower().split())

print(f'As palavras comuns são: {conjunto_1.intersection(conjunto_2)}')

#3-Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
# Quais itens apareceram nas duas listas
# Quais foram exclusivos de Laura
# Quais foram exclusivos da Ana
# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

lista_laura = input('Escreva os itens da lista de Laura separados por virgula: ').split(', ')
lista_ana = input('Escreva os itens da lista de Ana separados por virgula: ').split(', ')

conjunto_laura = set(lista_laura)
conjunto__ana = set(lista_ana)

print(f'Itens em ambas as lista: {", ".join(conjunto_laura & conjunto__ana)}')
print(f'Itens exclusivos de Laura: {", ".join(conjunto_laura - conjunto__ana)}')
print(f'Itens exclusivos de Ana: {", ".join(conjunto__ana - conjunto_laura)}')

#4-Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. 
# Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

permissao_principal = {'leitura', 'escrita', 'execução', 'compartilhamento'}

permissao_1 = set(map(str.strip, input('Digite as permissões solicitadas separadas por vírgula do caso 1: ').lower().split(',')))
permissao_2 = set(map(str.strip, input('Digite as permissões solicitadas separadas por vírgula do caso 2: ').lower().split(',')))

if permissao_1.issubset(permissao_principal):
  print('As permissões solicitadas do caso 1 fazem parte das permissões principais.')
else:
    print('As permissões solicitadas do caso 2 não fazem parte das permissões principais.')
if permissao_2.issubset(permissao_principal):
     print('As permissões solicitadas do caso 2 fazem parte das permissões principais.')
else:
    print('As permissões solicitadas do caso 2 não fazem parte das permissões principais.')

#5-Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
# Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

atividades_a = set(map(str.strip, input('Digite as atividades da equipe a separadas por vírgula: ').lower().split(',')))
atividades_b = set(map(str.strip, input('Digite as atividades da equipe b separadas por vírgula: ').lower().split(',')))

atividades_unidas = atividades_a.union(atividades_b)

atividade_excluir = set(map(str.strip, input('Digite a(s) atividade(s) a ser excluida (separada(s) por vírgula caso 2 ou mais): ').lower().split(',')))

atividades_final = atividades_unidas - atividade_excluir

print(f'Tarefas finais: {", ".join(atividades_final)}')

#6-Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. 
# Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. 
# O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

chaves = []    
valor = []

while True: 
 produto = input('Digite o nome do produto e sair para encerrar o cadastro: ').capitalize()
 if produto == 'Sair':
  break
 chaves.append(produto)
 quantidade = input('Digite a quantidade do produto e sair para encerrar o cadastro: ')
 if quantidade == 'sair':
  break
 valor.append(quantidade)


dicionario = {chaves[i] : valor[i] for i in range(len(chaves))}

print(f'Dicionário de produtos {dicionario}')


#7-Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. 
# Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.


estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

print(f'Estoque atual: {estoque}')


while True :
 produto_atualizar = input('Digite o nome do a ser atualizado ou sair para encerrar: ').capitalize()
 if produto_atualizar == 'Sair':
   break
 quantidade_atualizar = input('Digite a nova quantidade do produto ou sair para encerrar: ')
 if quantidade_atualizar == 'sair':
   break

 estoque[produto_atualizar] = int(quantidade_atualizar)

print(f'Estoque atualizado:{estoque}')

#8-Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. 
# Agora, ele precisa de um programa que apresente três informações:
# Os nomes de todos os participantes.
# As idades de todos os participantes.
# Uma relação completa com o nome e a idade de cada um.
# Sua tarefa é criar esse programa com base nas informações fornecidas.


participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

nomes = list(participantes.keys())
idades = list(participantes.values())

print(f'Nome dos participantes: {", ".join(nomes)}')
print(f'Idades dos participantes:{", ".join(map(str,idades))}')

print(f'Participantes e suas idades:')
for nome, idade in participantes.items():
 print(f' - {nome}: {idade} anos ')

#9-Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. 
# O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
# O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.


participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

print (participantes)

nome_remover = input("Nome do participante a ser removido :").strip()

if nome_remover in (participantes["Workshop 1"]):
    participantes["Workshop 1"].remove(nome_remover)
elif nome_remover in (participantes["Workshop 2"]):
    participantes["Workshop 2"].remove(nome_remover)

print("Lista atualizada de participantes :")
print(participantes)


#10-Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. 
# Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. 
# Sua tarefa é criar um programa que exiba o total de vendas por categoria.


vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

} 

print("Total de vendas por categoria:") 

for categoria, itens in vendas.items():
    total = sum((item["quantidade"] * item["valor_unitario"] for item in itens))
    print(f'-{categoria}: R$ {total} ')