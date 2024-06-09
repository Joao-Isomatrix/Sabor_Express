from Mod.restaurante import Restaurante
import os

"""restaurante_praça = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'mexicana')
restaurante_japones = Restaurante('japa', 'japnesa')

restaurante_mexicano.alternar_estado()
restaurante_mexicano.recerber_avaliacao('Joao', 8)
restaurante_mexicano.recerber_avaliacao('Pedro', 5)
restaurante_mexicano.recerber_avaliacao('julia', 8)
restaurante_mexicano.recerber_avaliacao('julia', 9)"""




#função responsavel por criar a logo
def exibir_nome_do_programa():      
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
#Exibe as opções na tela inicial
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()
#mensagem de erro recorrente que retorna para a tela inicial
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Função para exibir um subtitulo para cada função principal em tela
        ela deve receber o {texto} contendo o nome da função principal para ser
        exibida corretamente '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()            
        elif opcao_escolhida == 3: 
            ativar_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de restaurante')
    nome = input('Qual o nome do restaurante que deseja cadastrar?')
    categoria = input('Qual categoria o restaurante será?')
    Restaurante(nome, categoria)
    os.system('cls')
    print(f'O restaurante {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Lista de restaurantes disponiveis')
    if Restaurante.restaurantes == []:
        print ('não há restaurantes para exibir')
        voltar_ao_menu_principal()
    else:        
        Restaurante.listar_restaurantes()
        voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')   
    if Restaurante.restaurantes == []:
        print ('não há restaurantes para exibir')
        voltar_ao_menu_principal()
    else:
        restaurantes_disponiveis =  Restaurante.restaurantes
        
        print(f'Restaurantes disponiveis para realizar ativação: \n')
        print (f'{"RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(20)} | {"ATIVO"}')
        for restaurante in restaurantes_disponiveis:
            print (f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}' )        

        restaurante_escolhido = input('Qual restaurante deseja ativar?')
        
        restaurante_encontrado = False
        for restaurante in restaurantes_disponiveis:
            if restaurante_escolhido == restaurante._nome:   
                restaurante_encontrado = True         
                Restaurante.alternar_estado(restaurante)
                os.system('cls')
                print(f'O restaurante {restaurante._nome} foi ativado com sucesso')
                voltar_ao_menu_principal()            
        if restaurante_encontrado == False:
            input('restaurante não encontrado, verifique se o nome está correto!')            
            voltar_ao_menu_principal()

def main():
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()