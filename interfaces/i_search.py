from utils import *
from models_db import *
import time

def i_titulo(tipo_pesquisa, id=""):
    match(tipo_pesquisa):
        case "pro":
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
            return [id, nome_projeto, tipo_projeto, linha_pesquisa, area_atuação, nome_membro, nome_instituicao]
        
        case "pesq":
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

            return [id, nome_pesquisador, instituicao, area_atuacao]

        case "inst":
            clear()
            print("==========================\n"
                " Pesquisa por Instituição  \n"
                "==========================\n\n"
                "Preencha os dados a seguir para pesquisar uma instituição\n"
                "deixe em branco para pesquisar todas as instituições\n")
            nome_instituicao = input("Nome da instituição: ").strip() or ""
            sigla = input("Sigla: ").strip() or ""
            cnpj = input("CNPJ: ").strip() or ""
            natureza_juridica = input("Natureza jurídica: ").strip() or ""
            uf = input("UF: ").strip() or ""
            localidade = input("Localidade: ").strip() or ""
            time.sleep(2)

            return [id, nome_instituicao, sigla, cnpj, natureza_juridica, uf, localidade]
        
        case "est":
            clear()
            print("==========================\n"
                " Pesquisa por Estudante  \n"
                "==========================\n\n"
                "Preencha os dados a seguir para pesquisar um estudante\n"
                "deixe em branco para pesquisar todas os estudantes\n")
            nome_estudante = input("Nome do estudante: ").strip() or ""
            titulacao = input("Titulação: ").strip() or ""
            descricao = input("Descrição: ").strip() or ""
            matricula = input("Matrícula: ").strip() or ""
            curso_estudante = input("Curso: ").strip() or ""
            time.sleep(2)

            return [id, nome_estudante, titulacao, descricao, matricula, curso_estudante]

def i_resultado(tipo_pesquisa, resultado):
    # clear()
    if resultado is not None:
        if tipo_pesquisa[-1] == 'd':
            match(tipo_pesquisa):
                case "pesq_id":
                    print(f"Informações do pesquisador {resultado[0][1]}:\n\n")
                    for p in resultado:
                        print(
                            f"ID:                                   {p[0]}\n"
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
                
                case "est_id":
                    print(f"Informações do estudante {resultado[0][1]}:\n\n")
                    for e in resultado:
                        print(
                            f"ID:                                   {e[0]}\n"
                            f"Titulação:                            {e[2]}\n"
                            f"Descrição:                            {e[3]}\n"
                            f"Matrícula:                            {e[4]}\n"
                            f"Curso:                                {e[5]}\n"
                            f"Email:                                {e[6]}\n"
                            f"Nacionalidade:                        {e[7]}\n"
                            f"UF:                                   {e[8]}\n"
                            f"Cidade:                               {e[9]}\n"
                            f"Projetos que participa ({e[11]}):\n"
                            f"{e[10]}\n"
                            )
        else:
            match(tipo_pesquisa):
                case "pro":
                    print("Projetos encontrados:\n")
                    print("\n==========================\n\n")
                    if not resultado:
                        for p in resultado:
                            if p[0] is not None:
                                print(f"Nome:                         {p[0]}\n")
                            if p[1] is not None:
                                print(f"Resumo:                       {p[1]}\n")
                            if p[2] is not None:
                                print(f"Data de início:               {p[2]}\n")
                            if p[3] is not None:
                                print(f"Data de término:              {p[3]}\n")
                            if p[4] is not None:
                                print(f"Tipo de projeto:              {p[4]}\n")
                            if p[5] is not None:
                                print("Membros envolvidos:"
                                    f"{p[5]}\n\n")
                            if p[6] is not None:
                                print(f"Instituição fomentadora:      {p[6]}\n")
                            if p[7] is not None:
                                print(f"Linha de pesquisa:            {p[7]}\n")
                            if p[8] is not None:
                                print(f"Área de atuação:              {p[8]}\n")
                            if p[9] is not None:
                                print(f"Congressos que participou:    {p[9]}\n")
                            print("\n\n==========================\n")
                            time.sleep(1)
                        print("\n\nTotal de projetos encontrados: ", len(resultado[0]))
                    else:
                        print("Nenhum projeto encontrado com os critérios informados.")
                
                case "pesq":
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
                    print("\n\nTotal de pesquisadores encontrados: ", len(resultado[0]))

                case "inst":
                    print("\n\nInstituições encontradas:")
                    print("\n==========================\n\n")
                    for i in resultado:
                        print(
                            f"CNPJ:                 {i[0]}\n"
                            f"Nome:                 {i[1]}\n"
                            f"Sigla:                {i[2]}\n"
                            f"Natureza Jurídica:    {i[3]}\n"
                            f"Descrição:            {i[3]}\n"
                            f"UF:                   {i[4]}\n"
                            f"Localidade:           {i[5]}\n"
                            f"Recursos Investidos:  {i[6]}\n"
                            f"Projetos financiados:"
                            f"{i[7]}\n"
                            f"Projetos fomentados:"
                            f"{i[8]}\n")
                        print("\n\n==========================\n")
                        time.sleep(1)
                    print("\n\nTotal de instituições encontradas: ", len(resultado[0]))

                case "est":
                    print("\n\nEstudantes encontrados:")
                    print("\n==========================\n\n")
                    for e in resultado:
                        print(
                            f"ID:                                   {e[0]}\n"
                            f"Nome:                                 {e[1]}\n"
                            f"Titulação:                            {e[2]}\n"
                            f"Descrição:                            {e[3]}\n"
                            f"Matrícula:                            {e[4]}\n"
                            f"Curso:                                {e[5]}\n"
                            f"Email:                                {e[6]}\n"
                            f"Projetos que participa ({e[11]}):\n"
                            f"{e[10]}\n"
                            )
                        print("\n\n==========================\n")
                        time.sleep(1)
                    print("\n\nTotal de estudantes encontradas: ", len(resultado[0]))

    else:
        print("==============================\n"
              "Nenhuma informação encontrado."
              "\n============================")
        
    choice = input("\n\nDeseja voltar (S ou Y = sim): ").strip().upper()
    if choice == 'S' or choice == 'SIM' or choice == 'Y' or choice == 'YES':
        return
    else:
        exit()

class ISearch:
    def __init__(self, cursor, info, tipo_conta=""):
        self.cursor = cursor
        self.info = info
        self.tipo_conta = tipo_conta

    def search_projects(self):
        projeto = Pesquisa_projeto(
            id=self.info[0],
            projeto=self.info[1],
            tipo_projeto=self.info[2],
            nome_membro=self.info[3],
            nome_instituicao=self.info[4],
            linha_pesquisa = self.info[5],
            area_atuacao =  self.info[6],
        )
        
        resultado = projeto.resultado_pesquisa(self.cursor)

        return resultado

    def search_pesquisador(self):
        pesquisador = Pesquisa_pesquisador(
            id=self.info[0],
            nome_membro=self.info[1],
            nome_instituicao=self.info[2],
            area_atuacao=self.info[3]
        )
        
        if self.tipo_conta == "pesquisador" and pesquisador.id is not None:
            resultado = pesquisador.info_pesquisador_detalhado(self.cursor)
        else:
            resultado = pesquisador.info_pesquisador(self.cursor)
        
        return resultado
    
    def search_estudante(self):
        estudante = Pesquisa_estudante(
            id=self.info[0],
            nome_estudante=self.info[1],
            titulacao=self.info[2],
            descricao=self.info[3],
            matricula=self.info[4],
            curso_estudante=self.info[5]
        )
        
        resultado = estudante.info_estudante(self.cursor)

        return resultado

    def search_instituicao(self):
        instituicao = Pesquisa_instituicao(
            id=self.info[0],
            nome_instituicao=self.info[1],
            cnpj=self.info[2],
            sigla=self.info[3],
            natureza_juridica=self.info[4],
            uf=self.info[5],
            localidade=self.info[6],
        )
        
        resultado = instituicao.info_instituicao(self.cursor)

        return resultado



def menu(cursor):
    options = ["Voltar", "Pesquisar por Projeto", "Pesquisar por pesquisador", "Pesquisar por instituição"]

    while True:
        clear()
        print("==========================\n"
                "   Pesquisa de Projetos   \n"
                "==========================\n\n"
                "Selecione uma opção:")
        print_menu(options)
        choice = input_choice(len(options))

        if choice == 0:
            return
        
        elif choice == 1:
            info = i_titulo("pro")
            search = ISearch(cursor, info)
            resultado = search.search_projects()
            i_resultado("pro", resultado)
            
        
        elif choice == 2:
            info = i_titulo("pesq")
            search = ISearch(cursor, info, self.tipo_conta)
            resultado = search.search_pesquisador()
            i_resultado("pesq", resultado)

        elif choice == 3:
            info = i_titulo("inst")
            search = ISearch(cursor, info)
            resultado = search.search_instituicao()
            i_resultado("inst", resultado)
        
        else:
            input("Opção inválida.")
                
                
