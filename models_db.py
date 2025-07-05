"""
    Aqui estão as definições dos modelos do banco de dados.
    Esses modelos serão usados para fazer o CRUD dos dados das tabelas e demais funções relacionadas.
"""
import pyodbc


class Pesquisa_projeto:
    def __init__(self, projeto="", nome_instituicao="", nome_membro="", tipo_projeto="", linha_pesquisa="", area_atuacao=""):
        self.projeto = projeto
        self.nome_instituicao = nome_instituicao
        self.nome_membro = nome_membro
        self.tipo_projeto = tipo_projeto
        self.linha_pesquisa = linha_pesquisa
        self.area_atuacao = area_atuacao

    def resultado_pesquisa(self, cursor):
        operacao = ""
        if self.projeto != "":
            operacao += f"titulo LIKE '%{self.projeto}%' AND "
        
        if self.nome_instituicao != "":
            operacao += f"INSTITUICAO.Nome LIKE '%{self.nome_instituicao}%' AND "

        if self.nome_membro != "":
            operacao += f"MEMBRO.nome LIKE '%{self.nome_membro}%' AND "
        
        if self.tipo_projeto != "":
            operacao += f"TIPO_PROJETO.Nome_Tipo LIKE '%{self.tipo_projeto}%' AND "
        
        if self.linha_pesquisa != "":
            operacao += f"LINHA_PESQUISA.Nome LIKE '%{self.linha_pesquisa}%' AND "
        
        if self.area_atuacao != "":
            operacao += f"AREA_ATUACAO.Nome LIKE '%{self.area_atuacao}%' AND "

        if operacao != "":
            operacao = operacao[:-5]

            
            script = f"""
                SELECT Título titulo, PROJETO.Resumo resumo_proj, Data_inicio, Data_final, STRING_AGG(Nome_Tipo, ', ') AS Nome_Tipo, STRING_AGG(MEMBRO.nome || ' (' || Pesquisa.Funcao || ')', E'\n') AS Nome_membro, STRING_AGG(INSTITUICAO.Nome, ', ') AS Nome_instituicao, STRING_AGG(LINHA_PESQUISA.Nome, ', ') AS Linha_pesquisa, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(CONGRESSO.Nome, ', ') as nome_congresso
                FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO, Pesquisa, Fomenta, Vincula, Executa, CONGRESSO, Participa, Realiza, Financia
                WHERE ((Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) OR
                        (PROJETO.Cod_Proj = Realiza.Cod_Proj AND Realiza.Id_Estudante = MEMBRO.Id_Membro)) AND
                        ((PROJETO.Cod_Proj = Fomenta.Cod_Proj AND INSTITUICAO.CNPJ = Fomenta.CNPJ) OR
                        (PROJETO.Cod_Proj = Financia.Cod_Proj AND INSTITUICAO.CNPJ = Financia.CNPJ)) AND 
                        (AREA_ATUACAO.Id_Area_Atuacao = Vincula.Id_Area_Atuacao and Vincula.Cod_Proj = PROJETO.Cod_Proj) AND 
                        (PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj) AND 
                        (PROJETO.Cod_Proj = Executa.Cod_Proj AND Executa.Id_Linha_Pesquisa = LINHA_PESQUISA.Id_Linha_Pesquisa) AND 
                        (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj) AND
                        {operacao}
                group by titulo, Resumo, Data_inicio, Data_final
                order by titulo;"""
            
        else:
            script = f"""
                SELECT Título titulo, PROJETO.Resumo resumo_proj, Data_inicio, Data_final, STRING_AGG(Nome_Tipo, ', ') AS Nome_Tipo, STRING_AGG(MEMBRO.nome || ' (' || Pesquisa.Funcao || ')', E'\n') AS Nome_membro_pesquisador, STRING_AGG(INSTITUICAO.Nome, ', ') AS Nome_instituicao, STRING_AGG(LINHA_PESQUISA.Nome, ', ') AS Linha_pesquisa, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(CONGRESSO.Nome, ', ') as nome_congresso
                FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO, Pesquisa, Fomenta, Vincula, Executa, CONGRESSO, Participa, Realiza, Financia
                WHERE ((Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) OR
                        (PROJETO.Cod_Proj = Realiza.Cod_Proj AND Realiza.Id_Estudante = MEMBRO.Id_Membro)) AND
                        ((PROJETO.Cod_Proj = Fomenta.Cod_Proj AND INSTITUICAO.CNPJ = Fomenta.CNPJ) OR
                        (PROJETO.Cod_Proj = Financia.Cod_Proj AND INSTITUICAO.CNPJ = Financia.CNPJ)) AND 
                        (AREA_ATUACAO.Id_Area_Atuacao = Vincula.Id_Area_Atuacao and Vincula.Cod_Proj = PROJETO.Cod_Proj) AND 
                        (PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj) AND 
                        (PROJETO.Cod_Proj = Executa.Cod_Proj AND Executa.Id_Linha_Pesquisa = LINHA_PESQUISA.Id_Linha_Pesquisa) AND 
                        (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj)
                group by titulo, Resumo, Data_inicio, Data_final
                order by titulo;"""

        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return [resultados]
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

class Pesquisa_pesquisador:
    def __init__(self, id=None, nome_membro="", nome_instituicao="", area_atuacao=""):
        self.id = id
        self.nome_membro = nome_membro
        self.nome_instituicao = nome_instituicao
        self.area_atuacao = area_atuacao

    
    def info_pesquisador(self, cursor):
        operacao = ""
        if self.nome_membro != "":
            operacao += f"Nome_membro LIKE '%{self.nome_membro}%' AND "
        
        if self.nome_instituicao != "":
            operacao += f"Departamento LIKE '%{self.nome_instituicao}%' AND "

        if self.area_atuacao != "":
            operacao += f"AREA_ATUACAO.Nome LIKE '%{self.area_atuacao}%' AND "
        
        if operacao != "":
            operacao = operacao[:-5]

            script = f"""
            SELECT MEMBRO.Id_Membro id, MEMBRO.Nome Nome_membro, Titulação titulacao, Departamento, MEMBRO.Descrição descricao_membro, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(Email, ', ') as email_membro, COUNT(PROJETO.Cod_Proj), STRING_AGG(País, ', ') as pais, STRING_AGG(UF, ', ') as uf, STRING_AGG(Cidade, ', ') as cidade
            FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
            WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
                    (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
                    (Email.id_membro = MEMBRO.Id_Membro) AND
                    (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro) AND
                    {operacao}
            group by Nome_membro, titulacao, Departamento, descricao_membro, Departamento
            order by Nome_membro;"""
    
        else:
            script = f"""
            SELECT MEMBRO.Id_Membro id, MEMBRO.Nome Nome_membro, Titulação titulacao, Departamento, MEMBRO.Descrição descricao_membro, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(Email, ', ') as email_membro, COUNT(PROJETO.Cod_Proj), STRING_AGG(País, ', ') as pais, STRING_AGG(UF, ', ') as uf, STRING_AGG(Cidade, ', ') as cidade
            FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
            WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
                    (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
                    (Email.id_membro = MEMBRO.Id_Membro) AND
                    (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro)
            group by Nome_membro, titulacao, Departamento, descricao_membro, Departamento
            order by Nome_membro;"""

        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    
    def info_pesquisador_detalhado(self, cursor):
        operacao = "MEMBRO.Id_Membro = {self.id} AND " 
        if self.area_atuacao != "":
            operacao += f"MEMBRO.Nome LIKE '%{self.area_atuacao}%' AND "
        
        operacao = operacao[:-5]

        script = f"""
        SELECT MEMBRO.Id_Membro id_membro, MEMBRO.Nome Nome_membro, Titulação titulacao, Departamento, MEMBRO.Descrição descricao_membro, STRING_AGG(Email, ', ') as email_membro, STRING_AGG(País, ', ') as pais, STRING_AGG(UF, ', ') as uf, STRING_AGG(Cidade, ', ') as cidade, STRING_AGG(AREA_ATUACAO.Nome, E'\n') AS Nome_area_atuacao, STRING_AGG(PROJETO.Título || '(' || Pesquisa.Funcao || ')' || ': ' || PROJETO.Resumo, E'\n') AS Projetos, COUNT(CONGRESSO.Id_Congresso), STRING_AGG(CONGRESSO.Nome, E'\n') AS Congresso
        FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email, CONGRESSO, Participa
        WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
                (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
                (Email.id_membro = MEMBRO.Id_Membro) AND
                (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro) AND
                (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj) AND
                {operacao}
        GROUP BY MEMBRO.Id_Membro, Nome_membro, titulacao, Departamento, descricao_membro, Departamento, PROJETO.Título
		ORDER BY PROJETO.Título;"""

        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

class Pesquisa_estudante:
    def __init__(self, id=None, nome_estudante="", titulacao="", descricao="", matricula="", curso_estudante=""):
        self.id = id
        self.nome_estudante = nome_estudante
        self.titulacao = titulacao
        self.descricao = descricao
        self.matricula = matricula
        self.curso_estudante = curso_estudante

    def info_estudante(self, cursor):
        operacao = ""
        if self.id is not None:
            operacao += f"Id_Estudante = {self.id} AND "

        if self.nome_estudante != "":
            operacao += f"Nome LIKE '%{self.nome_estudante}%' AND "
        
        if self.titulacao != "":
            operacao += f"Titulacao LIKE '%{self.titulacao}%' AND "

        if self.descricao != "":
            operacao += f"Descrição LIKE '%{self.descricao}%' AND "

        if self.matricula != "":
            operacao += f"Matricula LIKE '%{self.matricula}%' AND "

        if self.curso_estudante != "":
            operacao += f"Curso LIKE '%{self.curso_estudante}%' AND "

        if operacao != "":
            operacao = operacao[:-5]

            script = f"""
            SELECT MEMBRO.Id_Membro id, Nome, MEMBRO.Titulação titulacao, Descrição descricao_estudante, Matrícula matricula, Curso_estudante Curso, STRING_AGG(Email, ', ') as email_estudante, STRING_AGG(País, ', ') as pais, STRING_AGG(UF, ', ') as uf, STRING_AGG(Cidade, ', ') as cidade, STRING_AGG(PROJETO.Título, E'\n') AS Projetos, COUNT(PROJETO.Cod_Proj) as num_projetos
            FROM MEMBRO, LOCALIDADE, Origem, Email, Realiza, PROJETO
            WHERE (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
                    (Email.id_membro = MEMBRO.Id_Membro) AND
                    (Realiza.Id_Estudante = MEMBRO.Id_Membro AND Realiza.Cod_Proj = PROJETO.Cod_Proj) AND
                    {operacao}
            GROUP BY id, Nome, Titulacao, Descrição, Matricula, Curso;"""
        
        else:
            script = f"""
            SELECT MEMBRO.Id_Membro id, Nome, MEMBRO.Titulação titulacao, Descrição descricao_estudante, Matrícula matricula, Curso_estudante Curso, STRING_AGG(Email, ', ') as email_estudante, STRING_AGG(País, ', ') as pais, STRING_AGG(UF, ', ') as uf, STRING_AGG(Cidade, ', ') as cidade, STRING_AGG(PROJETO.Título, E'\n') AS Projetos, COUNT(PROJETO.Cod_Proj) as num_projetos
            FROM MEMBRO, LOCALIDADE, Origem, Email, Realiza, PROJETO
            WHERE (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
                    (Email.id_membro = MEMBRO.Id_Membro) AND
                    (Realiza.Id_Estudante = MEMBRO.Id_Membro AND Realiza.Cod_Proj = PROJETO.Cod_Proj)
            GROUP BY id, Nome, Titulacao, Descrição, Matricula, Curso;"""
        
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return {resultado[0]:resultado[1:] for resultado in resultados}
            
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        

class Pesquisa_instituicao:
    def __init__(self, nome_instituicao="", sigla="", cnpj="", natureza_juridica="", uf="", localidade=""):
        self.nome_instituicao = nome_instituicao
        self.cnpj = cnpj
        self.sigla = sigla
        self.natureza_juridica = natureza_juridica
        self.uf = uf
        self.localidade = localidade
    
    
    def info_instituicao(self, cursor):
        operacao = ""
        if self.cnpj != "":
            operacao += f"cnpj = {self.cnpj} AND"

        if self.nome_instituicao != "":
            operacao += f"Nome LIKE '%{self.nome_instituicao}%' AND"

        if self.sigla != "":
            operacao += f"Sigla LIKE '%{self.sigla}%' AND"

        if self.natureza_juridica != "":
            operacao += f"Natureza_Juríd LIKE '%{self.natureza_juridica}%' AND"
        
        if self.uf != "":
            operacao += f"UF LIKE '%{self.uf}%' AND"

        if self.localidade != "":
            operacao += f"Localidade LIKE '%{self.localidade}%' AND"
        

        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
            SELECT INSTITUICAO.CNPJ cnpj, Nome, Sigla, Natureza_Juríd, Descrição descricao, UF, Localidade, Recursos_Investidos, STRING_AGG(id_proj_financiado || ' - ' || nome_proj_financiado, E'\n') AS Projetos_financiados, STRING_AGG(PROJETO.Cod_Proj || ' - ' || Título, E'\n') AS Projetos_fomentados
            FROM INSTITUICAO, PROJETO, Fomenta, (
                SELECT PROJETO.Cod_Proj id_proj_financiado, Título nome_proj_financiado, INSTITUICAO.CNPJ cnpj_instituicao, Nome nome_instituicao
                FROM PROJETO, Financia, INSTITUICAO
                WHERE (INSTITUICAO.CNPJ = Financia.CNPJ AND PROJETO.Cod_Proj = Financia.Cod_Proj)) AS Financia
            WHERE (INSTITUICAO.CNPJ = Fomenta.CNPJ AND PROJETO.Cod_Proj = Fomenta.Cod_Proj) AND
                    (INSTITUICAO.CNPJ = Financia.cnpj_instituicao) AND
                    {operacao}
            GROUP BY INSTITUICAO.CNPJ, Nome, Sigla, Natureza_Juríd, Descrição, UF, Localidade, Recursos_Investidos;"""
        
        else:
            script = f"""
            SELECT INSTITUICAO.CNPJ cnpj, Nome, Sigla, Natureza_Juríd, Descrição descricao, UF, Localidade, Recursos_Investidos, STRING_AGG(id_proj_financiado || ' - ' || nome_proj_financiado, E'\n') AS Projetos_financiados, STRING_AGG(PROJETO.Cod_Proj || ' - ' || Título, E'\n') AS Projetos_fomentados
            FROM INSTITUICAO, PROJETO, Fomenta, (
                SELECT PROJETO.Cod_Proj id_proj_financiado, Título nome_proj_financiado, INSTITUICAO.CNPJ cnpj_instituicao, Nome nome_instituicao
                FROM PROJETO, Financia, INSTITUICAO
                WHERE (INSTITUICAO.CNPJ = Financia.CNPJ AND PROJETO.Cod_Proj = Financia.Cod_Proj)) AS Financia
            WHERE (INSTITUICAO.CNPJ = Fomenta.CNPJ AND PROJETO.Cod_Proj = Fomenta.Cod_Proj) AND
                    (INSTITUICAO.CNPJ = Financia.cnpj_instituicao)
            GROUP BY INSTITUICAO.CNPJ, Nome, Sigla, Natureza_Juríd, Descrição, UF, Localidade, Recursos_Investidos;"""
            
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        

class Projeto:
    def __init__(self, tipo_projeto, titulo, resumo="", data_inicio="", data_final="", linha_pesquisa="", area_atuacao=""):
        self.titulo = titulo
        self.resumo = resumo
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.tipo_projeto = tipo_projeto
        self.linha_pesquisa = linha_pesquisa
        self.area_atuacao = area_atuacao

    def cria_projeto(self, cursor):
        try:
            script = f"""
            SELECT DISTINCT Id_Tipo_Proj FROM TIPO_PROJETO WHERE Nome_Tipo = '{self.tipo_projeto}';
            """
            cursor.execute(script)
            tipo_projeto_id = cursor.fetchone()
            if tipo_projeto_id == [[]]:
                script = f"""
                INSERT INTO TIPO_PROJETO (Nome_Tipo) VALUES ('{self.tipo_projeto}');
                SELECT Id_Tipo_Proj FROM TIPO_PROJETO WHERE Nome_Tipo = '{self.tipo_projeto}';
                """
                cursor.execute(script)
                tipo_projeto_id = cursor.fetchone()[0]
            else:
                tipo_projeto_id = tipo_projeto_id[0]

            script = f"""
            INSERT INTO PROJETO (Id_Tipo_Proj, Título, Resumo, Data_inicio, Data_final)
            VALUES ('{self.tipo_projeto_id}', '{self.titulo}', '{self.resumo}', '{self.data_inicio}', '{self.data_final}');
            """
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar o projeto: {e}")
            return False



def insert_account(cursor, acc_type, acc_name, acc_password):
    try:
        cursor.execute(f"INSERT INTO Conta (Id_Conta, Tipo, Nome, Senha) VALUES (DEFAULT, {acc_type}, '{acc_name}', '{acc_password}')")
        return True

    except pyodbc.Error as e:
        print(f"Erro na criação de conta!\n{e}")
        return -1

def account_in_db(cursor, acc_name, acc_password):
    try:
        acc_exists = len(cursor.execute(f"SELECT * FROM Conta WHERE Nome='{acc_name}' AND Senha='{acc_password}'").fetchall()) != 0

        return acc_exists

    except pyodbc.Error as e:
        print(f"Erro na consulta de conta!\n{e}")
        return -1

def get_acc(cursor, acc_name, acc_password):
    try:
        acc_record = cursor.execute(f"SELECT Id_Conta, Tipo FROM Conta WHERE Nome='{acc_name}' AND Senha='{acc_password}'").fetchall()

        if len(acc_record) == 0:
            return None

        return acc_record[0]

    except pyodbc.Error as e:
        print(f"Erro na consulta de conta!\n{e}")
        return None

def delete_acc_records(cursor):
    try:
        cursor.execute("DELETE FROM Conta")

    except pyodbc.Error as e:
        print(f"Erro na deleção de contas!\n{e}")
