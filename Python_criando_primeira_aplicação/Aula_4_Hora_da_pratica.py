# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

dados = {'nome': 'Maria',
         'idade': '25',
         'cidade': 'Rio de Janeiro'}

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

dados['idade'] = '27'

# Adicione um campo de profissão para essa pessoa;

dados['profissão'] = 'professora'

# Remova um item do dicionário.

dados.pop('cidade')

print(dados)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

quadrados = {i: i**2 for i in range (1,6)}
print(quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

comidas = {'banana': 'fruta',
           'bolo': 'sobremesa',
           'beterraba' : 'legume',
           'alface':'vegetal'
}

chave = input('Digite o nome da chave que deseja pesquisar: ')
print(chave)

if chave in comidas:
    print(f'A chave {chave} existe no dicionário')
else:
    print('A chave {chave} não existe no dicionário.')


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = '''Por que mentias leviana e bela ?
Se minha face pálida sentias
Queimada pela febre, e se minha vida
Tu vias desmaiar, por que mentias ?'''

palavras_frase = frase.split()
contagem_palavras = {}

for palavra in palavras_frase:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print(contagem_palavras)
