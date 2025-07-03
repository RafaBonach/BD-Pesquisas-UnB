from utils import *
from models_db import *
import time

class ISearch:
    def __init__(self, cursor, conta=""):
        self.cursor = cursor
        self.conta = conta

    def search_project(self):
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
        nome_instituicao = input("Nome da instituição: ").strip() or ""
        time.sleep(2)

        projeto = Pesquisa_projeto(
            projeto=nome_projeto,
            tipo_projeto=tipo_projeto,
            linha_pesquisa=linha_pesquisa,
            area_atuacao=area_atuação,
            nome_membro=nome_membro,
            nome_instituicao=nome_instituicao
        )
        
        resultado = projeto.resultado_pesquisa(self.cursor)

        clear()
        if resultado != None:
            print("\n\nProjetos encontrados:")
            print("\n==========================\n\n")
            for titulo, nome_tipo, resumo, l_pesquisa, escricao_linha_pesquisa, nome_area_atuacao, data_inicio, data_final, nome_congresso, funcao_membro, n_instituicao, tipo_fomento in resultado:
                
                print(f"""
Nome:                           {titulo}\n
Tipo de projeto:                {nome_tipo}\n
Resumo:                         {resumo}\n
Linha de pesquisa:              {l_pesquisa}\n
Descrição da linha de pesquisa: {escricao_linha_pesquisa}\n
Área de atuação:                {nome_area_atuacao}\n
Data de início:                 {data_inicio}\n
Data de término:                {data_final}\n
Congresso participado:          {nome_congresso}\n
Membro envolvido:               {nome_membro}\n
Funcao do membro:               {funcao_membro}\n
Nome da instituição fomentadora:{n_instituicao}\n
Tipo de fomento:                {tipo_fomento}\n
""")
                print("\n\n==========================\n")
                time.sleep(1)
            print("\n\nTotal de projetos encontrados: ", len(resultado))
        
        else:
            input("Erro no acesso ao banco de dados.")

        print("\n\nDeseja pesquisar novamente? (S/N)")
        choice = input().strip().upper()
        if choice == 'S':
            self.search_project()
        else:
            return
        
    def search_pesquisador(self):
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
            nome_membro=nome_pesquisador,
            nome_instituicao=instituicao,
            area_atuacao=area_atuacao
        )
        
        if self.conta == "Instituição":
            resultado = pesquisador.info_pesquisador_detalhado(self.cursor)

            clear()
            if resultado != None:
                print("\n\nPesquisadores encontrados:")
                print("\n==========================\n\n")
                for p in resultado:
                    print(f"""
Nome:               {p.Nome_membro}\n
Titulação:          {p.titulacao}\n
Descrição:          {p.descricao_membro}\n
Departamento:       {p.Departamento}\n
Área de atuação:    {p.Nome_area_atuacao}\n
Email:              {p.Email}\n
País:               {p.pais}\n
UF:                 {p.UF}\n
Projeto:            {p.titulo_projeto}\n
Resumo do projeto:  {p.resumo_projeto}\n
""")

                    print("\n\n==========================\n")
                    time.sleep(1)
                print("\n\nTotal de pesquisadores encontrados: ", len(resultado))
            else:
                input("Erro no acesso ao banco de dados.")
        else:
            resultado = pesquisador.info_pesquisador(self.cursor)

            clear()
            if resultado != None:
                print("\n\nPesquisadores encontrados:")
                print("\n==========================\n\n")
                for p in resultado:
                    print(f"""
Nome:               {p.Nome_membro}\n
Titulação:          {p.titulacao}\n
Descrição:          {p.descricao_membro}\n
Departamento:       {p.Departamento}\n
Área de atuação:    {p.Nome_area_atuacao}\n
Email:              {p.Email}\n
País:               {p.pais}\n
UF:                 {p.UF}\n
""")

                    print("\n\n==========================\n")
                    time.sleep(1)
                print("\n\nTotal de pesquisadores encontrados: ", len(resultado))
            else:
                input("Erro no acesso ao banco de dados.")

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
        if resultado != None:
            print("\n\nInstituições encontradas:")
            print("\n==========================\n\n")
            for i in resultado:
                print(f"""
Nome:       {i.Nome}\n
CNPJ:       {i.CNPJ}\n
Sigla:      {i.Sigla}\n
Descrição:  {i.Descricao}\n
UF:         {i.UF}\n
Localidade: {i.Localidade}\n
""")
                print("\n\n==========================\n")
                time.sleep(1)
            print("\n\nTotal de instituições encontradas: ", len(resultado))
        else:
            input("Erro no acesso ao banco de dados.")

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
                    self.search_project()

                case 2:
                    self.search_pesquisador()

                case 3:
                    self.search_instituicao()