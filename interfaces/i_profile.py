from utils import *
from interfaces.i_search import ISearch

class IProfile:
    def __init__(self, cursor, account):
        self.cursor = cursor
        self.account = account
        
        match (account["type"]):
            case 0:
                self.type = "instituição"
            case 1:
                self.type = "pesquisador"
            case 2:
                self.type = "estudante"
            case 3:
                self.type = "colaborador_externo"

    def setup_profile(self):
        clear()
        # TODO: inserir localidade nos membros
        match (self.account["type"]):
            case 0:
                input("perfil de instituição")
            case 1:
                input("perfil de pesquisador")
            case 2:
                input("perfil de estudante")
            case 3:
                input("perfil de colaborador ext.")


    def update_institution(self):
        clear()
        print_menu(title="Atualizar conta", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")
        
        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) == 0 or len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_abbreviation = input("Sigla (até 10 caracteres): ")
        if len(new_abbreviation) == 0 or len(new_abbreviation) > 10:
            input("\nSigla inválida.")
            return

        new_legal_category = input("Natureza jurídica: ")
        if len(new_legal_category) == 0 or len(new_legal_category) > 20:
            input("\nNatureza jurídica inválida.")
            return

        new_uf = input("Nova UF: ")
        if len(new_uf) != 2:
            input("\nUF inválida.")
            return

        new_location = input("Nova localidade: ")
        if len(new_location) == 0 or len(new_location) > 30:
            input("\nLocalidade inválida.")
            return

        new_invested_amount = input("Recursos investidos (em centavos): ")
        if not new_invested_amount.isnumeric():
            print("Quantia inválida.")
            return
        
        new_description = input("Nova descrição: ")

        # inserir

        input("\nAtualização realizada com sucesso.")
    
    def update_researcher(self):
        clear()
        print_menu(title="Atualizar conta", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) == 0 or len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) == 0 or len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return
        
        new_description = input("Nova descrição: ")

        new_department = input("Departamento: ")
        if len(new_department) == 0 or len(new_department) > 30:
            input("\nDepartamento inválido.")
            return

        # inserir
        
        input("\nAtualização realizada com sucesso.")


    def update_student(self):
        clear()
        print_menu(title="Atualizar conta", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) == 0 or len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) == 0 or len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return
        
        new_description = input("Nova descrição: ")

        new_registration = input("Matrícula: ")
        if len(new_registration) == 0 or len(new_registration) > 30:
            input("\nMatrícula inválida.")
            return

        # inserir
        
        input("\nAtualização realizada com sucesso.")


    def update_extern(self):
        clear()
        print_menu(title="Atualizar conta", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) == 0 or len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) == 0 or len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return
        
        new_description = input("Nova descrição: ")

        # inserir
        
        input("\nAtualização realizada com sucesso.")


    def run(self):
        while True:
            clear()
            options = ["Sair da conta", "Atualizar conta", "Pesquisar"]
            print_menu(options, f"{self.account["name"]}", "Escolha uma opção:")

            choice = input_choice(len(options))

            match (choice):
                case 0:
                    return
                case 1:
                    match (self.account["type"]):
                        case 0:
                            self.update_institution()
                        case 1:
                            self.update_researcher()
                        case 2:
                            self.update_student()
                        case 3:
                            self.update_extern()
                case 2:
                    i_search = ISearch(self.cursor, self.type)
                    i_search.menu()
                case _:
                    print("Opção inválida.")
