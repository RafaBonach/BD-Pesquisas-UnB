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
        print(f"Conexão bem-sucedida com o banco de dados '{database_name}'!")
        return conexao
    except pyodbc.Error as e:
        print(f"Erro ao conectar ao banco de dados '{database_name}':", e)
        return None


def create_database(password, db_name='db_pesquisas'):
    try:
        conexao = connect_to_database('postgres', password=password)
        if not conexao:
            return None
        
        conexao.autocommit = True
        print("Conexão com o banco de dados 'postgres' bem-sucedida!")

        cursor_admin = conexao.cursor()

        cursor_admin.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        if not cursor_admin.fetchone():
            cursor_admin.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' criada com sucesso!")
        else:
            print(f"Database '{db_name}' já existe.")

        cursor_admin.close()
        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

def create_tables_sql_script(password ,db_name='db_pesquisas', sql_script_path='media/script_db.sql'):
    try:
        conexao = connect_to_database(db_name, password=password)
        if not conexao:
            return None
        
        cursor = conexao.cursor()

        with open(sql_script_path, 'r', encoding='utf-8') as file:
            script = file.read()
        
        cursor.execute(script)
        conexao.commit()
        print("Tabelas criadas com sucesso!")

        cursor.close()
        conexao.close()
    except pyodbc.Error as e:
        print("Erro ao criar tabelas:", e)