'''
    Esse será o arquivo principal do projeto.
'''
from backend_db import get_bd, execute_sql_file

# Executa o arquivo SQL para criar as tabelas no banco de dados
if __name__ == "__main__": # Se o arquivo for executado diretamente, executa o código abaixo
    print("Executando arquivo SQL para criar tabelas...")
    execute_sql_file()
    print("Tabelas criadas com sucesso!")
