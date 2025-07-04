from utils import *
from models_db import *
import time

class ISearch:
    def __init__(self, cursor, tipo_conta=""):
        self.cursor = cursor
        self.tipo_conta = tipo_conta

    def search_projects(self):
        clear()
        print("==========================\n"
              "   Pesquisa por Projeto   \n"
              "==========================\n\n"
              "Preencha os dados a seguir para pesquisar um projeto\n"
              "deixe em branco para pesquisar todos os projetos\n")
        nome_projeto = input("Nome do projeto: ").strip() or ""
        tipo_projeto = input("Tipo do projeto: ").strip() or ""
        linha_pesquisa = input("Linha de pesquisa: ").strip() or ""
        area_atuação = input("Área de atuação: ").strip() or ""
        nome_membro = input("Nome do membro: ").strip() or ""
        nome_instituicao = input("Nome da instituição fomentadora: ").strip() or ""
        time.sleep(2)

        projeto = Pesquisa_projeto(
            projeto=nome_projeto,
            tipo_projeto=tipo_projeto,
            nome_membro=nome_membro,
            nome_instituicao=nome_instituicao,
            linha_pesquisa = linha_pesquisa,
            area_atuacao = area_atuação
        )
        
        resultado = projeto.resultado_pesquisa(self.cursor)

        clear()
        if resultado != [[]]:
            print("Projetos encontrados:\n")
            print("\n==========================\n\n")
            for p in resultado:
                
                print(
                f"Nome:                         {p[0]}\n"
                f"Resumo:                       {p[1]}\n"
                f"Data de início:               {p[2]}\n"
                f"Data de término:              {p[3]}\n"
                f"Tipo de projeto:              {p[4]}\n"
                f"Membros envolvidos:"
                f"      {p[5]}\n"
                f"Instituição fomentadora:      {p[6]}\n"
                f"Linha de pesquisa:            {p[7]}\n"
                f"Área de atuação:              {p[8]}\n"
                f"Congressos que participou:    {p[9]}\n"
                )
                print("\n\n==========================\n")
                time.sleep(1)

            print("\n\nTotal de projetos encontrados: ", len(resultado))
        else:
            print("==========================\n"
                "Nenhum projeto encontrado com os critérios informados."
                "\n==========================")

        print("\n\nDeseja pesquisar novamente? (S/N)")
        choice = input().strip().upper()
        if choice == 'S':
            self.search_project()
        else:
            return

    def search_pesquisador(self, id=None):
        clear()
        print("==========================\n"
              " Pesquisa por Pesquisador  \n"
              "==========================\n\n"
              "Preencha os dados a seguir para pesquisar um pesquisador\n"
              "deixe em branco para pesquisar todos os pesquisadores\n")
        nome_pesquisador = input("Nome do pesquisador: ").strip() or ""
        instituicao = input("Instituição: ").strip() or ""
        area_atuacao = input("Área de atuação: ").strip() or ""
        time.sleep(2)

        pesquisador = Pesquisa_pesquisador(
            id=id,
            nome_membro=nome_pesquisador,
            nome_instituicao=instituicao,
            area_atuacao=area_atuacao
        )
        
        if self.tipo_conta == "pesquisador" and pesquisador.id is not None:
            resultado = pesquisador.info_pesquisador_detalhado(self.cursor)

            clear()
            if resultado != [[]]:
                print("\n\nPesquisadores encontrados:")
                print("\n==========================\n\n")
                for p in resultado:
                    print(
                        f"ID:                                   {p[0]}\n"
                        f"Nome:                                 {p[1]}\n"
                        f"Titulação:                            {p[2]}\n"
                        f"Departamento:                         {p[3]}\n"
                        f"Descrição:                            {p[4]}\n"
                        f"Área de atuação:                      {p[5]}\n"
                        f"Email:                                {p[6]}\n"
                        f"País:                                 {p[7]}\n"
                        f"UF:                                   {p[8]}\n"
                        f"Cidade:                               {p[9]}\n"
                        f"""Areas de Atuação:
                                {p[10]}\n"""
                        f"""Projetos que participa:
                                {p[11]}\n"""
                        f"Quantidade de congressos que participou: {p[12]}\n"
                        f"""Congressos que participou:
                                {p[13]}\n""")

                    print("\n\n==========================\n")
                    time.sleep(1)
                print("\n\nTotal de pesquisadores encontrados: ", len(resultado))
            else:
                print("==========================\n"
                "Nenhum Pesquisador encontrado com os critérios informados."
                "\n==========================")
        else:
            resultado = pesquisador.info_pesquisador(self.cursor)

            clear()
            if resultado != [[]]:
                print("\n\nPesquisadores encontrados:")
                print("\n==========================\n\n")
                for p in resultado:
                    print(
                        f"Nome:                                 {p[1]}\n"
                        f"Titulação:                            {p[2]}\n"
                        f"Departamento:                         {p[3]}\n"
                        f"Descrição:                            {p[4]}\n"
                        f"Área de atuação:                      {p[5]}\n"
                        f"Email:                                {p[6]}\n"
                        f"Quantidade de projetos que participa: {p[7]}\n")

                    print("\n\n==========================\n")
                    time.sleep(1)
                print("\n\nTotal de pesquisadores encontrados: ", len(resultado))
            else:
                print("==========================\n"
                "Nenhum Pesquisador encontrado com os critérios informados."
                "\n==========================")


        print("\n\nDeseja pesquisar novamente? (S/N)")
        choice = input().strip().upper()
        if choice == 'S':
            self.search_pesquisador()
        else:
            return
    
    def search_instituicao(self):
        clear()
        print("==========================\n"
              " Pesquisa por Instituição  \n"
              "==========================\n\n"
              "Preencha os dados a seguir para pesquisar uma instituição\n"
              "deixe em branco para pesquisar todas as instituições\n")
        nome_instituicao = input("Nome da instituição: ").strip() or ""
        sigla = input("Sigla: ").strip() or ""
        cnpj = input("CNPJ: ").strip() or ""
        time.sleep(2)

        instituicao = Pesquisa_instituicao(
            nome_instituicao=nome_instituicao,
            cnpj=cnpj,
            sigla=sigla
        )
        
        resultado = instituicao.info_instituicao(self.cursor)

        clear()
        if resultado != [[]]:
            print("\n\nInstituições encontradas:")
            print("\n==========================\n\n")
            for i in resultado:
                print(f"""
Nome:       {i[0]}\n
CNPJ:       {i[1]}\n
Sigla:      {i[2]}\n
Descrição:  {i[3]}\n
UF:         {i[4]}\n
Localidade: {i[5]}\n
""")
                print("\n\n==========================\n")
                time.sleep(1)
            print("\n\nTotal de instituições encontradas: ", len(resultado))
        else:
            print("Nenhum projeto encontrado com os critérios informados.")


        print("\n\nDeseja pesquisar novamente? (S/N)")
        choice = input().strip().upper()
        if choice == 'S':
            self.search_instituicao()
        else:
            return

    def menu(self):
        options = ["Voltar", "Pesquisar por Projeto", "Pesquisar por pesquisador", "Pesquisar por instituição"]

        while True:
            clear()
            print("==========================\n"
                  "   Pesquisa de Projetos   \n"
                  "==========================\n\n"
                  "Selecione uma opção:")
            print_menu(options)
            choice = input_choice(len(options))

            if choice == -1:
                input("Opção inválida.")

            if choice == 0:
                return
            
            match(choice):
                case 1:
                    self.search_projects()

                case 2:
                    self.search_pesquisador()

                case 3:
                    self.search_instituicao()
