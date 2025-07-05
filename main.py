from backend_db import *
from telas_db import *

def main():
    create_database(db_name='db_pesquisas', password=123)
    create_tables_sql_script(db_name='db_pesquisas', password=123, sql_script_path='media/script_db.sql')
    # Conecte ao banco
    conexao = connect_to_database('db_pesquisas', password=123)

    # Teste Instituição
    print("=== Teste Instituição ===")
    inserir_instituicao(conexao, 123456789, "UnB", "UnB", "Pública", "DF", "Brasília", 1000000, "Universidade de Brasília")
    atualizar_instituicao(conexao, 123456789, nome="UnB Atualizada", recursos_investidos=2000000)
    #deletar_instituicao(conexao, 123456789)

    # Teste Membro Externo
    print("=== Teste Membro Externo ===")
    inserir_membro_externo(conexao, 1, "João Externo", "Doutor", "Consultor")
    atualizar_membro(conexao, 1, nome="João Externo Atualizado")
    #deletar_membro(conexao, 1)

    # Teste Estudante
    print("=== Teste Estudante ===")
    inserir_estudante(conexao, 2, "Maria Estudante", "Mestre", "Estudante", 20231234, "Engenharia")
    atualizar_membro(conexao, 2, curso_estudante="Engenharia Civil")
    deletar_membro(conexao, 2)

    # Teste Pesquisador
    print("=== Teste Pesquisador ===")
    inserir_pesquisador(conexao, 3, "Carlos Pesquisador", "Doutor", "Pesquisador", "Departamento de Física")
    atualizar_membro(conexao, 3, departamento="Departamento de Química")
    deletar_membro(conexao, 3)

    # Teste Email
    print("=== Teste Email ===")
    inserir_email(conexao, "joao@email.com", 1)
    atualizar_email(conexao, "joao@email.com", 1, "joao.novo@email.com")
    deletar_email(conexao, "joao.novo@email.com", 1)

    # Teste CNAE
    print("=== Teste CNAE ===")
    inserir_cnae(conexao, 123456789, "85.11-2/00")
    atualizar_cnae(conexao, 123456789, "85.11-2/00", "85.12-1/00")
    #deletar_cnae(conexao, 123456789, "85.12-1/00")

if __name__ == "__main__":
    main()
