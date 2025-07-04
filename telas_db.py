import  pyodbc
from backend_db import connect_to_database # Para usar a função de conexão

### TELA INSTITUIÇÃO ###

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


### TELA MEMBRO
def inserir_membro_externo(conexao, id_membro, nome, titulacao, descricao=None):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO MEMBRO (id_Membro, Nome, Titulação,  Descrição)
            VALUES (?, ?, ?, ?)
        """, (id_membro, nome, titulacao, descricao))
        conexao.commit()
        print("Membro externo inserido com sucesso!")
    except pyodbc.Error as  e:
        print("Erro ao inserir membro externo:", e)

def inserir_estudante(conexao, id_membro, nome, titulacao, descricao, matricula, curso_estudante):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO MEMBRO (Id_Membro, Nome, Titulação, Descrição, Matrícula, Curso_estudante)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_membro, nome, titulacao, descricao, matricula, curso_estudante))
        conexao.commit()
        print("Estudante inserido com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao inserir estudante:", e)

def inserir_pesquisador(conexao, id_membro, nome, titulacao, descricao, departamento):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO MEMBRO (Id_Membro, Nome, Titulação, Descrição, Departamento)
            VALUES (?, ?, ?, ?, ?)
        """, (id_membro, nome, titulacao, descricao, departamento))
        conexao.commit()
        print("Pesquisador inserido com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao inserir pesquisador:", e)

def atualizar_membro(conexao, id_membro, nome=None, titulacao=None, descricao=None, departamento=None, matricula=None, curso_estudante=None):
    try:
        cursor = conexao.cursor()
        campos = []
        valores = []
        if nome: campos.append("Nome = ?"); valores.append(nome)
        if titulacao: campos.append("Titulação = ?"); valores.append(titulacao)
        if descricao: campos.append("Descrição = ?"); valores.append(descricao)
        if departamento: campos.append("Departamento = ?"); valores.append(departamento)
        if matricula: campos.append("Matrícula = ?"); valores.append(matricula)
        if curso_estudante: campos.append("Curso_estudante = ?"); valores.append(curso_estudante)
        if len(campos) == 0:
            print("Nenhuma campo para atualizar.")
            return
        query = f"UPDATE MEMBRO SET {', '.join(campos)} WHERE Id_membro = ?"
        valores.append(id_membro)
        cursor.execute(query, valores)
        conexao.commit()
        print("Membro atualizado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao atualizar membro!", e)

def deletar_membro(conexao, id_membro):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM MEMBRO WHERE Id_Membro = ?", (id_membro,))
        conexao.commit()
        print("Membro deletado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao deletar membro:", e)
        