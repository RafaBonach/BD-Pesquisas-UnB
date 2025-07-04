'''
    Esse será o arquivo principal do projeto.
'''
from backend_db import create_database, create_tables_sql_script, connect_to_database
import pyodbc

from telas_db import inserir_instituicao, inserir_membro_externo, inserir_estudante, inserir_pesquisador

conexao = connect_to_database('db_pesquisas', password='SENHA_DO_BANCO')

inserir_instituicao(conexao, 123, "UnB", "UnB", "Pública", "DF", "Brasília", 100000, "Universidade de Brasília")
inserir_membro_externo(conexao, 1, "João", "Doutor", "Consultor externo")
inserir_estudante(conexao, 2, "Maria", "Mestre", "Estudante", 2023123, "Engenharia")
inserir_pesquisador(conexao, 3, "Carlos", "Doutor", "Pesquisador", "Departamento de Física")

from telas_db import inserir_email, deletar_email, inserir_cnae, deletar_cnae

conexao = connect_to_database('db_pesquisas', password='SENHA')

# Email
inserir_email(conexao, "joao@email.com", 1)
deletar_email(conexao, "joao@email.com", 1)

# CNAE
inserir_cnae(conexao, 123456789, "85.11-2/00")
deletar_cnae(conexao, 123456789, "85.11-2/00")
