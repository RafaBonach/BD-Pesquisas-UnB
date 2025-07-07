from utils import *
from interfaces.i_search import ISearch
from models_db import *
from telas_db import *

class IProfile:
    def __init__(self, cursor, account):
        self.cursor = cursor
        self.account = account
        _t = 0 if account["type"] == 1 else 1
        self.info = get_entity_info(self.cursor, _t, id=self.account["id_entity"])

        match (account["type"]):
            case 1:
                self.type = "instituição"
            case 2:
                self.type = "pesquisador"
            case 3:
                self.type = "estudante"
            case 4:
                self.type = "colaborador_externo"


    def update_institution_menu(self):
        clear()
        print_menu(title="Atualizar - Instituição", description="Preencha os campos:\n")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) > 40:
            print("\nNome inválido.")
            return

        new_acronym = input("Sigla (até 10 caracteres): ")
        if len(new_acronym) > 10:
            print("\nSigla inválida.")
            return

        new_legal_category = input("Natureza jurídica: ")
        if len(new_legal_category) > 20:
            print("\nNatureza jurídica inválida.")
            return

        new_uf = input("Nova UF: ")
        if len(new_uf) > 0 and len(new_uf) != 2:
            print("\nUF inválida.")
            return

        new_location = input("Nova localidade: ")
        if len(new_location) > 30:
            print("\nLocalidade inválida.")
            return

        new_invested_amount = input("Recursos investidos (em centavos): ")
        if len(new_invested_amount) != 0 and not new_invested_amount.isnumeric():
            print("Quantia inválida.")
            return
        
        new_description = input("Nova descrição: ")

        if not atualizar_instituicao(self.cursor, self.info[0], new_name, new_acronym, new_legal_category, new_uf, new_location, new_invested_amount, new_description):
            input("\nNada para atualizar.")
            return True

        input("\nAtualização realizada com sucesso.")
        return True


    def update_researcher_menu(self):
        clear()
        print_menu(title="Atualizar - Pesquisador", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return
        
        new_description = input("Nova descrição: ")

        new_department = input("Departamento: ")
        if len(new_department) > 30:
            input("\nDepartamento inválido.")
            return


        if not atualizar_membro(self.cursor, self.account["id_entity"], new_name, new_qualification, new_description, new_department, "", ""):
            input("\nNada para atualizar.")
            return True

        input("\nAtualização realizada com sucesso.")
        return True


    def update_student_menu(self):
        clear()
        print_menu(title="Atualizar - Estudante", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return

        new_description = input("Nova descrição: ")

        new_registration = input("Matrícula: ")
        if len(new_registration) > 30:
            input("\nMatrícula inválida.")
            return

        new_course = input("Curso: ")

        if not atualizar_membro(self.cursor, self.account["id_entity"], new_name, new_qualification, new_description, "", new_registration, new_course):
            input("\nNada para atualizar.")
            return True

        input("\nAtualização realizada com sucesso.")
        return True


    def update_extern_menu(self):
        clear()
        print_menu(title="Atualizar conta", description="Preencha os campos a serem atualizados:\n(Deixe em branco para manter o registro atual)")

        new_name = input("Nome (até 40 caracteres): ")
        if len(new_name) > 40:
            input("\nNome inválido.")
            return

        new_qualification = input("Titulação (até 10 caracteres): ")
        if len(new_qualification) > 15:
            input("\nTitulação inválida.")
            return

        new_description = input("Nova descrição: ")

        if not atualizar_membro(self.cursor, self.account["id_entity"], new_name, new_qualification, new_description, "", "", ""):
            input("\nNada para atualizar.")
            return True
        
        input("\nAtualização realizada com sucesso.")
        return True


    def delete_account(self):
        clear()
        print_menu(title="DELETAR CONTA", description="\nDeletar sua conta a removerá dos registros de seus projetos\nVocê tem certeza que quer deletar sua conta? (S/N)")
        choice = input().lower()

        if choice == "s":
            if self.account["type"] == 1:
                del_ent = deletar_instituicao(self.cursor, self.account["id_entity"])
            elif self.account["type"] <= 4:
                del_ent = deletar_membro(self.cursor, self.account["id_entity"])
            
            if not del_ent:
                input("\nFalha ao deletar conta")
                return

            if delete_acc(self.cursor, self.account["id"]):
                input("\nConta deletada com sucesso.")
                return True


    def run(self):
        while True:
            clear()
            options = ["Sair da conta", "Atualizar conta", "Deletar conta", "Pesquisar"]
            print_menu(options, f"{self.account["name"]}", "Escolha uma opção:")

            choice = input_choice(len(options))

            match (choice):
                case 0:
                    return
                case 1:
                    match (self.account["type"]):
                        case 1:
                            suc = self.update_institution_menu()
                        case 2:
                            suc = self.update_researcher_menu()
                        case 3:
                            suc = self.update_student_menu()
                        case 4:
                            suc = self.update_extern_menu()
                        
                    if not suc:
                        input("\nFalha na atualização da conta.")
                case 2:
                    if self.delete_account():
                        return "delete"
                # pesquisa
                case _:
                    print("Opção inválida.")
