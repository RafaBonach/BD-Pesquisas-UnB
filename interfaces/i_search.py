from utils import *
from models_db import *
import time

def i_titulo(tipo_pesquisa):
    match(tipo_pesquisa):
        case "pro":
            clear()
            print("==========================\n"
                "   Pesquisa por Projeto   \n"
                "==========================\n\n"
                "Preencha os dados a seguir para pesquisar um projeto\n"
                "deixe em branco para pesquisar todos os projetos\n")
            nome_projeto = input("Nome do projeto: ").strip() or ""
            time.sleep(2)
            return [nome_projeto]
        
        case "pesq":
            clear()
            print("==========================\n"
                " Pesquisa por Pesquisador  \n"
                "==========================\n\n"
                "Preencha os dados a seguir para pesquisar um pesquisador\n"
                "deixe em branco para pesquisar todos os pesquisadores\n")
            nome_pesquisador = input("Nome do pesquisador: ").strip() or ""
            instituicao = input("Instituição: ").strip() or ""
            time.sleep(2)

            return [nome_pesquisador, instituicao]

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
            time.sleep(2)

            return [nome_instituicao, sigla, cnpj]
        
def i_resultado(tipo_pesquisa, resultado):
    # clear()
    if resultado is not None:
        l_resultados = {}
        match(tipo_pesquisa):
            case "pro":
                print("Projetos encontrados:")
                print("\n==========================\n\n")
                if resultado:
                    for p in resultado:
                        l_resultados[p[0]] = p[1:]
                        print(f"Código do projeto:          {p[0] if p[0] else "N/A"}")
                        print(f"Título:                     {p[1] if p[1] else "N/A"}")
                        print(f"Data de ínicio:             {p[2] if p[2] else "N/A"}")
                        print(f"Prazo de entrega:           {p[3] if p[3] else "N/A"}")
                        print(f"Resumo:                     {p[4] if p[4] else "N/A"}")
                        print(f"Tipo de projeto:            {p[5] if p[5] else "N/A"}")
                        print(f"Pesquisadores:              {p[6] if p[6] else "N/A"}")
                        print(f"Estudantes:                 {p[7] if p[7] else "N/A"}")
                        print(f"Área de atuação:            {p[8] if p[8] else "N/A"}")
                        print(f"Congresso que participou:   {p[9] if p[9] else "N/A"}")
                        print(f"Instituiçao financeira:     {p[10] if p[10] else "N/A"}")
                        print(f"Instituição fomentadora:    {p[11] if p[11] else "N/A"}")
                        print(f"Patrimônio do projeto:      {p[12] if p[12] else "N/A"}")
                        print(f"Localização do projeto:     {p[13] if p[13] else "N/A"}")
                        print(f"Linhas de pesquisa:         {p[14] if p[14] else "N/A"}")
                        print("\n\n==========================\n")
                        time.sleep(1)
                    print("\n\nTotal de projetos encontrados: ", len(resultado[0]))
                else:
                    print("Nenhum projeto encontrado com os critérios informados.")
            
            case "pesq":
                print("\n\nPesquisadores encontrados:")
                print("\n==========================\n\n")
                if resultado:
                    for p in resultado:
                        l_resultados[p[0]] = p[1:]
                        print(f"Id:                     {p[0] if p[0] else "N/A"}")
                        print(f"Nome:                   {p[1] if p[1] else "N/A"}")
                        print(f"Títulação:              {p[2] if p[2] else "N/A"}")
                        print(f"Descrição:              {p[3] if p[3] else "N/A"}")
                        print(f"Departamento:           {p[4] if p[4] else "N/A"}")
                        print(f"Matrícula do estudante: {p[5] if p[5] else "N/A"}")
                        print(f"Curso do Estudante:     {p[6] if p[6] else "N/A"}")
                        print(f"Localização de origem:  {p[7] if p[7] else "N/A"}")
                        print(f"Emails:                 {p[8] if p[8] else "N/A"}")
                        print(f"Área de atuação:        {p[9] if p[9] else "N/A"}")
                        print(f"projetos que pesquisa:  {p[10] if p[10] else "N/A"}")
                        print(f"Projetos que participa: {p[11] if p[11] else "N/A"}")
                        print("\n\n==========================\n")
                    print("\n\nTotal de pesquisadores encontrados: ", len(l_resultados))
                    time.sleep(1)
                else:
                    print("Nenhum membro encontrado com os critérios informados.")

            case "inst":
                print("\n\nInstituições encontradas:")
                print("\n==========================\n\n")
                if resultado:
                    for p in resultado:
                        l_resultados[p[0]] = p[1:]
                        print(f"CNPJ:                   {p[0] if p[0] else "N/A"}")
                        print(f"Nome:                   {p[1] if p[1] else "N/A"}")
                        print(f"Sigla:                  {p[2] if p[2] else "N/A"}")
                        print(f"Natureza juridica:      {p[3] if p[3] else "N/A"}")
                        print(f"UF:                     {p[4] if p[4] else "N/A"}")
                        print(f"Localidade da empresa:  {p[5] if p[5] else "N/A"}")
                        print(f"Descrição da empresa:   {p[7] if p[7] else "N/A"}")
                        print(f"CNAE:                   {p[8] if p[8] else "N/A"}")
                        print(f"Projetos Fomentados:    {p[9] if p[9] else "N/A"}")
                        print(f"Projetos Financiados:   {p[10] if p[10] else "N/A"}")
                        print("\n\n==========================\n")
                    print("\n\nTotal de pesquisadores encontrados: ", len(l_resultados))
                    time.sleep(1)
                else:
                    print("Nenhuma instituição encontrada com os critérios informados.")
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
    def __init__(self, cursor, info=""):
        self.cursor = cursor
        self.info = info

    def search_projects(self):
        projeto = Pesquisa_projeto(
            id=self.info[0],
            projeto=self.info[1],
        )
        print(projeto)
        
        resultado = projeto.resultado_pesquisa(self.cursor)

        return resultado

    def search_pesquisador(self):
        pesquisador = Pesquisa_membros(
            id=self.info[0],
            nome_membro=self.info[1],
        )
        
        resultado = pesquisador.info_pesquisador(self.cursor)
        
        return resultado
    
    def search_instituicao(self):
        print(self.info)
        instituicao = Pesquisa_instituicao(
            nome_instituicao=self.info[0],
            sigla=self.info[1],
            cnpj=self.info[2],
        )

        resultado = instituicao.info_instituicao(self.cursor)
        
        return resultado



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

            if choice == 0:
                return
            
            elif choice == 1:
                info = i_titulo("pro")
                search = ISearch(self.cursor, info)
                resultado = search.search_projects()
                i_resultado("pro", resultado)
                
            
            elif choice == 2:
                info = i_titulo("pesq")
                search = ISearch(self.cursor, info)
                resultado = search.search_pesquisador()
                i_resultado("pesq", resultado)

            elif choice == 3:
                info = i_titulo("inst")
                search = ISearch(self.cursor, info)
                resultado = search.search_instituicao()
                i_resultado("inst", resultado)
            
            else:
                input("Opção inválida.")
                
                
