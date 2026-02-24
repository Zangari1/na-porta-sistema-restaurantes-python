import os

restaurantes = [{'nome':'McDonalds', 'categoria':'Fast Food', 'ativo':False}, 
                {'nome':'Figueira Rubayat', 'categoria':'Churrascaria', 'ativo':True},
                {'nome':'Makoto', 'categoria':'Japonês', 'ativo':False}]

def exibir_nome():
    print("""
█▄░█ ▄▀█   █▀█ █▀█ █▀█ ▀█▀ ▄▀█
█░▀█ █▀█   █▀▀ █▄█ █▀▄ ░█░ █▀█
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes cadastrados')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def encerrar_app():
    exibir_subtitulo('Encerrando o App...')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()

def exibir_subtitulo(texto):
    '''
    Esta Função é responsável por limpar o terminal e exibir o subtitulo estilizado
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''
    Esta Função é responsável por realizar o cadastro de novos restaurantes

    Inputs: 
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    - Imprime que o restaurante foi cadastrado com sucesso
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu()

def listar_restaurantes():
    '''
    Esta Função é responsável por Listar os restaurantes cadastrados
    '''
    exibir_subtitulo('Listando restaurantes')

    legenda = f"- {'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}"
    linha = '-' * (len(legenda) + 10)

    print(legenda)
    print(linha)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu()

def status_restaurante():
    '''
    Esta Função é responsável por alternar o status do restaurante (Ativado/Desativado)
    '''
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado. ')
            
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Selecione uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            status_restaurante()
        elif opcao_escolhida == 4: 
            encerrar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()