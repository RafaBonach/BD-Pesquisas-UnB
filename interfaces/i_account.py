from utils import *
from models_db import insert_account, account_in_db, get_acc, delete_acc, link_acc, link_location
from interfaces.i_profile import IProfile

class IAccount:
    def __init__(self, cursor):
        self.cursor = cursor
        self.acc_options = ["Voltar", "Criar conta", "Entrar em conta"]
        self.account = None


    def validate(self, username, password):
        return account_in_db(username, password)


    def register_menu(self):
        clear()

        # escolher o tipo de conta
        options = ["Cancelar", "Instituição", "Pesquisador", "Estudante", "Colaborador Externo"]
        print_menu(options, "Registro", "Escolha o tipo de conta:")

        choice = input_choice(len(options))

        if choice == 0:
            return
        elif choice > 0 and choice < 5:
            acc_type = choice
        else:
            input("\nOpção inválida.")
            return

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

        # inserir registro na tabela de contas
        success = insert_account(self.cursor, acc_type, username, password)
        if not success:
            input("\nEsse nome de usuário já está sendo usado. Falha na criação de conta!")
            return
        elif success == -1:
            input("\nFalha na criação da conta!")
            return

        acc_id = get_acc(self.cursor, username, password)[0]

        entity_id = None
        # criar entidade
        match (choice):
            case 1:
                entity_id = self.create_institution_menu()
            case 2:
                entity_id = self.create_researcher_menu()
            case 3:
                entity_id = self.create_student_menu()
            case 4:
                entity_id = self.create_extern_menu()


        # se criação da entidade falhar, remover conta
        if not entity_id:
            delete_acc(self.cursor, acc_id)

            input("\nFalha na criação de conta.")
            return

        # ligar conta e entidade
        if not link_acc(self.cursor, int(acc_id), entity_id):
            delete_acc(self.cursor, acc_id)

            input("\nFalha na criação de conta.")
            return

        input(f"\nConta de tipo {options[acc_type]} criada com sucesso!")


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
        """account: dicionário de conta, com id, tipo de conta e nome"""

        profile = IProfile(cursor, account)
        profile.run()


    def set_location(self):
        country = input("País de origem: ")
        if not check_max_len(country, 45):
            input("\nPaís inválido.")
            return False

        uf = input("UF em que reside: ")
        if len(uf) != 2:
            input("\nUF inválida.")
            return False

        city = input("Cidade em que reside: ")
        if not check_max_len(city, 45):
            input("\nCidade inválida.")
            return False

        link_location(self.account["id"])
        return True


    def create_institution_menu(self):
        clear()
        print_menu(title="Registro - Instituição", description="Preencha os campos:\n")
        
        name = input("Nome (até 40 caracteres): ")
        if not check_max_len(name, 40):
            print("\nNome inválido.")
            return None

        abbreviation = input("Sigla (até 10 caracteres): ")
        if not check_max_len(abbreviation, 10):
            print("\nSigla inválida.")
            return None

        legal_category = input("Natureza jurídica: ")
        if not check_max_len(legal_category, 20):
            print("\nNatureza jurídica inválida.")
            return None

        uf = input("Nova UF: ")
        if len(uf) == 0 or  len(uf) != 2:
            print("\nUF inválida.")
            return None

        location = input("Nova localidade: ")
        if not check_max_len(location, 30):
            print("\nLocalidade inválida.")
            return None

        invested_amount = input("Recursos investidos (em centavos): ")
        if len(legal_category) == 0 or not invested_amount.isnumeric():
            print("\nQuantia inválida.")
            return None

        description = input("Nova descrição: ")
        if len(description) == 0:
            print("\nDescrição inválida.")

        # insert

        # get id

        input("\nRegistro realizado com sucesso.")
        # return id


    def create_researcher_menu(self):
        clear()
        print_menu(title="Registro - Pesquisador", description="Preencha os campos:\n")

        name = input("Nome (até 40 caracteres): ")
        if not check_max_len(name, 40):
            print("\nNome inválido.")
            return

        qualification = input("Titulação (até 15 caracteres): ")
        if not check_max_len(qualification, 15):
            print("\nTitulação inválida.")
            return

        description = input("Nova descrição: ")
        if len(description) == 0:
            print("\nDescrição inválida.")
            return

        department = input("Departamento: ")
        if not check_max_len(department, 30):
            print("\nDepartamento inválido.")
            return

        # insert

        # get id

        input("\nRegistro realizada com sucesso.")
        return True
    

    def create_student_menu(self):
        clear()
        print_menu(title="Registro - Estudante", description="Preencha os campos:\n")

        name = input("Nome (até 40 caracteres): ")
        if not check_max_len(name, 40):
            print("\nNome inválido.")
            return False

        qualification = input("Titulação (até 15 caracteres): ")
        if not check_max_len(qualification, 15):
            print("\nTitulação inválida.")
            return False

        description = input("Nova descrição: ")
        if len(description) == 0:
            print("\nDescrição inválida.")
            return False

        registration = input("Matrícula: ")
        if not registration.isnumeric() or len(registration) != 9:
            print("\nMatrícula inválida.")
            return False

        # insert

        # get id

        input("\nRegistro realizado com sucesso.")
        return True


    def create_extern_menu(self):
        clear()
        print_menu(title="Registro - Colab. Ext.", description="Preencha os campos:\n")

        new_name = input("Nome (até 40 caracteres): ")
        if not check_max_len(new_name, 40):
            print("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 15 caracteres): ")
        if not check_max_len(new_qualification, 15):
            print("\nTitulação inválida.")
            return

        new_description = input("Nova descrição: ")
        if len(new_description) == 0:
            print("\nDescrição inválida.")

        # insert

        # get id

        input("\nRegistro realizado com sucesso.")
        return True


    def run(self):
        options = ["Voltar", "Criar conta", "Entrar em conta"]

        while True:
            clear()
            print_menu(options, "Gerenciar Conta", "Selecione uma opção:")

            choice = input_choice(len(options))

            match(choice):
                case 0:
                    return
                case 1:
                    self.register_menu()
                case 2:
                    self.login_menu()
                case _:
                    input("\nOpção inválida.")
