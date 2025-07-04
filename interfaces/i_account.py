from utils import *
from models_db import insert_account, account_in_db, get_acc

class IAccount:
    def __init__(self, cursor):
        self.cursor = cursor
        self.acc_options = ["Voltar", "Criar conta", "Entrar em conta"]
        self.account = None
    

    def validate(self, username, password):
        return account_in_db(username, password)


    def register_menu(self, acc_type:int):
        """acc_type: tipo de conta (0 instituição, 1 pesquisador, 2 estudante, 3 colaborador externo)"""
        clear()
        print("==================\n"
              "     Registro     \n"
              "==================\n\n"
              "Insira o nome de usuário (até 15 caracteres):")

        username = input()
        if len(username) == 0 or len(username) > 15:
            input("Nome inválido")
            return

        print("Insira a senha (exatamente 8 caracteres):")

        password = input()
        if len(password) != 8 or " " in password:
            input("Senha inválida")
            return

        success = insert_account(self.cursor, acc_type, username, password)
        if not success:
            input("\nFalha na criação da conta!")
            return

        input("\nConta criada com sucesso!")


    def login_menu(self):
        clear()
        print("==================\n"
                "       Login      \n"
                "==================\n\n"
                "Nome de usuário:")
        username = input()
        print("Senha:")
        password = input()


        acc_info = get_acc(self.cursor, username, password)

        if not acc_info:
            input("Não foi possível fazer login. Tente novamente.")
            return

        self.account = {
            "acc_id" : acc_info[0],
            "acc_type" : acc_info[1]
        }

        input("Login efetuado com sucesso!")
        self.go_to_menu(self.account)

    def go_to_menu(self, account):
        """account: dicionário de conta, com id e tipo de conta"""
        # prosseguir pra tela de perfil do usuário
        """
        match (acccount["acc_type"]):
            case 0:
                #login instit.
            case 1:
                #pesquisador
            case 2:
                #estudante
            case 3:
                #col. externo
            case _:
                input("Falha ao acessar página de usuário")
                return"""
        return



    def institution_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "   Conta - Instituição    \n"
                  "==========================\n\n"
                  "Escolha uma opção:")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case 0:
                    return
                case 1:
                    self.register_menu(0)
                case 2:
                    self.login_menu()
                case _:
                    input("Opção inválida.")


    def researcher_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "   Conta - Pesquisador    \n"
                  "==========================\n\n"
                  "Escolha uma opção:")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case 0:
                    return
                case 1:
                    self.register_menu(1)
                case 2:
                    self.login_menu()
                case _:
                    input("Opção inválida.")

    def student_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "    Conta - Estudante     \n"
                  "==========================\n\n"
                  "Escolha uma opção:")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case 0:
                    return
                case 1:
                    self.register_menu(2)
                case 2:
                    self.login_menu()
                case _:
                    input("Opção inválida.")


    def extern_menu(self):
        while True:
            clear()
            print("==========================\n"
                  " Conta - Colaborador Ext.  \n"
                  "==========================\n\n"
                  "Escolha uma opção:")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case 0:
                    return
                case 1:
                    self.register_menu(3)
                case 2:
                    self.login_menu()
                case _:
                    input("Opção inválida.")


    def run(self):
        options = ["Voltar", "Instituição", "Pesquisador", "Estudante", "Colaborador Externo"]

        while True:
            clear()
            print("==========================\n"
                  "     Gerenciar Conta      \n"
                  "==========================\n\n"
                  "Selecione o tipo de conta:")

            print_menu(options)
            choice = input_choice(len(options))
            
            if choice == -1:
                input("Opção inválida.")

            if choice == 0:
                return
            
            match(choice):
                case 1:
                    self.institution_menu()

                case 2:
                    self.researcher_menu()

                case 3:
                    self.student_menu()

                case 4:
                    self.extern_menu()
