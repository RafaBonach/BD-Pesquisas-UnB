from utils import *
from models_db import insert_account, account_in_db, get_acc
from interfaces.i_profile import IProfile

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
        print_menu(title="Registro", description="Insira o nome de usuário (até 15 caracteres):")

        username = input()
        if len(username) == 0 or len(username) > 15:
            input("Nome inválido")
            return

        print("Insira a senha (exatamente 6 caracteres):")

        password = input()
        if len(password) != 6 or " " in password:
            input("Senha inválida.")
            return

        success = insert_account(self.cursor, acc_type, username, password)
        if not success:
            input("\nFalha na criação da conta!")
            return

        input("\nConta criada com sucesso!")


    def login_menu(self):
        clear()
        print_menu(title="Login")

        print("Nome de usuário:")
        username = input()
        print("Senha:")
        password = input()

        acc_info = get_acc(self.cursor, username, password)

        if not acc_info:
            input("Não foi possível fazer login. Tente novamente.")
            return

        self.account = {
            "id" : acc_info[0],
            "type" : acc_info[1],
            "name" : acc_info[2]
        }

        input("Login efetuado com sucesso!")
        self.go_to_profile(self.cursor, self.account)


    def go_to_profile(self, cursor, account):
        """account: dicionário de conta, com id e tipo de conta"""
        profile = IProfile(cursor, account)
        profile.setup_profile()
        profile.run()

    def institution_menu(self):
        while True:
            clear()
            print_menu(self.acc_options, "Conta - Instituição", "Escolha uma opção:")

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
            print_menu(self.acc_options, title="Conta - Pesquisador", description="Escolha uma opção:")

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
            print_menu(self.acc_options, "Conta - Estudante", "Escolha uma opção:")

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
            print_menu(self.acc_options, "Conta - Colaborador Ext.", "Escolha uma opção:")

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
            print_menu(options, "Gerenciar Conta", "Selecione o tipo de conta:")
            
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
