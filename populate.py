import getpass
from backend_db import *

tables = {
    "area_atuacao" : [
        [],
        [],
        [],
        [],
        []
    ],
    "localidade" : [
        [70910900, "Brasil", "DF", "Brasília"], # UnB - Darcy
        [5508220, "Brasil", "SP", "São Paulo"], # USP
        [],
        [],
        []
    ],
    "projeto" : [
        [1, , , , , ],
        [2, , , , , ],
        [3, , , , , ],
        [4, , , , , ],
        [5, , , , , ]
    ],
    "tipo_projeto" : [
        [1, ],
        [2, ],
        [3, ],
        [4, ],
        [5, ]
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
        ["DEFAULT", "Filosofia da ciência contemporânea", "..."],
        ["DEFAULT", "\"Histórias\" da Filosofia", "..."],
        ["DEFAULT", "O corpo na visão da fenomenologia", "..."],
        ["DEFAULT", "Os sistemas sensoriais de vertebrados", "..."],
        ["DEFAULT", "Direito, Democracia e Mudanças Institucionais" "...",]
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

    for k, v in tables.items():
        values = str(v)[1:-1] # remover [] da string
        conexao.cursor().execute(f"""
                                 INSERT INTO '{k}'
                                 VALUES ({values})
                                 """)
