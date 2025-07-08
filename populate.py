import getpass
from backend_db import *

tables = {
    "area_atuacao" : [
        ["DEFAULT" , "Ciências Humanas", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Diplomacia", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Decoração", "Linguística, Letras e Artes"],
        ["DEFAULT" , "Engenharia de Armamentos", "Engenharias"],
        ["DEFAULT" , "Carreira Militar", "Outra"],
        ["DEFAULT" , "Secretariado Executivo", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Engenharia de Agrimensura", "Engenharias"],
        ["DEFAULT" , "Segurança Contra Incêndio", "Engenharias"],
        ["DEFAULT" , "Relações Públicas", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Carreira Religiosa", "Ciências Humanas"],
        ["DEFAULT" , "Engenharia Cartográfica", "Engenharias"],
        ["DEFAULT" , "Engenharia Têxtil", "Engenharias"],
        ["DEFAULT" , "História Natural", "Ciências Humanas"],
        ["DEFAULT" , "Ciências Atuariais", "Ciências Exatas e da Terra"],
        ["DEFAULT" , "Desenho de Moda", "Linguística, Letras e Artes"],
        ["DEFAULT" , "Administração Rural", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Estudos Sociais", "Ciências Humanas"],
        ["DEFAULT" , "Tecnologias Naval e Marítima", "Engenharias"],
        ["DEFAULT" , "Desenho de Projetos", "Engenharias"],
        ["DEFAULT" , "Administração Hospitalar", "Ciências da Saúde"],
        ["DEFAULT" , "Bioética", "Ciências da Saúde"],
        ["DEFAULT" , "Planejamento Energético", "Engenharias"],
        ["DEFAULT" , "Química Industrial", "Ciências Exatas e da Terra"],
        ["DEFAULT" , "Tecnologias nas áreas Aeronáuticas", "Engenharias"],
        ["DEFAULT" , "Fontes Alternativas de Energia", "Engenharias"],
        ["DEFAULT" , "Mudanças Climáticas","Ciências Biológicas"],
        ["DEFAULT" , "Relações Internacionais", "Ciências Sociais Aplicadas"],
        ["DEFAULT" , "Economia Doméstica", "Ciências Humanas"],
        ["DEFAULT" , "Defesa", "Outra"]
    ],
    "localidade" : [
        [70910900, "Brasil", "DF", "Brasília"], # UnB - Darcy
        [5508220, "Brasil", "SP", "São Paulo"], # USP
        [31270901, "Brasil", "MG", "Belo Horizonte"], # UFMG
        [74690900, "Brasil", "GO", "Goiânia"], # UFG
        [13565905, "Brasil", "SP", "São Carlos"] #UFSCAR
    ],
    "projeto" : [
        [0, 3, '"Laboratório de Pesquisa em História e Historiografia do Brasil"', '2021-08-09', '2024-09-08', ],
        [1, 4, '(Im)polidez em diferentes contextos sócio/interculturais', '2018-11-12', '2022-07-21'],
        [2, 7, 'A1 Rota da Seda na Antigüidade', '2010-12-27', '2020-09-25'],
        [3, 6, 'A Sustentabilidade em Arquitetura e Urbanismo', '2023-10-16', '2010-03-31'],
        [4, 7, 'A formação do professor de língua estrangeira', '2010-05-11', '2012-10-23'],
        [5, 5,'A fraseologia e sua equação nas sub-áreas da Lingüística Aplicada', '2011-06-30', '2019-12-29'],
        [6, 4, 'A tradução como ferramenta de resistência e inclusão', '2014-09-06', '2016-01-07'],
        [7, 6, 'AFETO - Grupo de Pesquisa em Etnocenologia', '2011-05-13', '2021-07-07'],
        [8, 8, 'ALEA- Laboratório de Associação da Linguística, Educação e Antropologia em Estudos do Contato de Línguas, Dialetos e Grupos Sociais na Europa, África e Américas', '2018-04-07', '2011-04-03'],
        [9, 7, 'AMAMENTAÇAO E SAUDE', '2022-02-20', '2012-03-21'],
        [10, 6, 'AQUARELA - Aplicações com Qualidade de Serviços em Redes de Alta Velocidade', '2017-07-25', '2023-03-16'],
        [11, 5, 'AQUARIPARIA', '2015-10-28', '2018-09-03'],
        [12, 2, 'AQUASENSE - Sensoriamento remoto para o monitoramento da qualidade das águas continentais', '2022-03-24', '2011-04-13'],
        [13, 3, 'ARCHAI: AS ORIGENS DO PENSAMENTO OCIDENTAL', '2014-11-29', '2023-11-30'],
        [14, 3, 'AVALIAÇÃO DE RISCO DA EXPOSIÇÃO HUMANA A RESIDUOS E CONTAMINANTES', '2011-11-28', '2020-12-13'],
        [15, 7, 'Acesso Livre', '2013-06-30', '2024-10-20'],
        [16, 2, 'Acesso a Medicamentos e Uso Responsável - AMUR', '2024-10-27', '2011-10-19'],
        [17, 6, 'AcquaUnB', '2021-12-25', '2016-11-18'],
        [18, 3, 'Adaptações estruturais e funcionais de plantas em resposta a variações ambientais', '2023-06-24', '2022-01-07'],
        [19, 2, 'Administração Pública Comparada', '2014-05-15', '2014-08-31'],
        [20, 3, 'Administração da Justiça', '2021-04-12', '2011-09-25'],
        [21, 8, 'Alimentação e Microbiota intestinal', '2018-01-06', '2018-04-25'],
        [22, 8, 'Alimentação e qualidade de vida nas restrições alimentares', '2020-06-09', '2018-12-26'],
        [23, 7,  'Ambiente 33 - Espacialidades, Comunicação, Estética e Tecnologias', '2011-06-23', '2012-09-08'],
        [24, 8,'Anarchai - Metafísica e política contemporâneas', '2015-11-20', '2017-05-27'],
        [25, 6,'Animalia: Grupo de Estudos sobre as Relações entre Humanos e Animais na Antiguidade', '2015-04-19', '2022-02-05'],
        [26, 4, 'Antropologia Política da Saúde', '2021-07-13', '2016-09-25'],
        [27, 7, 'Análise e Produção de Materiais Didáticos Multimodais para o Ensino de Línguas', '2015-05-08', '2015-12-11'],
        [28, 2, 'Análises Laboratoriais Aplicadas', '2024-04-29', '2020-03-29'],
        [29, 6, 'Aprendizagem Colaborativa on-line -GPACO', '2017-11-16', '2013-05-04'],
        [30, 8,'Aprendizagem Lúdica: Pesquisas e Intervenções em Educação e Desporto', '2014-08-10', '2020-02-14'],
        [31, 2,'Aprendizagem, Comportamento e Letramento informacional', '2013-06-18', '2010-07-18'],
        [32, 7,'Aprendizagem, escolarização e desenvolvimento humano', '2010-05-12', '2010-09-16'],
        [33, 6, 'Aprendizagens,Tecnologias e Educação a Distância', '2020-08-20', '2010-01-11'],
        [34, 2, 'Arquitetura e Urbanismo da Região de Brasília', '2014-05-04', '2023-08-13'],
        [35, 8, 'Arte Computacional', '2014-02-07', '2022-01-13'],
        [36, 3, 'Arte, Sociedade e Interpretações do Brasil', '2010-06-11', '2012-10-12'],
        [37, 6, 'As Tecnologias da Informação e Comunicação nos Processos de Formação Musical', '2019-10-08', '2017-09-27'],
        [38, 5, 'Aspectos microbiológicos e imunológicos da interação hospedeiro-fungo', '2021-01-02', '2015-09-20'],
        [39, 5, 'Avaliação computacional de dados, processos e moléculas de interesse na saúde humana', '2020-07-05', '2024-07-28'],
        [40, 8, 'Avaliação de tecnologias em doenças tropicais negligenciadas', '2018-05-10', '2014-10-13'],
        [41, 7,  'Avaliação e Intervenção em Fisioterapia (GPAFi)', '2014-01-21', '2018-03-18'],
        [42, 4, 'Avaliação e organização do trabalho pedagógico', '2025-09-23', '2024-08-12'],
        [43, 1, 'BICAS - Iniciativa BRICS de Estudos sobre Transformações Agrárias', '2020-07-18', '2015-06-28'],
        [44, 5, 'BRANDING: CONSTRUÇÃO, POSICIONAMENTO, IMAGEM E IDENTIDADE DE MARCA', '2015-04-05', '2014-10-01'],
        [45, 6, 'Bactérias aeróbias formadoras de endósporos - Bafes', '2020-09-21', '2015-03-22'],
        [46, 2, 'Bactérias lácticas e Probióticos na Alimentação', '2011-07-31', '2023-08-05'],
        [47, 7, 'Bases moleculares da interação hospedeiro-patógeno (fungos patogênicos: P. brasiliensis, C. albicans e C. neoformans)', '2025-09-20', '2016-01-10'],
        [48, 4, 'BiTGroup - Grupo de Pesquisa em Sistemas Biométricos', '2023-07-31', '2016-10-13'],
        [49, 8, "AQUARIPARIA", "2014-02-20", "2024-01-09"],
    ],
    "tipo_projeto" : [
        [1, "Ciências Sociais Aplicadas"],
        [2, "Linguística, Letras e Artes"],
        [3, "Engenharias"],
        [4, "Outra"],
        [5, "Ciências Humanas"],
        [6, "Ciências Exatas e da Terra"],
        [7, "Ciências da Saúde"],
        [8, "Ciências Biológicas"]
    ],
    "patrimonio" : [
        [1, "DEFAULT", "Estetoscópio", 200, "..."],
        [1, "DEFAULT", "Microscópio Digital", 26000, "..."],
        [3, "DEFAULT", "Martelo", 80, "..."],
        [4, "DEFAULT", "Furadeira BOSCH", 500, "..."],
        [5, "DEFAULT", "Carrinho de mão", 120, "..."]
    ],
    "possui" : [
        [1, 70910900], # Projeto 0 na localidade 70910900 (UnB - Darcy)
        [2, 5508220], # Projeto 1 na localidade 5508220 (USP)
        [3, 31270901], # Projeto 2 na localidade 31270901 (UFMG)
        [4, 74690900], # Projeto 3 na localidade 74690900 (UFGO)
        [5, 13565905] # Projeto 4 na localidade 13565905 (UFSCAR)
    ],
    "financia" : [
        [1, 38174000143], # Projeto 0 da UnB financiado pela instituição 00038174000143
        [2, 63025530000104], # Projeto 1 da USP financiado pela instituição 00038174000143
        [3, 17217985000104], # Projeto 2 da UFMG financiado pela instituição 00038174000143
        [4, 1567601000143], # Projeto 3 da UFG financiado pela instituição 00038174000143
        [5, 66991647000130] # Projeto 4 da UFSCAR financiado pela instituição 00038174000143
    ],
    "fomenta" : [
        [38174000143, 1], # Projeto 0 fomentado pela UnB
        [63025530000104,2], # Projeto 1 fomentado pela USP
        [17217985000104,3], # Projeto 2 fomentado pela UFMG
        [1567601000143,4], # Projeto 3 fomentado pela UFG
        [66991647000130,5] # Projeto 4 fomentado pela UFSCAR 
    ],
    "participa" : [
        [1, 1], # Congresso 1 (CSBC) com Projeto 0
        [2, 2], # Congresso 2 com Projeto 1
        [3, 3], # Congresso 3 com Projeto 2 
        [4, 4], # Congresso 4 com Projeto 3
        [5, 5] # Congresso 5 com Projeto 4
    ],
    "vincula" : [
        [1, 1], # Área 0 (Ciências Humanas) vinculada ao Projeto 0
        [2, 2], # Área 1 (Diplomacia) vinculada ao Projeto 1
        [3, 3], # Área 2 (Decoração) vinculada ao Projeto 2
        [4, 4], # Área 3 (Engenharia de Armamentos) ao Projeto 3
        [5, 5] # Área 4 (Carreira Militar) ao Projeto 4
    ],
    "pesquisa" : [
        [1, 1], # Pesquisador 1 pesquisa Projeto 0
        [1, 2], # Pesquisador 1 pesquisa Projeto 1
        [1, 3], # Pesquisador 1 pesquisa Projeto 2
        [2, 4], # Pesquisador 2 pesquisa Projeto 3
        [2, 5] # Pesquisador 2 pesquisa Projeto 4
    ],
    "realiza" : [
        [3, 1], # Estudante 3 realiza Projeto 0
        [3, 2], # Estudante 3 realiza Projeto 1
        [3, 3], # Estudante 3 realiza Projeto 2
        [4, 4], # Estudante 4 realiza Projeto 3
        [4, 5] # Estudante 4 realiza Projeto 4
    ],
    "executa" : [
        [1, 1], # Linha de Pesquisa 0 executa Projeto 0
        [2, 2], # Linha de Pesquisa 1 executa Projeto 1
        [3, 3], # Linha de Pesquisa 2 executa Projeto 2
        [4, 4], # Linha de Pesquisa 3 executa Projeto 3
        [5, 5] # Linha de Pesquisa 4 executa Projeto 4
    ],
    "congresso" : [
        [1, "CSBC", "..."],
        [2, "Congresso Brasileiro de Cardiologia", ".."],
        [3, "Congresso Brasileiro de Informática na Educaç", "..."],
        [4, "Simpósio Brasileiro de Banco de Dados", "..."],
        [5, "Simpósio Brasileiro de Educação em Computação", "..."]
    ],
    "edicao" : [
        [1, 2025],
        [2, 80],
        [3, 2025],
        [4, 40],
        [5, 2025]
    ],
    "linha_pesquisa" : [
        ["Filosofia da ciência contemporânea", "..."],
        ["\"Histórias\" da Filosofia", "..."],
        ["O corpo na visão da fenomenologia", "..."],
        ["Os sistemas sensoriais de vertebrados", "..."],
        ["Direito, Democracia e Mudanças Institucionais", "..."],
        ["Comunidades Aquáticas"],
        ["Comunidades Terrestres"],
        ["Decomposição de Detritos"],
        ["Dinâmica de Matéria Orgânica"],
        ["Ecologia da Paisagem e Clima"],
        ["Ecologia Isotópica"],
        ["Extensão"],
        ["Funcionamento de Ecossistemas"],
        ["Manejo integrado de bacias hidrográficas"],
        ["Modelagem Ecológica"],
        ["Monitoramento de Sistemas Aquáticos"],
        ["Peixes indicadores de qualidade ambiental"],
        ["Restauração Ecológica"],
        ["Transferência de Tecnologia e Popularização da Ciência"]
    ],
    "membro" : [
        ["DEFAULT", "João da Silva Rocha", "Mestrado", "...", "CIC", "NULL", "NULL"],
        ["DEFAULT", "Cláudia Santoro", "Doutorado", "...", "MAT", "NULL", "NULL"],
        ["DEFAULT", "Cristiano Messi Ronaldinho Jr.", "Graduação", "...", "NULL", 212264423, "EST"],
        ["DEFAULT", "Janaína Arantes", "Graduação", "...", "NULL", 531117756, "CIC"],
        ["DEFAULT", "Amanda", "Graduação", "...", "NULL", "NULL", "NULL"]
    ],
    "email" : [
        [1, "pudim@gov.br"],
        [2, "magicodeoz@mail.oz"],
        [3, "alice@maravilhas.pais"],
        [3, "kafka@morfose.meta"],
        [5, "joao@joao.joao"]
    ],
    "origem" : [
        [70910900, 2],
        [5508220, 1],
        [31270901, 3],
        [74690900, 4],
        [13565905, 5]
    ],
    "atua" : [
        [1],
        [2],
        [3],
        [4],
        [5]
    ],
    "instituicao" : [
        [38174000143, "Universidade de Brasília", "UnB", "Fundação Pública de Direito Público Federal", "DF", "Asa Norte, Campus Darcy Ribeiro", 20000, "Uma Universidade transformadora, com a missão de produzir, integrar e divulgar conhecimento, formando cidadãos comprometidos com a ética, a responsabilidade social e o desenvolvimento sustentável. Essa é a Universidade de Brasília, cuja trajetória se entrelaça com a história da capital do país."], # UnB - Darcy
        [63025530000104, "Universidade de São Paulo", "USP", "Autarquia Estadual ou do Distrito Federal", "SP", "R DA REITORIA", 213233, "USP, as the major institution of higher learning and research in Brazil, is responsible for educating a large part of Brazilian Masters and Ph.D’s. On our site, you can find information about our structure, ways of entrance and services offered to the foreign community."], # USP
        [17217985000104, "Universidade de Minas Gerais", "UFMG", "Fundação Pública de Direito Público Federal", "MG", "...", 153455555, "Localizada na Região Sudeste, a mais industrializada do Brasil, a UFMG, instituição pública de ensino superior gratuito, é a mais antiga universidade do estado de Minas Gerais. Sua fundação ocorreu em 7 de setembro de 1927 com o nome Universidade de Minas Gerais (UMG). Quase um século após, a instituição é liderança regional e nacional em ensino, extensão, cultura, pesquisa científica e geração de patentes, em diversas áreas do conhecimento."], # UFMG
        [1567601000143, "Universidade Federal de Goiás", "UFGO", "Fundação Pública de Direito Público Federal", "GO", "...", 4341239,  "..."], # UFGO
        [66991647000130, "Universidade Federal de São Carlos", "UFSCAR", "Sociedade de Economia Mista", "SP", "RDV WASHINGTON LUIZ", 2222, "..."] # UFSCAR
    ],
    "cnae" : [
        [38174000143, 85317], # UnB - Darcy
        [63025530000104, 85325], # USP
        [17217985000104, 8411600], # UFMG
        [1567601000143, 8531700], # UFG
        [66991647000130, 85503] # UFSCAR
    ],
}

if __name__ == "__main__":
    password = getpass.getpass("Senha: ")

    create_database(password=password, db_name='db_pesquisas')
    create_tables_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_db.sql')
    create_procedures_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_procedure.sql')
    create_view_sql_script(password=password, db_name='db_pesquisas', sql_script_path='media/script_view.sql')
    conexao = connect_to_database(database_name='db_pesquisas', password=password)

    print("===================\n"
          "Populando tabelas:")
    for table in tables.keys():
        print(f" - {table}")
    input("===================\n"
        "\nPressione Enter para continuar...")

    try:
        for k, v in tables.items():
            for linha in v:
                valores = ""
                
                for i in range(len(linha)):
                    if type(linha[i]).__name__ == "str" and linha[i] != "DEFAULT":
                        valores += f"'{linha[i]}'"
                    else:
                        valores += f"{linha[i]}"


                    if i < len(linha) - 1:
                        valores += ", "

                print("insert", k, " -> ", valores)

                conexao.cursor().execute(f"""
                                        INSERT INTO {k}
                                        VALUES ({valores})
                                        """)
            
        print("Tabelas populadas com sucesso!")

    except pyodbc.Error as e:
        print(f"Erro ao popular tabelas!!\n{e}")
    except Exception as exc:
        print(f"Erro ao popular tabelas!!\n{exc}")
