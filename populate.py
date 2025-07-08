import getpass
from backend_db import *

tables = {
    "area_atuacao" : [
        [1,"Ciências Sociais Aplicadas", "Ciências Humanas"],
        [2,"Diplomacia", "Ciências Sociais Aplicadas"],
        [3,"Decoração", "Linguística, Letras e Artes"],
        [4,"Engenharia de Armamentos", "Engenharias"],
        [5,"Carreira Militar", "Outra"],
        [6,"Secretariado Executivo", "Ciências Sociais Aplicadas"],
        [7,"Engenharia de Agrimensura", "Engenharias"],
        [8,"Segurança Contra Incêndio", "Engenharias"],
        [9,"Relações Públicas", "Ciências Sociais Aplicadas"],
        [10,"Carreira Religiosa", "Ciências Humanas"],
        [11,"Engenharia Cartográfica", "Engenharias"],
        [12,"Engenharia Têxtil", "Engenharias"],
        [13,"História Natural", "Ciências Humanas"],
        [14,"Ciências Atuariais", "Ciências Exatas e da Terra"],
        [15,"Desenho de Moda", "Linguística, Letras e Artes"],
        [16,"Administração Rural", "Ciências Sociais Aplicadas"],
        [17,"Estudos Sociais", "Ciências Humanas"],
        [18,"Tecnologias Naval e Marítima", "Engenharias"],
        [19,"Desenho de Projetos", "Engenharias"],
        [20,"Administração Hospitalar", "Ciências da Saúde"],
        [21,"Bioética", "Ciências da Saúde"],
        [22,"Planejamento Energético", "Engenharias"],
        [23,"Química Industrial", "Ciências Exatas e da Terra"],
        [24,"Tecnologias nas áreas Aeronáuticas", "Engenharias"],
        [25,"Fontes Alternativas de Energia", "Engenharias"],
        [26,"Mudanças Climáticas","Ciências Biológicas"],
        [27,"Relações Internacionais", "Ciências Sociais Aplicadas"],
        [28,"Economia Doméstica", "Ciências Humanas"],
        [29,"Defesa", "Outra"]
    ],
    "localidade" : [
        [70910900, "Brasil", "DF", "Brasília"], # UnB - Darcy
        [5508220, "Brasil", "SP", "São Paulo"], # USP
        [],
        [],
        []
    ],
    "projeto" : [
        [0,3, '"Laboratório de Pesquisa em História e Historiografia do Brasil"', '2021-08-09', '2024-09-08', ],
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
        [13,  3, 'ARCHAI: AS ORIGENS DO PENSAMENTO OCIDENTAL', '2014-11-29', '2023-11-30'],
        [14,  3, 'AVALIAÇÃO DE RISCO DA EXPOSIÇÃO HUMANA A RESIDUOS E CONTAMINANTES', '2011-11-28', '2020-12-13'],
        [15,  7, 'Acesso Livre', '2013-06-30', '2024-10-20'],
        [16,  2, 'Acesso a Medicamentos e Uso Responsável - AMUR', '2024-10-27', '2011-10-19'],
        [17,  6, 'AcquaUnB', '2021-12-25', '2016-11-18'],
        [18, 3, 'Adaptações estruturais e funcionais de plantas em resposta a variações ambientais', '2023-06-24', '2022-01-07'],
        [19, 2, 'Administração Pública Comparada', '2014-05-15', '2014-08-31'],
        [20, 3, 'Administração da Justiça', '2021-04-12', '2011-09-25'],
        [21, 8, 'Alimentação e Microbiota intestinal', '2018-01-06', '2018-04-25'],
        [22, 8, 'Alimentação e qualidade de vida nas restrições alimentares', '2020-06-09', '2018-12-26'],
        [23,7,  'Ambiente 33 - Espacialidades, Comunicação, Estética e Tecnologias', '2011-06-23', '2012-09-08'],
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
        [36,  3, 'Arte, Sociedade e Interpretações do Brasil', '2010-06-11', '2012-10-12'],
        [37,  6, 'As Tecnologias da Informação e Comunicação nos Processos de Formação Musical', '2019-10-08', '2017-09-27'],
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
        [1],
        [2],
        [3],
        [4],
        [5]
    ],
    "possui" : [
        [],
        [],
        [],
        [],
        []
    ],
    "financia" : [
        [],
        [],
        [],
        [],
        []
    ],
    "fomenta" : [
        [],
        [],
        [],
        [],
        []
    ],
    "participa" : [
        [],
        [],
        [],
        [],
        []
    ],
    "vincula" : [
        [],
        [],
        [],
        [],
        []
    ],
    "pesquisa" : [
        [],
        [],
        [],
        [],
        []
    ],
    "realiza" : [
        [],
        [],
        [],
        [],
        []
    ],
    "executa" : [
        [],
        [],
        [],
        [],
        []
    ],
    "congresso" : [
        [1, "'CSBC'", "'...'"],
        [2, "'Congresso Brasileiro de Cardiologia'", "'..'"],
        [3, "'Congresso Brasileiro de Informática na Educaç'", "'...'"],
        [4, "'Simpósio Brasileiro de Banco de Dados'", "'...'"],
        [5, "'Simpósio Brasileiro de Educação em Computação'", "'...'"]
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
        [1],
        [2],
        [3],
        [4],
        [5]
    ],
    "email" : [
        [1, "pudim@gov.br"],
        [2, "magicodeoz@mail.oz"],
        [3, "alice@maravilhas.pais"],
        [3, "kafka@morfose.meta"],
        [5, "joao@joao.joao"]
    ],
    "origem" : [
        [],
        [],
        [],
        [],
        []
    ],
    "atua" : [
        [],
        [],
        [],
        [],
        []
    ],
    "instituicao" : [
        ["00038174000143"], # UnB - Darcy
        ["63025530000104"], # USP
        [],
        [],
        []
    ],
    "cnae" : [
        [85317], # UnB - Darcy
        [85325], # USP
        [],
        [],
        []
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
    for k, v in tables.items():
        values = str(v)[1:-1] # remover [] da string
        conexao.cursor().execute(f"""
                                 INSERT INTO '{k}'
                                 VALUES ({values})
                                 """)
        
    print("Tabelas populadas com sucesso!")
