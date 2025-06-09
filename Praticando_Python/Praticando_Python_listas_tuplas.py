# 1-Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa.
# Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

item = input('Digite o item que você quer verificar: ')
lista_comprar = ['arroz', 'café', 'manteiga']

if item in lista_comprar:
    print(f'O item {item} está na lista.')
else:
    print(f'O item {item} precisa ser comprado.')


# 2-Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. 
# Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.
# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

lista_notas = []
notas = float(input('Digite a nota dos participantes:'))
while len(lista_notas) < 5:
    lista_notas.append(notas)
    lista_notas = sorted(lista_notas)
    notas = float(input('Digite a nota dos participantes:'))

print(lista_notas)

#3-Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. 
# À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
#Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

lista_voluntario = []
voluntario = input('Digite o nome do voluntário (ou sair para encerrar): ')

while voluntario != 'sair':
    lista_voluntario.append(voluntario)
    voluntario = input('Digite o nome do voluntário (ou sair para encerrar): ')
    if voluntario == 'sair':
     print('O cadastro foi encerrado.')
     break
     
 
print(lista_voluntario)

#4-Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
#Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

estoque_1 = tuple(input('Digite os produtos do estoque 1 (separados por vírgula): ').split(','))
estoque_2 = tuple(input('Digite os produtos do estoque 2 (separados por vírgula): ').split(','))

estoque_completo = estoque_1 + estoque_2

print(f' Estoque  completo: {estoque_completo}')

#5-Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
# Camila quer adicionar novos nomes e organizá-los em posições específicas.
#Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

lista_atual_convidados =  ['Ana', 'Pedro', 'Carlos']

print(f'Lista atual de convidados: {lista_atual_convidados}')

novo_convidado = input('Digite o nome do novo convidado: ')
posição = int(input('Digite a posição que deseja inserir o convidado: '))-1

lista_atual_convidados.insert(posição, novo_convidado)

print(f' A lista atualizada é :{lista_atual_convidados}')

#6-A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante.
#  Os eventos foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.
#Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

eventos_registrados.reverse()

print(f' A ordem dos eventos na ordem correta é: {eventos_registrados}')

#7-O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
# Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
#Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

nome_incorreto = input('Digite o nome incorreto: ')
nome_correto = input('Digite o nome correto: ')

lista_atletas = ['Ana', 'Carlos', 'Pedro', 'José']

posição = lista_atletas.index(nome_incorreto)
lista_atletas.remove(nome_incorreto)
lista_atletas.insert(posição,nome_correto)

print(f'Lista corrigida:{lista_atletas}')

#8-Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.
#Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.

pedidos = input('Digite os pedidos (separados por vírgula): ').split(',')

pedidos.pop(-1)

print(f'Pedidos finais:{pedidos}')


#9-A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma.
#  Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.
#Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

notas = input('Digite a nota dos alunos separada por vírgula: ').split(',')

float_notas = map(float,notas)

media = sum(float_notas)/len(notas)

print(f'Média final da turma:{media:.2f}')

#10-Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
# Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. 
#Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(',')

for i in range(0,len(dados),3):
     print (f'Aluno: {dados[i]}\nIdade:{dados[i +1]}\n Nota: {dados[i+2]}')

