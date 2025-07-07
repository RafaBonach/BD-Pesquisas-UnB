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
        instituicao = Instituicao()
        patrimonio = Patrimonio()
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
                try:
                    projeto.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date() if data_inicio else None
                    projeto.data_final = datetime.strptime(data_final, '%Y-%m-%d').date() if data_final else None
                except ValueError:
                    print("Data inválida. Formato esperado: AAAA-MM-DD.")
                    return
                projeto.resumo = resumo
                time.sleep(1)

                # Cria Tipo de Projeto
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
                            break
                
                self.create_project(projeto)
                
                
                validador = ''
                validador = input("\n\nDeseja inserir uma localidade no projeto?(S/N): ")
                time.sleep(1)
                if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                    while True:
                        projeto.localidade = None
                        localidade = Localidade()
                        # Cria Localidade do Projeto
                        clear()
                        print("==========================\n"
                            "Localidades disponíveis:\n")
                        l_localidades = self.list_localidades(localidade)
                        cod_postal = input("Digite o código postal da localidade do projeto, N para não inserir localidade no projeto\nou selecione qualquer tecla para criar uma nova localidade: ")
                        if l_localidades != {} and int(cod_postal) in l_localidades:
                            localidade.cod_postal = int(cod_postal)
                        elif cod_postal.strip().upper() == 'N':
                            print("\nLocalidade não inserida no projeto.\n")
                            localidade.cod_postal = None
                        else:
                            clear()
                            print("==========================\n"
                                "Criador de Localidades\n"
                                "==========================\n\n"
                                "\nInsira a informação a baixo\n")
                            localidade.cod_postal = input("Código postal: ")
                            localidade.pais = input("País: ")
                            localidade.uf = input("UF(2 Letras): ")
                            localidade.cidade = input("Cidade: ")

                            if len(localidade.uf) != 2:
                                print("UF inválida. Deve conter exatamente 2 letras.")
                                if input("\n\nDeseja inserir outra localidade no projeto?(S/N): ").strip().upper() != 'S':
                                    break
                                continue
                            
                            if localidade.cod_postal and localidade.pais and localidade.uf and localidade.cidade:
                                self.create_localidade(localidade)
                                projeto.localidade = localidade
                                self.connect_projeto_localidade(projeto)
                            else:
                                print("\n\nDados da localidade inválidos. Localidade não criada.")
                                projeto.localidade = None

                            if input("\n\nDeseja inserir outra localidade no projeto?(S/N): ").strip().upper() != 'S':
                                break
                            
                        
                        
                        
                
                validador = ''
                validador = input("\n\nDeseja inserir uma linha de pesquisa no projeto?(S/N): ")
                time.sleep(1)
                if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                    while True:
                        projeto.linha_pesquisa = None
                        linha_pesquisa = LinhaPesquisa()
                        # Cria Linha de Pesquisa
                        clear()
                        print("==========================\n"
                            "Linhas de pesquisa disponíveis:\n")
                        l_linha_pesquisa = self.list_linhas_pesquisa(linha_pesquisa)
                        id_linha_pesquisa = input("Digite o ID da linha de pesquisa do projeto, N para não inserir linha de pesquisa no projeto\nou selecione qualquer tecla para criar uma nova linha de pesquisa: ")
                        if l_linha_pesquisa != {} and id_linha_pesquisa.isdigit() and int(id_linha_pesquisa) in l_linha_pesquisa:
                            linha_pesquisa.id_linha = int(id_linha_pesquisa)
                            projeto.linha_pesquisa = linha_pesquisa
                        elif id_linha_pesquisa.strip().upper() == 'N':
                            print("\nLinha de pesquisa não inserida no projeto.\n")
                            projeto.linha_pesquisa = None
                        else:
                            clear()
                            print("==========================\n"
                                "Criador de Linhas de Pesquisa\n"
                                "==========================\n\n"
                                "\nInsira a informação a baixo\n")
                            nome_linha = input("Nome da linha de pesquisa: ")
                            desc_linha = input("Descrição da linha de pesquisa: ")
                            linha_pesquisa.nome_linha = nome_linha
                            linha_pesquisa.descricao_linha = desc_linha
                            
                            if linha_pesquisa.nome_linha and linha_pesquisa.descricao_linha:
                                self.create_linha_pesquisa(linha_pesquisa)
                                projeto.linha_pesquisa = linha_pesquisa
                                self.connect_projeto_linha_pesquisa(projeto)
                            else:
                                print("\n\nDados da linha de pesquisa inválidos. Linha de pesquisa não criada.")
                                projeto.linha_pesquisa = None
                        
                        if input("\n\nDeseja inserir outra linha de pesquisa no projeto?(S/N): ").strip().upper() != 'S':
                            break


                    
                validador = ''
                validador = input("\n\nDeseja inserir uma area de atuação do projeto?(S/N): ")
                time.sleep(1)
                if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                    while True:
                        projeto.area_atuacao = None
                        area_atuacao = AreaAtuacao()
                        # Cria Area de Atuação do Projeto
                        clear()
                        print("==========================\n"
                            "Áreas de atuação disponíveis:\n")
                        l_areas_atuacao = self.list_areas_atuacao(area_atuacao)

                        id_area_atuacao = input("Digite o ID da área de atuação do projeto, N para não inserir área de atuação no projeto\nou selecione qualquer tecla para criar uma nova área de atuação: ")

                        if l_areas_atuacao != {} and id_area_atuacao.isdigit() and int(id_area_atuacao) in l_areas_atuacao:
                            area_atuacao.id_area = int(id_area_atuacao)
                            projeto.area_atuacao = area_atuacao
                        elif id_area_atuacao.strip().upper() == 'N':
                            print("\nÁrea de atuação não será inserida no projeto.\n")
                            projeto.area_atuacao = None
                        else:
                            clear()
                            print("==========================\n"
                                "Criador de Áreas de Atuação\n"
                                "==========================\n\n"
                                "\nInsira a informação a baixo\n")
                            nome_area = input("Nome da área de atuação: ")
                            abrangencia = input("Abrangência da área de atuação: ")
                            descricao_area = input("Descrição da área de atuação (opcional): ")
                            area_atuacao.abrangecia = abrangencia
                            area_atuacao.nome_area = nome_area
                            area_atuacao.descricao_area = descricao_area if descricao_area != "" else ""

                            
                            if area_atuacao.abrangecia and area_atuacao.nome_area:
                                self.create_area_atuacao(area_atuacao)
                                projeto.area_atuacao = area_atuacao
                                self.connect_projeto_area_atuacao(projeto)
                            else:
                                print("\n\nDados da área de atuação inválidos. Área de atuação não criada.")
                                projeto.area_atuacao = None

                        if input("\n\nDeseja inserir outra área de atuação no projeto?(S/N): ").strip().upper() != 'S':
                            break

                validador = ''
                validador = input("\n\nDeseja inserir um congresso que o projeto participou?(S/N): ")
                time.sleep(1)
                if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                    while True:
                        projeto.congresso = None
                        congresso = Congresso()
                        # Cria Congresso do Projeto
                        clear()
                        print("==========================\n"
                            "Congressos disponíveis:\n")
                        l_congressos = self.list_congressos(congresso)

                        id_congresso = input("Digite o ID do congresso que o projeto participou, N para não inserir congresso no projeto\nou selecione qualquer tecla para criar um novo congresso: ")
                        if l_congressos != {} and id_congresso.isdigit() and int(id_congresso) in l_congressos:
                            congresso.id_congresso = int(id_congresso)
                            projeto.congresso = congresso
                        elif id_congresso.strip().upper() == 'N':
                            print("\nCongresso não será inserido no projeto.\n")
                            projeto.congresso = None
                        else:
                            clear()
                            print("==========================\n"
                                "Criador de Congressos\n"
                                "==========================\n\n"
                                "\nInsira a informação a baixo\n")
                            nome_congresso = input("Nome do congresso: ")
                            descricao_congresso = input("Descrição do congresso: ")
                            objetivo = input("Objetivo do congresso (opcional): ")
                            congresso.nome_congresso = nome_congresso
                            congresso.desc_congresso = descricao_congresso
                            congresso.objetivo = objetivo
                            
                            if congresso.nome_congresso and congresso.desc_congresso:
                                self.create_congresso(congresso)
                                projeto.congresso = congresso
                                self.connect_projeto_congresso(projeto)
                            else:
                                print("\n\nDados do congresso inválidos. Congresso não criado.")
                                projeto.congresso = None
                        
                        if input("\n\nDeseja inserir outro congresso no projeto?(S/N): ").strip().upper() != 'S':
                            break

                validador = ''
                validador = input("\n\nDeseja inserir um patrimônio do projeto?(S/N): ")
                time.sleep(1)
                if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                    while True:
                        projeto.patrimonio = None
                        patrimonio = Patrimonio()
                        # Cria Patrimônio do Projeto
                        clear()
                        print("==========================\n"
                            "Patrimônios disponíveis:\n")
                        l_patrimonios = self.list_patrimonios(patrimonio)

                        id_patrimonio = input("Digite o ID do patrimônio do projeto, N para não inserir patrimônio no projeto\nou selecione qualquer tecla para criar um novo patrimônio: ")
                        if l_patrimonios != {} and id_patrimonio.isdigit() and int(id_patrimonio) in l_patrimonios:
                            patrimonio.id_patrimonio = int(id_patrimonio)
                            projeto.patrimonio = patrimonio
                        elif id_patrimonio.strip().upper() == 'N':
                            print("\nPatrimônio não será inserido no projeto.\n")
                            projeto.patrimonio = None
                        else:
                            clear()
                            print("==========================\n"
                                "Criador de Patrimônios\n"
                                "==========================\n\n"
                                "\nInsira a informação a baixo\n")
                            nome_patrimonio = input("Nome do patrimônio: ")
                            custo_patrimonio = input("Custo do patrimônio: ")
                            especificacao_patrimonio = input("Especificação do patrimônio (opcional): ")
                            patrimonio.nome_patrimonio = nome_patrimonio
                            patrimonio.custo_patrimonio = custo_patrimonio
                            patrimonio.especificacao_patrimonio = especificacao_patrimonio
                            
                            if patrimonio.nome_patrimonio and patrimonio.custo_patrimonio:
                                projeto.patrimonio = patrimonio
                                self.connect_projeto_patrimonio(projeto)
                            else:
                                print("\n\nDados do patrimônio inválidos. Patrimônio não criado.")
                                projeto.patrimonio = None

                        if input("\n\nDeseja inserir outro patrimônio no projeto?(S/N): ").strip().upper() != 'S':
                            break


                validador = ''
                for i in ['Fomentadora', 'Financiadora']:
                    validador = input(f"\n\nDeseja inserir uma instituição {i} do projeto?(S/N): ")
                    time.sleep(1)
                    if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                        while True:
                            projeto.instituicao = None
                            instituicao = Instituicao()
                            clear()
                            print("==========================\n"
                                "Instituições disponíveis:\n")
                            l_instituicoes = self.list_instituicoes(instituicao)
                            id_instituicao = input(f"Digite o ID da Instituição {i} do projeto ou Precisone qualquer tecla para não inserir instituição: ")
                            if l_instituicoes != {} and id_instituicao.isdigit() and int(id_instituicao) in l_instituicoes:
                                instituicao.cnpj = int(id_instituicao)
                                if i == 'Fomentadora':
                                    instituicao.tipo_fomento = input("Digite o tipo de fomento desta insitituição: ")
                                    if instituicao.tipo_fomento == '':
                                        print("Tipo de fomento não pode ser vazio.")
                                        if input("Deseja inserir outra instituição fomentadora? (S/N): ").strip().upper() != 'S':
                                            time.sleep(1)
                                            break
                                        continue
                                projeto.instituicao = instituicao
                                self.connect_projeto_instituicao(projeto)

                                if input(f"\n\nDeseja inserir outra instituição {i} do projeto?(S/N): ").strip().upper() != 'S':
                                    time.sleep(1)
                                    break
                            else:
                                print(f"\nInstituição {i} não será inserida no projeto.\n")
                                projeto.instituicao = None
                                break

                validador = ''
                for i in ['Pesquisador', 'Estudante', 'Outro Membro']:
                    validador = input(f"\n\nDeseja inserir um {i} no projeto?(S/N): ")
                    time.sleep(1)
                    if validador.strip().upper() == 'S' or validador.strip().upper() == 'SIM':
                        while True:
                            projeto.membro = None
                            membro = Membro()
                            clear()
                            print("==========================\n"
                                "Membros disponíveis:\n")
                            l_membros = self.list_membros(membro, i)
                            id_membro = input(f"Digite o ID do {i} do projeto ou Precisone qualquer tecla para não inserir membro: ")
                            if l_membros != {} and id_membro.isdigit() and int(id_membro) in l_membros:
                                membro.id_membro = int(id_membro)
                                if i != 'Estudante':
                                    membro.funcao = input(f"Digite a função do {i} no projeto: ")
                                    if membro.funcao == '':
                                        print("Função não pode ser vazia.")
                                        if input("Deseja inserir outro membro? (S/N): ").strip().upper() != 'S':
                                            time.sleep(1)
                                            break
                                        continue
                                projeto.membro = membro
                                self.connect_projeto_membro(projeto, i)
                                if input(f"\n\nDeseja inserir outro {i} no projeto?(S/N): ").strip().upper() != 'S':
                                    time.sleep(1)
                                    break
                            else:
                                print(f"\n{i} não será inserido no projeto.\n")
                                projeto.membro = None
                                break

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
            
            case 'i':
                clear()
                print("==================================\n"
                    "  Inserir relatório de projetos    \n"
                        "================================\n\n"
                        "\nLista de projetos disponíveis:\n")
                self.list_projects(projeto)
                id_projeto = input("\n\nDigite o ID do projeto que deseja inserir o relatório: ")
                if not id_projeto.isdigit():
                    print("ID inválido.\n")
                    return None
                projeto.cod_projeto = int(id_projeto)
                caminho_relatorio = input("Caminho do relatório: ")
                if not caminho_relatorio:
                    print("Caminho do relatório não pode ser vazio.\n")
                    return None
                if projeto.insere_relatorio(self.cursor, caminho_relatorio):
                    print(f"\n\nRelatório inserido com sucesso!")
                else:
                    print("\n\nErro ao inserir o relatório.")

            case 'r':
                clear()
                print("======================================\n"
                        "   Retirar relatório de projetos    \n"
                        "====================================\n\n"
                        "\nLista de projetos disponíveis:\n")
                self.list_projects(projeto)
                id_projeto = input("\n\nDigite o ID do projeto que deseja retirar o relatório: ")
                if not id_projeto.isdigit():
                    print("ID inválido.\n")
                    return None
                projeto.cod_projeto = int(id_projeto)
                caminho = input("Digite o caminho onde deseja salvar o relatório: ")
                if caminho:
                    if projeto.retirar_relatorio(self.cursor, caminho):
                        print(f"\n\nRelatório '{projeto.titulo}' foi retirado com sucesso!")
                        print(f"Seu relatório foi salvo em: {caminho}/{projeto.titulo}.pdf")
                    else:
                        print("\n\nErro ao retirar o relatório.")
                else:
                    print("Caminho inválido.")

    
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
                l_projetos = projeto.busca_projeto(self.cursor)
                if not l_projetos:
                    print("\n\nNenhum projeto criado até o momento")
                    return
                projeto.cod_projeto = l_projetos[0][0]  # Pega o ID do projeto criado

                print(f"\n\nProjeto '{projeto.titulo}' criado com sucesso!")
            else:
                print("\n\nErro ao criar o projeto.")
        else:
            print("\n\nDados do projeto inválidos.")

    def list_projects(self, projeto):
        lista_projetos = projeto.lista_projetos(self.cursor)
        l_projetos = {}
        if not lista_projetos:
            print("Nenhum projeto encontrado.")
        else:
            for proj in lista_projetos:
                l_projetos[proj[0]] = (proj[1], proj[2], proj[3], proj[4], proj[5])
                resumo = proj[2] if proj[2] else "N/A"
                print(f"==========================\n")
                print(f"ID:                             {proj[0]}\n"
                        f"Titulo:                         {proj[1]}\n"
                        f"Resumo:                       {resumo}\n"
                        f"Data de Inicio do projeto:    {proj[3]}\n"
                        f"Data de Fim do projeto:       {proj[4]}\n"
                        f"Tipo de projeto:              {proj[5]}")
                print(f"\n==========================\n\n")
        return l_projetos

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
        
    
    def connect_projeto_localidade(self,projeto):
        # Insere a localidade do projeto, se houver
        if projeto.localidade:
            if not projeto.insere_localidade(self.cursor):
                print("\n\nErro ao inserir localidade no projeto.")
                return
            
    def connect_projeto_linha_pesquisa(self, projeto):
        # Insere a linha de pesquisa do projeto, se houver
        if projeto.linha_pesquisa:
            if not projeto.insere_linha_pesquisa(self.cursor):
                print("\n\nErro ao inserir linha de pesquisa no projeto.")
                return
    
    def connect_projeto_area_atuacao(self, projeto):
        # Insere area de atuação do projeto, se houver
        if projeto.area_atuacao:
            if not projeto.insere_area_atuacao(self.cursor):
                print("\n\nErro ao inserir área de atuação no projeto.")
                return
                
    def connect_projeto_congresso(self, projeto):
        # Insere Congresso que o projeto tenha participado, se houver
        if projeto.congresso:
            if not projeto.insere_congresso(self.cursor):
                print("\n\nErro ao inserir congresso no projeto.")
                return
    
    def connect_projeto_instituicao(self, projeto):
        # Insere Instituição fomentadora do projeto, se houver
        if projeto.instituicao:
            if not projeto.insere_instituicao(self.cursor):
                print("\n\nErro ao inserir instituição fomentadora no projeto.")
                return
    
    def connect_projeto_patrimonio(self, projeto):
        # Insere Patrimonio do projeto, se houver
        if projeto.patrimonio:
            if not projeto.insere_patrimonio(self.cursor):
                print("\n\nErro ao inserir patrimônio no projeto.")
                return

    def connect_projeto_membro(self, projeto, tipo_membro=""):
        tipo_membro = tipo_membro.strip().upper()
        # Insere Membro do projeto, se houver
        if projeto.membro:
            if not projeto.insere_membro(self.cursor, tipo_membro):
                print("\n\nErro ao inserir membro no projeto.")
                return

    # LOCALIDADE
    def create_localidade(self, localidade):
        if isinstance(localidade, Localidade):
            if localidade.criar_localidade(self.cursor):
                print(f"\n\nLocalidade '{localidade.cidade}' criada com sucesso!")
            else:
                print("\n\nErro ao criar a localidade.")
        else:
            print("\n\nDados da localidade inválidos.")

    def list_localidades(self, localidade):
        lista_localidades = localidade.lista_localidades(self.cursor)
        if not lista_localidades:
            print("Nenhuma localidade encontrada.")
            return {}
        else:
            l_localidades = {}
            for loc in lista_localidades:
                l_localidades[loc[0]] = (loc[1], loc[2], loc[3])
                print(f"==========================\n")
                print(f"Código Postal: {loc[0]}\n"
                      f"País:          {loc[1]}\n"
                      f"UF:           {loc[2]}\n"
                      f"Cidade:       {loc[3]}")
                print(f"\n==========================\n\n")
            return l_localidades

    # LINHA DE PESQUISA
    def create_linha_pesquisa(self, l_pesquisa):
        if isinstance(l_pesquisa, LinhaPesquisa):
            if l_pesquisa.criar_linha_pesquisa(self.cursor):
                print(f"\n\nLinha de pesquisa '{l_pesquisa.nome_linha}' criada com sucesso!")
            else:
                print("\n\nErro ao criar a linha de pesquisa.")
        else:
            print("\n\nDados da linha de pesquisa inválidos.")

    def list_linhas_pesquisa(self, l_pesquisa):
        lista_linhas_pesquisa = l_pesquisa.lista_linhas_pesquisa(self.cursor)
        if not lista_linhas_pesquisa:
            print("Nenhuma linha de pesquisa encontrada.")
            return {}
        else:
            l_linhas_pesquisa = {}
            for lp in lista_linhas_pesquisa:
                l_linhas_pesquisa[lp[0]] = (lp[1], lp[2])
                print(f"==========================\n")
                print(f"ID: {lp[0]}\n"
                      f"Nome: {lp[1]}\n"
                      f"Descrição: {lp[2]}")
                print(f"\n==========================\n\n")
            return l_linhas_pesquisa

    # AREA DE ATUAÇÃO
    def create_area_atuacao(self, area_atuacao):
        if isinstance(area_atuacao, AreaAtuacao):
            if area_atuacao.criar_area_atuacao(self.cursor):
                print(f"\n\nÁrea de atuação '{area_atuacao.nome_area}' criada com sucesso!")
            else:
                print("\n\nErro ao criar a área de atuação.")
        else:
            print("\n\nDados da área de atuação inválidos.")
    
    def list_areas_atuacao(self, area_atuacao):
        lista_areas_atuacao = area_atuacao.lista_areas_atuacao(self.cursor)
        if not lista_areas_atuacao:
            print("Nenhuma área de atuação encontrada.")
            return {}
        else:
            l_areas_atuacao = {}
            for aa in lista_areas_atuacao:
                l_areas_atuacao[aa[0]] = (aa[1], aa[2])
                print(f"==========================\n")
                print(f"ID: {aa[0]}\n"
                      f"Abrangência: {aa[1]}\n"
                      f"Nome: {aa[2]}")
                print(f"\n==========================\n\n")
        return l_areas_atuacao
    
    # CONGRESSO
    def create_congresso(self, congresso):
        if isinstance(congresso, Congresso):
            if congresso.criar_congresso(self.cursor):
                print(f"\n\nCongresso '{congresso.nome_congresso}' criado com sucesso!")
            else:
                print("\n\nErro ao criar o congresso.")
        else:
            print("\n\nDados do congresso inválidos.")

    def list_congressos(self, congresso):
        lista_congressos = congresso.lista_congressos(self.cursor)
        if not lista_congressos:
            print("Nenhum congresso encontrado.")
            return {}
        else:
            l_congressos = {}
            for c in lista_congressos:
                l_congressos[c[0]] = (c[1], c[2])
                print(f"==========================\n")
                print(f"ID: {c[0]}\n"
                      f"Nome: {c[1]}\n"
                      f"Descrição: {c[2]}")
                print(f"\n==========================\n\n")
        return l_congressos
    
    # PATRIMÔNIO
    def create_patrimonio(self, patrimonio):
        if isinstance(patrimonio, Patrimonio):
            if patrimonio.criar_patrimonio(self.cursor):
                print(f"\n\nPatrimônio '{patrimonio.nome_patrimonio}' criado com sucesso!")
            else:
                print("\n\nErro ao criar o patrimônio.")
        else:
            print("\n\nDados do patrimônio inválidos.")

    def list_patrimonios(self, patrimonio):
        lista_patrimonios = patrimonio.lista_patrimonios(self.cursor)
        if not lista_patrimonios:
            print("Nenhum patrimônio encontrado.")
            return {}
        else:
            l_patrimonios = {}
            for pat in lista_patrimonios:
                l_patrimonios[pat[0]] = (pat[1], pat[2], pat[3], pat[4])
                print(f"==========================\n")
                print(f"ID: {pat[0]}\n"
                      f"Nome: {pat[1]}\n"
                      f"Custo: {pat[2]}\n"
                      f"Especificação: {pat[3]}")
                print(f"\n==========================\n\n")
        return l_patrimonios
    
    # MEMBROS
    def list_membros(self, membro, tipo_membro=""):
        tipo_membro = tipo_membro.strip().upper()
        lista_membros = membro.lista_membros(self.cursor, tipo_membro)
        if not lista_membros:
            print("Nenhum membro encontrado.")
            return {}
        else:
            l_membros = {}
            for m in lista_membros:
                l_membros[m[0]] = (m[1], m[2], m[3])
                print(f"==========================\n")
                print(f"ID: {m[0]}\n"
                      f"Nome: {m[1]}\n"
                      f"Tipo: {m[2]}\n"
                      f"Descricao: {m[3]}\n")
                if tipo_membro == 'PESQUISADOR':
                    print(f"Departamento: {m[4]}")
                    l_membros[m[0]] = (m[1], m[2], m[3], m[4])
                elif tipo_membro == 'ESTUDANTE':
                    print(f"Matricula: {m[4]}\n"
                          f"Curso: {m[5]}")
                    l_membros[m[0]] = (m[1], m[2], m[3], m[4], m[5])
                print(f"\n==========================\n\n")
            return l_membros

    # INSTITUIÇÃO
    def list_instituicoes(self, instituicao):
        lista_instituicoes = instituicao.lista_instituicoes(self.cursor)
        if not lista_instituicoes:
            print("Nenhuma instituição encontrada.")
            return {}
        else:
            l_instituicoes = {}
            for inst in lista_instituicoes:
                l_instituicoes[inst[0]] = (inst[1], inst[2], inst[3])
                print(f"==========================\n")
                print(f"ID: {inst[0]}\n"
                      f"Nome: {inst[1]}\n"
                      f"Sigla: {inst[2]}\n"
                      f"CNPJ: {inst[3]}")
                print(f"\n==========================\n\n")
        return l_instituicoes

    def run(self):
        clear()
        print("\n==========================\n"
              " Gerenciador de Projetos  \n"
              "    de Pesquisa da UnB    \n"
              "==========================\n\n")
        print("Selecione uma opção:")
        options = ["Voltar", "Criar projeto", "Listar projetos", "Atualizar projeto", "Deletar projeto", "Inserir Relatorio", "Coletar Relatório"]
        print_menu(options)
        choice = input_choice(len(options))

        if choice == 0:
            return
        elif choice == 1:
            self.title('c')
        elif choice == 2:
            project = self.title('l')
            self.list_projects(project)
        elif choice == 3:
            project = self.title('u')
            self.update_project(project)
        elif choice == 4:
            project = self.title('d')
            self.delete_project(project)
        elif choice == 5:
            self.title('i')
        elif choice == 6:
            self.title('r')
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

        
