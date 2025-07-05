from utils import *
from models_db import *
import time
from datetime import datetime

class IProject:
    def __init__(self, cursor):
        self.cursor = cursor

    def title(self, action):
        clear()
        projeto = Projeto()
        match action:
            case 'c':
                print("==========================\n"
                      "   Criador de Projetos    \n"
                      "==========================\n\n"
                    "\nInsira as informações a baixo\n")
                titulo = input("Título do projeto: ")
                data_inicio = input("Data de início (AAAA-MM-DD): ")
                data_final = input("Data de término (AAAA-MM-DD): ")
                resumo = input("Resumo do projeto (opcional): ")
                projeto.titulo = titulo
                projeto.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date() if data_inicio else None
                projeto.data_final = datetime.strptime(data_final, '%Y-%m-%d').date() if data_final else None
                projeto.resumo = resumo
                time.sleep(1)

                clear()
                lista_t_proj = projeto.lista_t_projetos(self.cursor)
                print("Tipos de projeto disponíveis:")
                print(f"{'ID':<5} {'Nome':<20}")
                l_t_proj = {}
                for tp in lista_t_proj:
                    l_t_proj[tp[0]] = tp[1]
                    print(f"{tp[0]} - {tp[1]}")
                id_tipo_proj = input("Digite o ID do tipo de projeto\nou selecine qualquer tecla para criar um novo projeto: ")

                if id_tipo_proj.isdigit() and int(id_tipo_proj) in l_t_proj:
                    projeto.id_t_projeto = int(id_tipo_proj)
                    return projeto
                else:
                    clear()
                    print("==========================\n"
                        "Criador de Tipos de Projetos\n"
                        "==========================\n\n"
                        "\nInsira a informação a baixo\n")
                    nome_tipo = input("Nome do tipo de projeto: ")
                    projeto.nome_tipo_projeto = nome_tipo
                    tipo_proj = projeto.lista_t_projetos(self.cursor)
                    for tp in tipo_proj:
                        if tp[1].upper() == nome_tipo.upper():
                            projeto.id_t_projeto = tp[0]
                    time.sleep(1)
                    return projeto
                
                """
==============================================================================================
                Agora, é preciso criar as conexões com as outras tabelas
==============================================================================================
                """

            case 'l':
                print("==========================\n"
                      "   Lista de Projetos    \n"
                      "==========================\n\n")
                return projeto
                
            case 'u':
                clear()
                print("==========================\n"
                      "   Atualizador de Projetos    \n"
                      "==========================\n\n"
                      "\nLista de projetos disponíveis:\n")
                lista_projetos = projeto.lista_projetos(self.cursor)
                if not lista_projetos:
                    print("Nenhum projeto encontrado.\n")
                    print("Não é possivel atualizar um projeto sem antes criá-lo.\n")
                    return None
                else:
                    self.list_projects(projeto)
                id_projeto = input("\n\nDigite o ID do projeto que deseja atualizar: ")
                if not id_projeto.isdigit():
                    print("ID inválido.")
                    return None
                projeto.cod_projeto = int(id_projeto)
                titulo = input("Novo título do projeto (deixe em branco para não alterar): ")
                if titulo:
                    projeto.titulo = titulo
                data_inicio = input("Nova data de início (AAAA-MM-DD) (deixe em branco para não alterar): ")
                if data_inicio:
                    projeto.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date() if data_inicio else None
                data_final = input("Nova data de término (AAAA-MM-DD) (deixe em branco para não alterar): ")
                if data_final:
                    projeto.data_final = datetime.strptime(data_final, '%Y-%m-%d').date() if data_final else None
                resumo = input("Novo resumo do projeto (deixe em branco para não alterar): ")
                if resumo:
                    projeto.resumo = resumo
                
                clear()
                lista_t_proj = projeto.lista_t_projetos(self.cursor)
                print("Tipos de projeto disponíveis:")
                print(f"{'ID':<5} {'Nome':<20}")
                l_t_proj = {}
                for tp in lista_t_proj:
                    l_t_proj[tp[0]] = tp[1]
                    print(f"{tp[0]} - {tp[1]}")
                id_tipo_proj = input("Digite o ID do tipo de projeto, N para não alterar\nou selecine qualquer tecla para criar um novo projeto: ")

                if id_tipo_proj.isdigit() and int(id_tipo_proj) in l_t_proj:
                    projeto.id_t_projeto = int(id_tipo_proj)
                    return projeto
                elif id_tipo_proj.strip().upper() == 'N':
                    print("\nTipo de projeto não alterado.\n")
                    return projeto
                else:
                    clear()
                    print("==========================\n"
                        "Atualizador de Tipos de Projetos\n"
                        "==========================\n\n"
                        "\nInsira a informação a baixo\n")
                    nome_tipo = input("Novo nome do tipo de projeto: ")
                    projeto.nome_tipo_projeto = nome_tipo
                    tipo_proj = projeto.lista_t_projetos(self.cursor)
                    for tp in tipo_proj:
                        if tp[1].upper() == nome_tipo.upper():
                            projeto.id_t_projeto = tp[0]
                            break
                    time.sleep(1)
                    return projeto
                
                """
==============================================================================================
                Agora, é preciso atualizar as conexões com as outras tabelas
==============================================================================================
                """

                
            case 'd':
                print("==========================\n"
                        "   Deletador de Projetos    \n"
                        "==========================\n\n"
                        "\nLista de projetos disponíveis:\n")
                lista_projetos = projeto.lista_projetos(self.cursor)
                if not lista_projetos:
                    print("Nenhum projeto encontrado.\n")
                    print("Não é possivel deletar um projeto sem antes criá-lo.\n")
                    return None
                else:
                    self.list_projects(projeto)
                    id_projeto = input("\n\nDigite o ID do projeto que deseja deletar: ")
                if not id_projeto.isdigit():
                    print("ID inválido.")
                    return None
                projeto.cod_projeto = int(id_projeto)
                return projeto


    def create_project(self, projeto):
        if isinstance(projeto, Projeto):
            if projeto.nome_tipo_projeto:
                if not projeto.criar_t_projeto(self.cursor):
                    print("\n\nErro ao criar o tipo de projeto.")
                    return
            tipos_projeto = projeto.lista_t_projetos(self.cursor)
            if not tipos_projeto:
                print("\n\nErro ao buscar o tipo de projeto criado.")
                return
            
            for tp in tipos_projeto:
                if tp[1].upper() == projeto.nome_tipo_projeto.upper():
                    projeto.id_t_projeto = tp[0]
                    break

            if projeto.cria_projeto(self.cursor):
                print(f"\n\nProjeto '{projeto.titulo}' criado com sucesso!")
            else:
                print("\n\nErro ao criar o projeto.")
        else:
            print("\n\nDados do projeto inválidos.")

    def list_projects(self, projeto):
        lista_projetos = projeto.lista_projetos(self.cursor)
        if not lista_projetos:
            print("Nenhum projeto encontrado.")
        else:
            for proj in lista_projetos:
                resumo = proj[2] if proj[2] else "N/A"
                print(f"==========================\n")
                print(f"ID:                             {proj[0]}\n"
                        f"Titulo:                         {proj[1]}\n"
                        f"Resumo:                       {resumo}\n"
                        f"Data de Inicio do projeto:    {proj[3]}\n"
                        f"Data de Fim do projeto:       {proj[4]}\n"
                        f"Tipo de projeto:              {proj[5]}")
                print(f"\n==========================\n\n")

    def update_project(self, projeto):
        if isinstance(projeto, Projeto):
            if projeto.atualiza_projeto(self.cursor):
                print(f"\n\nProjeto '{projeto.titulo}' atualizado com sucesso!")
            else:
                print("\n\nErro ao atualizar o projeto.")
        else:
            print("\n\nDados do projeto inválidos.")

    def delete_project(self, projeto):
        if isinstance(projeto, Projeto):
            if projeto.deleta_projeto(self.cursor):
                print(f"\n\nProjeto '{projeto.cod_projeto}' deletado com sucesso!")
            else:
                print("\n\nErro ao deletar o projeto.")
        else:
            print("\n\nDados do projeto inválidos.")
        
    
    def run(self):
        clear()
        print("\n==========================\n"
              " Gerenciador de Projetos  \n"
              "    de Pesquisa da UnB    \n"
              "==========================\n\n")
        print("Selecione uma opção:")
        options = ["Voltar", "Criar projeto", "Listar projetos", "Atualizar projeto", "Deletar projeto"]
        print_menu(options)
        choice = input_choice(len(options))

        if choice == 0:
            return
        elif choice == 1:
            data_project = self.title('c')
            self.create_project(data_project)
        elif choice == 2:
            project = self.title('l')
            self.list_projects(project)
        elif choice == 3:
            project = self.title('u')
            self.update_project(project)
        elif choice == 4:
            project = self.title('d')
            self.delete_project(project)
        else:
            print("\nOpção inválida. Tente novamente.\n")
            time.sleep(2)
            
        voltar = input("\nDeseja voltar ao menu principal?(S/N): ").strip().upper()
        if voltar == 'S' or voltar == 'SIM':
            self.run()
        else:
            print("\nSaindo do gerenciador de projetos...")
            time.sleep(2)
            clear()
            return

        
