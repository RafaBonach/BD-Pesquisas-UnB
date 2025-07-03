from utils import *

class IAccount:
    def __init__(self):
        self.acc_options = ["Voltar", "Criar conta", "Entrar em conta"]
    

    def validate(self, acc_type, username, password):
        """acc_type: tipo de conta (0 instituição, 1 pesquisador, 2 estudante, 3 colaborador externo)"""
        # checar se nome de usuário e senha constam nos registros
        return True


    def create_account(self, acc_type:int, username, passord):
        """acc_type: tipo de conta (0 instituição, 1 pesquisador, 2 estudante, 3 colaborador externo)"""
        # criar conta no BD?
        return True


    def register_menu(self, acc_type:int):
        """acc_type: tipo de conta (0 instituição, 1 pesquisador, 2 estudante, 3 colaborador externo)"""
        clear()
        print("==================\n"
              "     Registro     \n"
              "==================\n\n"
              "Insira o nome de usuário: ")
        username = input()
        print("Insira a senha: ")
        password = input()

        success = self.create_account(acc_type, username, password)
        if not success:
            input("Falha na criação da conta.")

        input("\nConta criada com sucesso!")


    def login_menu(self, acc_type):
        """acc_type: tipo de conta (0 instituição, 1 pesquisador, 2 estudante, 3 colaborador externo)"""
        clear()
        print("==================\n"
                "       Login      \n"
                "==================\n\n"
                "Nome de usuário: ")
        username = input()
        print("Senha: ")
        password = input()

        if not self.validate(acc_type, username, password):
            print("Não foi possível fazer login. Tente novamente.")

        # logar


    def institution_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "   Conta - Instituição    \n"
                  "==========================\n\n"
                  "Escolha uma opção: ")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case -1:
                    input("Opção inválida.")
                case 0:
                    return
                case 1:
                    self.register_menu(0)
                case 2:
                    self.login_menu(0)


    def researcher_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "   Conta - Pesquisador    \n"
                  "==========================\n\n"
                  "Escolha uma opção: ")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case -1:
                    input("Opção inválida.")
                case 0:
                    return
                case 1:
                    self.register_menu(1)
                case 2:
                    self.login_menu(1)

    def student_menu(self):
        while True:
            clear()
            print("==========================\n"
                  "    Conta - Estudante     \n"
                  "==========================\n\n"
                  "Escolha uma opção: ")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case -1:
                    input("Opção inválida.")
                case 0:
                    return
                case 1:
                    self.register_menu(2)
                case 2:
                    self.login_menu(2)


    def extern_menu(self):
        while True:
            clear()
            print("==========================\n"
                  " Conta - Colaborador Ext.  \n"
                  "==========================\n\n"
                  "Escolha uma opção: ")
            print_menu(self.acc_options)
            choice = input_choice(len(self.acc_options))

            match(choice):
                case -1:
                    input("Opção inválida.")
                case 0:
                    return
                case 1:
                    self.register_menu(3)
                case 2:
                    self.login_menu(3)


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
