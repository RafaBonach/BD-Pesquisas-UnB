"""
    Esse arquivo contém funções para conectar ao banco de dados PostgreSQL,
    criar um banco de dados e criar tabelas a partir de um script SQL.
"""
import pyodbc
import psycopg2

def connect_to_database(database_name, password, user_id='postgres'):
    try:
        conexao = pyodbc.connect("Driver={Devart ODBC Driver for PostgreSQL};"
                                f"Database={database_name};"
                                "Server=localhost;"
                                "PORT=5432;"
                                f"User ID={user_id};"
                                f"Password={password};"
                                "String Types=Unicode")
        conexao.autocommit = True
        return conexao
    
    except pyodbc.Error as e:
        return e

def connect_to_database_documments(database_name, password, user_id='postgres'):
    try:
        conexao = psycopg2.connect(database=database_name,
                                   user=user_id,
                                   password=password,
                                   host='localhost',
                                   port='5432')
        conexao.autocommit = True
        return conexao
    except psycopg2.Error as e:
        return e


def create_database(password, database_name='postgres', db_name='db_pesquisas'):
    try:
        conexao = connect_to_database(database_name=database_name, password=password)
        if isinstance(conexao, Exception):
            return None
        
        conexao.autocommit = True

        cursor_admin = conexao.cursor()

        cursor_admin.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        if not cursor_admin.fetchone():
            cursor_admin.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' criada com sucesso!")
        else:
            print(f"Database '{db_name}' já existe.")

        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

def create_tables_sql_script(password ,db_name='db_pesquisas', sql_script_path='media/script_db.sql'):
    try:
        conexao = connect_to_database(db_name, password=password)
        if isinstance(conexao, Exception):
            return None
        
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
        """)

        existing_tables = [row[0].upper() for row in cursor.fetchall()]

        expected_tables = [
            'MEMBRO', 'TIPO_PROJETO', 'PROJETO', 'INSTITUICAO', 'CONGRESSO',
            'LINHA_PESQUISA', 'AREA_ATUACAO', 'LOCALIDADE', 'PATRIMONIO',
            'EMAIL', 'ORIGEM', 'ATUA', 'PESQUISA', 'REALIZA', 'POSSUI',
            'VINCULA', 'EXECUTA', 'PARTICIPA', 'CNAE', 'FINANCIA',
            'FOMENTA', 'EDICAO', 'CONTA'
        ]

        tables_found = [table for table in expected_tables if table in existing_tables]

        if len(tables_found) == len(expected_tables):
            return True
        elif len(tables_found) > 0:
            for table in reversed(expected_tables):  # Remove em ordem reversa devido às FK
                if table in existing_tables:
                    try:
                        cursor.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
                        print(f"   - Tabela {table} removida")
                    except pyodbc.Error as e:
                        print(f"   ⚠️  Erro ao remover {table}: {e}")
            conexao.commit()
            
        with open(sql_script_path, 'r', encoding='utf-8') as file:
            script = file.read()
        
        cursor.execute(script)
        conexao.commit()
        print("Tabelas criadas com sucesso!")
        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao criar tabelas:", e)

def create_procedures_sql_script(password, db_name='db_pesquisas', sql_script_path='media/script_procedure.sql'):
    try:
        conexao = connect_to_database(db_name, password=password)
        if isinstance(conexao, Exception):
            return None
        
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT routine_name
            FROM information_schema.routines 
            WHERE routine_schema = 'public'
            AND routine_type = 'PROCEDURE'
                       """)
        
        existing_procedures = [row[0].lower() for row in cursor.fetchall()]

        expected_procedures = ['inserir_projeto', 'deletar_projeto', 'inserir_tipo_projeto',
                               'deletar_tipo_projeto', 'inserir_localidade', 'vincular_projeto_localidade',
                               'inserir_linha_pesquisa', 'vincular_projeto_linha_pesquisa', 'inserir_area_atuacao',
                               'vincular_projeto_area_atuacao', 'inserir_congresso', 'vincular_projeto_congresso',
                               'instituicao_fomenta_projeto', 'instituicao_financia_projeto', 'inserir_patrimonio',
                               'vincular_pesquisador_projeto', 'vincular_estudante_projeto']
        
        procedures_found = [proc for proc in expected_procedures if proc in existing_procedures]

        if len(procedures_found) == len(expected_procedures):
            return True
        elif len(procedures_found) > 0:
            for proc in reversed(expected_procedures):
                if proc in existing_procedures:
                    try:
                        cursor.execute(f"DROP PROCEDURE IF EXISTS {proc} CASCADE")
                        print(f"   - Procedimento {proc} removido")
                    except pyodbc.Error as e:
                        print(f"   ⚠️  Erro ao remover {proc}: {e}")
            conexao.commit()

        with open(sql_script_path, 'r', encoding='utf-8') as file:
            script = file.read()
        
        cursor.execute(script)
        conexao.commit()
        print("Procedimentos criados com sucesso!")
        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao criar procedimentos:", e)

def create_view_sql_script(password, db_name='db_pesquisas', sql_script_path='media/script_view.sql'):
    try:
        conexao = connect_to_database(db_name, password=password)
        if isinstance(conexao, Exception):
            return None
        
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT table_name 
            FROM information_schema.views 
            WHERE table_schema = 'public'
        """)

        existing_views = [row[0].upper() for row in cursor.fetchall()]

        expected_views = ['VW_DETALHES_PROJETOS_AGRUPADA',
                          'VW_DETALHES_MEMBROS_AGRUPADA',
                          'VW_DETALHES_INSTITUICOES_AGRUPADA']

        views_found = [view for view in expected_views if view in existing_views]

        if len(views_found) == len(expected_views):
            return True
        elif len(views_found) > 0:
            for view in reversed(expected_views):
                if view in existing_views:
                    try:
                        cursor.execute(f"DROP VIEW IF EXISTS {view} CASCADE")
                        print(f"   - View {view} removida")
                    except pyodbc.Error as e:
                        print(f"   ⚠️  Erro ao remover {view}: {e}")
            conexao.commit()

        with open(sql_script_path, 'r', encoding='utf-8') as file:
            script = file.read()
        
        cursor.execute(script)
        conexao.commit()
        print("View criada com sucesso!")
        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao criar view:", e)

if __name__ == "__main__":
    # Exemplo de uso
    password = input("Digite a senha do banco de dados: ")
    create_database(password)
    create_tables_sql_script(password)
    create_procedures_sql_script(password)
    create_view_sql_script(password)