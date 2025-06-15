import os

restaurantes = restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
 '''Exibe o nome do programa'''
 print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')

def exibir_opcoes():
 ''' Exibe as opções do programa'''
 print('1.Castrar restaurante')
 print('2.Listar restaurante')
 print('3.Alternar estado do restaurante')
 print('4.Sair\n')

def finalizar_app():   
    '''Finaliza o app'''
    exibir_subtitulo('Finalizar app\n')

def voltar_menu_principal():
  '''Retona ao menu principal, exibindo nome do programa e opçoes de escolha'''
  input('\n\n Digite uma tecla para voltar ao menu inicial')
  main()

def exibir_subtitulo(texto):
  '''Exibe o titulo da opção escolhida'''
  os.system('cls')
  linha = '*' * len(texto)
  print(linha)
  print(texto)
  print(linha)
  print()
  

def opcao_invalida():
   '''Mostrar uma mensagem quando um valor digitado não está na lista de opções'''
   print('Opção inválida.\n')
   voltar_menu_principal()

def cadastrar_novo_restaurante():
  ''' Esssa função é responsavel por cadastrar um novo restaurante
  
  Input:
- Nome do restaurante
- Categoria

Output:
- Adiciona um novo restaurante à lista de restaurantes
    
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
  categoria = input(f'Digite o nome da caregoria do restaurante {nome_do_restaurante}: ')
  dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
  restaurantes.append(dados_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
  voltar_menu_principal()

def listar_restaurante():
  '''Mostra uma lista de todos os restaurantes cadastrados'''
  exibir_subtitulo('Listando restaurantes')
  print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo'] else 'desativado'
    print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
   
  voltar_menu_principal()

def alternar_estado_restaurante():
    '''Alternar o estado do restaurante entre ativo e desativado'''
    exibir_subtitulo('Alternando estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado = False
    for restaurante in restaurantes():
      if nome_restaurante == restaurante['nome']:
       restaurante_encontrado = True
       restaurante['ativo'] = not restaurante['ativo']
       mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
    
    if not restaurante_encontrado:
     print('O restaurante não foi encontrado.')
    voltar_menu_principal
    

def escolher_opcao():
 '''Seleciona a opção escolhida das opçoes '''
 try:
   opcao_escolhida = int(input('Escolha uma opção: '))
   if opcao_escolhida == 1:
     cadastrar_novo_restaurante()
   elif opcao_escolhida == 2:
     listar_restaurante()
   elif opcao_escolhida == 3:
     alternar_estado_restaurante()
   elif opcao_escolhida == 4:
    finalizar_app()
   else :
    opcao_invalida()
 except:
    opcao_invalida()

def main():
    '''Reinicia o programa'''
    print('Finalizando o app\n')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()