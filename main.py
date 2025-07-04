'''
    Esse será o arquivo principal do projeto.
'''
from utils import *
from backend_db import *
from interfaces.i_account import IAccount
from interfaces.i_search import ISearch
import time

# Executa o arquivo SQL para criar as tabelas no banco de dados
if __name__ == "__main__": # Se o arquivo for executado diretamente, executa o código abaixo
    print("==========================\n"
            " Gerenciador de Projetos  \n"
            "    de Pesquisa da UnB    \n"
            "==========================\n\n"
            "Bem-vindo ao sistema de gerenciamento de projetos de pesquisa da UnB!\n"
            "Para começar, precisamos garantir que o banco de dados esteja configurado.\n"
            "Por favor, insira a senha do banco de dados PostgreSQL:\n")
    password = input("Senha: ")

    create_database(password=password, db_name='db_pesquisas')
    create_tables_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_db.sql')
    conexao = connect_to_database(database_name='db_pesquisas', password=password)
    
    input()
    
    options = ["Sair", "Gerenciar conta", "Pesquisar projetos e pesquisadores"]

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

        match(choice):
            case 1:
                i_acc = IAccount(conexao.cursor())
                i_acc.run()
            
            case 2:
                i_search = ISearch(conexao.cursor())
                i_search.menu()
