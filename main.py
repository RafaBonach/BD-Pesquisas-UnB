'''
    Esse será o arquivo principal do projeto.
'''
from utils import *
from backend_db import *
from interfaces.i_account import IAccount
from interfaces.i_search import *
from interfaces.i_project import IProject
import time
import getpass

# Executa o arquivo SQL para criar as tabelas no banco de dados
if __name__ == "__main__": # Se o arquivo for executado diretamente, executa o código abaixo
    while True:
        clear()
        print("==========================\n"
                " Gerenciador de Projetos  \n"
                "    de Pesquisa da UnB    \n"
                "==========================\n\n"
                "Bem-vindo ao sistema de gerenciamento de projetos de pesquisa da UnB!\n"
                "Para começar, precisamos garantir que o banco de dados esteja configurado.\n"
                "Por favor, insira a senha do banco de dados PostgreSQL:\n")
        password = getpass.getpass("Senha: ")
        
        create_database(password=password, db_name='db_pesquisas')
        create_tables_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_db.sql')
        create_procedures_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_procedure.sql')
        conexao = connect_to_database(database_name='db_pesquisas', password=password)
    
        if isinstance(conexao, Exception):
            erro_str = str(conexao)

            if "Authentication failed" in erro_str or "HY000" in erro_str:
                print("\n🔐 ERRO DE AUTENTICAÇÃO:\n"
                      "\n   A senha fornecida está incorreta!"
                      "\n   Verifique suas credenciais do PostgreSQL.")
                
            elif "database" in erro_str.lower() and "does not exist" in erro_str.lower():
                print("🗄️ ERRO DE BANCO DE DADOS:")
                print("   O banco de dados não foi encontrado!")

            elif "connection" in erro_str.lower() or "server" in erro_str.lower():
                print("🌐 ERRO DE CONEXÃO:")
                print("   Não foi possível conectar ao servidor PostgreSQL!")
                print("   Verifique se o PostgreSQL está rodando.")

            else:
                print(f"❌ Erro desconhecido: {conexao}")


            verificador = input("\nPressione E para sair ou ENTER para tentar novamente: ")
            if verificador.strip().upper() == 'E':
                clear()
                print("Saindo do programa...")
                exit()
        else:
            print("\n✅ Conexão bem-sucedida com o banco de dados 'db_pesquisas'!\n")
            print("🚀 Iniciando programa!")
            break
        
        time.sleep(2)
    
    options = ["Sair", "Gerenciar conta", "Pesquisar projetos e pesquisadores", "Gerenciar projetos"]

    while True:
        #clear()
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
            print("Fim do programa.")
            time.sleep(2)
            clear()
            exit()

        match(choice):
            case 1:
                i_acc = IAccount(conexao.cursor())
                i_acc.run()
            
            case 2:
                menu(conexao.cursor())
            
            case 3:
                i_proj = IProject(conexao.cursor())
                i_proj.run()