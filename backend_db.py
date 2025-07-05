"""
    Esse arquivo contém funções para conectar ao banco de dados PostgreSQL,
    criar um banco de dados e criar tabelas a partir de um script SQL.
"""
import pyodbc

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

if __name__ == "__main__":
    # Exemplo de uso
    password = input("Digite a senha do banco de dados: ")
    create_database(password)
    create_tables_sql_script(password)