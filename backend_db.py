"""
    Esse arquivo conecta ao banco de dados e executa o arquivo SQL para criar as tabelas.
    Ele utiliza SQLAlchemy para gerenciar a conexão e as transações com o banco de dados
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Defina a URL postgresql com o seguinte padrão:
# postgresql://<username>:<password>@<host>:<port>/<database>
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/pesquisas_unb"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def execute_sql_file():
    sql_file_path = os.path.join(os.path.dirname(__file__), 'media', 'script_db.sql')

    try:
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        
        sql_commands = [cmd.strip() for cmd in sql_script.split(';') if cmd.strip()]

        with engine.connect() as connection:
            for command in sql_commands:
                if command and not command.startswith('--'):
                    try:
                        connection.execute(text(command))
                        connection.commit()
                    except Exception as e:
                        print(f"Error executing command: {command}\n{e}")

    except FileNotFoundError:
        print(f"SQL file not found: {sql_file_path}")
    except Exception as e:
        print(f"An error occurred while executing the SQL file: {e}")
    
def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
