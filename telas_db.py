import  pyodbc
from backend_db import connect_to_database # Para usar a função de conexão

# Tela Instituição
## Inserção ##
def inserir_instituicao(conexao, cnpj, nome, sigla, natureza_jurid, uf, localidade, recursos_investidos, descricao):
    try:
        cursor = conexao.cursor()
        cursor.exwcute("""
            INSERT INTO INSTITUICAO (CNPJ, Nome, Sigla, Natureza_Jurid, UF, Localidade, Recursos_Investidos, Descrição)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (cnpj, nome, sigla, natureza_jurid, uf, localidade, recursos_investidos, descricao))
        conexao.commit()
        print("Instituição inserida com sucesso!")
    except pyodbc.Error as e:
        print("Errp ao inserir instituição:", e)

## Atualização ##    
def atualizar_instituicao(conexao, cnpj, nome=None, sigla=None, natureza_jurid=None, uf=None, localidade=None, recursos_investidos=None, descricao=None):
    try:
        cursor = conexao.cursor()
        campos = []
        valores = []
        if nome: campos.append("Nome = ?"); valores.append(nome)
        if sigla: campos.append("Sigla = ?"); valores.append(sigla)
        if natureza_jurid: campos.append("Natureza_Juríd = ?"); valores.append(natureza_jurid)
        if uf: campos.append("UF = ?"); valores.append(uf)
        if localidade: campos.append("Localidade =   ?"); valores.append(localidade)
        if recursos_investidos is not None: campos.append("Recursos_Investidos = ?"); valores.append(recursos_investidos)
        if descricao: campos.append("Descrição = ?"); valores.append(descricao)
        if not campos:
            print("Nenhum campo para atualizar.")
            return
        query = f"UPDATE INSTITUICAO SET {', '.join(campos)} WHERE CNPJ = ?"
        valores.append(cnpj)
        cursor.execute(query, valores)
        conexao.commit()
        print("Instituição atualizada com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao atualizar instituição:", e)

## Excluir ##
def deletar_instituicao(conexao, cnpj):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM INSTITUICAO WHERE CNPJ = ?", (cnpj,))
        conexao.commit()
        print("Instituição deletada com sucesso!")
    except pyodbc.Error as  e:
        print("Erro ao deletar instituição:", e)
