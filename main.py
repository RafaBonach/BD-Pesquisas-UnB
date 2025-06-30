'''
    Esse será o arquivo principal do projeto.
'''
from utils import *
from interfaces.i_account import IAccount

# Executa o arquivo SQL para criar as tabelas no banco de dados
if __name__ == "__main__": # Se o arquivo for executado diretamente, executa o código abaixo
    print("Executando arquivo SQL para criar tabelas...")
    print("Tabelas criadas com sucesso!")
    
    options = ["Sair", "Gerenciar conta"]

    while True:
        clear()
        print("==========================\n"
              " Gerenciador de Projetos  \n"
              "    de Pesquisa da UnB    \n"
              "==========================\n\n"
              "Selecione uma opção:")

        print_menu(options)

        choice = input_choice(len(options))
        
        if choice == -1:
            input("Opção inválida.")

        elif choice == 0:
            input("Fim do programa.")
            clear()
            exit()

        elif choice == 1:
            i_acc = IAccount()
            i_acc.run()
