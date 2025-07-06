import pyodbc
from backend_db import connect_to_database # Para usar a função de conexão

### TELA INSTITUIÇÃO ###
## VERIFICAÇÕES 
def instituicao_existe(cursor, cnpj):
    """Verifica se uma instituição já existe pelo CNPJ."""
    try:
        cursor.execute("SELECT 1 FROM INSTITUICAO WHERE CNPJ = ?", (cnpj,))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao verificar instituição:", e)
        return False

def membro_existe(cursor, nome):
    """Verifica se um membro já existe pelo Id_Membro."""
    try:
        cursor.execute("SELECT 1 FROM MEMBRO WHERE Nome = ?", (nome))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao verificar membro:", e)
        return False

def email_existe(cursor, email, nome):
    """Verifica se um e-mail já está cadastrado para o membro."""
    try:
        cursor.execute("SELECT 1 FROM Email WHERE Email = '?' AND Nome = '?'", (email, nome))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao verificar e-mail:", e)
        return False

def cnae_existe(cursor, cnpj_instituicao, cnae):
    """Verifica se um CNAE já está cadastrado para a instituição."""
    try:
        cursor.execute("SELECT 1 FROM CNAE WHERE CNPJ_Instituicao = ? AND CNAE = ?", (cnpj_instituicao, cnae))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao verificar CNAE:", e)
        return False





################################
## Inserção ##
def inserir_instituicao(cursor, cnpj, nome, sigla, natureza_jurid, uf, localidade, recursos_investidos, descricao):
    if instituicao_existe(cursor, cnpj):
        print(f"Instituição com CNPJ {cnpj} já existe. Não é possível inserir duplicado.")
        return False
    try:
        cursor.execute(f"""
            INSERT INTO INSTITUICAO (CNPJ, Nome, Sigla, Natureza_Juríd, UF, Localidade, Recursos_Investidos, Descrição)
            VALUES ({cnpj}, '{nome}', '{sigla}', '{natureza_jurid}', '{uf}', '{localidade}', {recursos_investidos}, '{descricao}')
        """)
        print("Instituição inserida com sucesso!")
        return True
    except pyodbc.Error as e:
        print("Erro ao inserir instituição:", e)
        return -1

## Atualização ##    
def atualizar_instituicao(cursor, cnpj, nome=None, sigla=None, natureza_jurid=None, uf=None, localidade=None, recursos_investidos=None, descricao=None):
    try:
        campos = []
        valores = []
        if nome != "": campos.append("Nome = ?"); valores.append(nome)
        if sigla != "": campos.append("Sigla = ?"); valores.append(sigla)
        if natureza_jurid != "": campos.append("Natureza_Juríd = ?"); valores.append(natureza_jurid)
        if uf != "": campos.append("UF = ?"); valores.append(uf)
        if localidade != "": campos.append("Localidade =   ?"); valores.append(localidade)
        if recursos_investidos != "": campos.append("Recursos_Investidos = ?"); valores.append(recursos_investidos)
        if descricao != "": campos.append("Descrição = ?"); valores.append(descricao)
        if not campos:
            print("Nenhum campo para atualizar.")
            return False
        query = f"UPDATE INSTITUICAO SET {', '.join(campos)} WHERE CNPJ = ?"
        valores.append(cnpj)
        print("query", query, valores)
        cursor.execute(query, valores)

        print("Instituição atualizada com sucesso!")
        return True
    except pyodbc.Error as e:
        print("Erro ao atualizar instituição:", e)
        return False

## Excluir ##
def deletar_instituicao(cursor, cnpj):
    try:
        cursor.execute("DELETE FROM INSTITUICAO WHERE CNPJ = ?", (cnpj,))

        print("Instituição deletada com sucesso!")
    except pyodbc.Error as  e:
        print("Erro ao deletar instituição:", e)


### TELA MEMBRO
# Inserção do membro externo
def inserir_membro_externo(cursor, nome, titulacao, descricao=None):
    if membro_existe(cursor, nome):
        print(f"Membro com Nome {nome} já existe. Não é possível inserir duplicado.")
        return False
    try:
        cursor.execute(f"""
            INSERT INTO MEMBRO (id_Membro, Nome, Titulação,  Descrição)
            VALUES (DEFAULT, '{nome}', '{titulacao}', '{descricao}')
        """)

        print("Membro externo inserido com sucesso!")
        return True

    except pyodbc.Error as  e:
        print("Erro ao inserir membro externo:", e)
        return -1

# Inserção do estudante
def inserir_estudante(cursor, nome, titulacao, descricao, matricula, curso_estudante):
    if membro_existe(cursor, nome):
        print(f"Membro com Nome {nome} já existe. Não é possível inserir duplicado.")
        return False
    try:
        cursor.execute(f"""
            INSERT INTO MEMBRO (Id_Membro, Nome, Titulação, Descrição, Matrícula, Curso_estudante)
            VALUES (DEFAULT, '{nome}', '{titulacao}', '{descricao}', {matricula}, '{curso_estudante}')
        """)

        print("Estudante inserido com sucesso!")
        return True
    except pyodbc.Error as e:
        print("Erro ao inserir estudante:", e)
        return -1

def inserir_pesquisador(cursor, nome, titulacao, descricao, departamento):
    if membro_existe(cursor, nome):
        print(f"Membro com Nome {nome} já existe. Não é possível inserir duplicado.")
        return False
    try:
        cursor.execute(f"""
            INSERT INTO MEMBRO (Id_Membro, Nome, Titulação, Descrição, Departamento)
            VALUES (DEFAULT, '{nome}', '{titulacao}', '{descricao}', '{departamento}')
        """)

        print("Pesquisador inserido com sucesso!")
        return True
    except pyodbc.Error as e:
        print("Erro ao inserir pesquisador:", e)
        return -1

def atualizar_membro(cursor, id_membro, nome=None, titulacao=None, descricao=None, departamento=None, matricula=None, curso_estudante=None):
    try:
        campos = []
        valores = []
        if nome != "": campos.append("Nome = ?"); valores.append(nome)
        if titulacao != "": campos.append("Titulação = ?"); valores.append(titulacao)
        if descricao != "": campos.append("Descrição = ?"); valores.append(descricao)
        if departamento != "": campos.append("Departamento = ?"); valores.append(departamento)
        if matricula != "": campos.append("Matrícula = ?"); valores.append(matricula)
        if curso_estudante != "": campos.append("Curso_estudante = ?"); valores.append(curso_estudante)
        if len(campos) == 0:
            print("Nenhuma campo para atualizar.")
            return False
        query = f"UPDATE MEMBRO SET {', '.join(campos)} WHERE Id_membro = ?"
        valores.append(id_membro)
        cursor.execute(query, valores)

        print("Membro atualizado com sucesso!")
        return True
    except pyodbc.Error as e:
        print("Erro ao atualizar membro!", e)
        return -1

def deletar_membro(cursor, id_membro):
    try:
        cursor.execute("DELETE FROM MEMBRO WHERE Id_Membro = ?", (id_membro))

        print("Membro deletado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao deletar membro:", e)

### PARA ATRIBUTOS MULTIVALORADOS
## CRUD PARA EMAIL(MEMBRO)
def inserir_email(cursor, email, id_membro):
    if email_existe(cursor, email, id_membro):
        print(f"E-mail '{email}' já está cadastrado para o membro {id_membro}. Não é possível inserir duplicado.")
        return
    try:
        cursor.execute(f"""
            INSERT INTO Email (id_membro, Email)
            VALUES ({id_membro}, '{email}')
        """)

        print("Email inserido com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao inserir email:", e)

def atualizar_email(cursor, email_antigo, id_membro, email_novo):
    if email_existe(cursor, email_novo, id_membro):
        print(f"E-mail '{email_novo}' já está cadastrado para o membro {id_membro}. Não é possível atualizar para duplicado.")
        return
    try:
        cursor.execute("""
            UPDATE Email
            SET Email = ?
            WHERE Email = ? AND id_membro = ?
        """, (email_novo, email_antigo, id_membro))

        print("Email atualizado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao atualizar email:", e)

def deletar_email(cursor, email, id_membro):
    try:
        cursor.execute("""
            DELETE FROM Email
            WHERE Email = ? AND id_membro = ?
        """, (email, id_membro))

        print("Email deletado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao deletar email:", e)

## CRUD PARA CNAE(INSTITUIÇÃO)

def inserir_cnae(cursor, cnpj_instituicao, cnae):
    if cnae_existe(cursor, cnpj_instituicao, cnae):
        print(f"CNAE '{cnae}' já está cadastrado para a instituição {cnpj_instituicao}. Não é possível inserir duplicado.")
        return
    try:
        cursor.execute(f"""
            INSERT INTO CNAE (CNPJ_Instituicao, CNAE)
            VALUES ({cnpj_instituicao}, '{cnae}')
        """)

        print("CNAE inserido com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao inserir CNAE:", e)

def atualizar_cnae(cursor, cnpj_instituicao, cnae_antigo, cnae_novo):
    if cnae_existe(cursor, cnpj_instituicao, cnae_novo):
        print(f"CNAE '{cnae_novo}' já está cadastrado para a instituição {cnpj_instituicao}. Não é possível atualizar para duplicado.")
        return
    try:
        cursor.execute("""
            UPDATE CNAE
            SET CNAE = ?
            WHERE CNPJ_Instituicao= ? AND CNAE = ?
        """, (cnae_novo, cnpj_instituicao, cnae_antigo))

        print("CNAE atualizado com sucesso!")
    except pyodbc.Error as e:
        print("Erro ao atualizar CNAE:", e)
