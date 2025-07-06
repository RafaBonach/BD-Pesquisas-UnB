"""
    Aqui estão as definições dos modelos do banco de dados.
    Esses modelos serão usados para fazer o CRUD dos dados das tabelas e demais funções relacionadas.
"""
import pyodbc

class Pesquisa_projeto:
    def __init__(self, id="", projeto="", nome_instituicao="", nome_membro="", tipo_projeto="", linha_pesquisa="", area_atuacao=""):
        self.id = id
        self.projeto = projeto
        self.nome_instituicao = nome_instituicao
        self.nome_membro = nome_membro
        self.tipo_projeto = tipo_projeto
        self.linha_pesquisa = linha_pesquisa
        self.area_atuacao = area_atuacao

    def resultado_pesquisa(self, cursor):
        operacao = ""
        if self.id != "":
            operacao += f"PROJETO.Cod_Proj = {self.id} AND "

        if self.projeto != "":
            operacao += f"Título LIKE '%{self.projeto}%' AND "
        
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
                SELECT PROJETO.Cod_Proj id_proj ,Título titulo, PROJETO.Resumo resumo_proj, Data_inicio, Data_final, STRING_AGG(Nome_Tipo, ', ') AS Nome_Tipo, STRING_AGG(MEMBRO.nome || ' (' || Pesquisa.Funcao || ')', E'\n') AS Nome_membro, STRING_AGG(INSTITUICAO.Nome, ', ') AS Nome_instituicao, STRING_AGG(LINHA_PESQUISA.Nome, ', ') AS Linha_pesquisa, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(CONGRESSO.Nome, ', ') as nome_congresso
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
                group by PROJETO.Cod_Proj, Título, PROJETO.Resumo, Data_inicio, Data_final
                order by Título;"""
            
        else:
            script = f"""
                SELECT PROJETO.Cod_Proj, Título titulo, PROJETO.Resumo resumo_proj, Data_inicio, Data_final, STRING_AGG(Nome_Tipo, ', ') AS Nome_Tipo, STRING_AGG(MEMBRO.nome || ' (' || Pesquisa.Funcao || ')', E'\n') AS Nome_membro_pesquisador, STRING_AGG(INSTITUICAO.Nome, ', ') AS Nome_instituicao, STRING_AGG(LINHA_PESQUISA.Nome, ', ') AS Linha_pesquisa, STRING_AGG(AREA_ATUACAO.Nome, ', ') AS Nome_area_atuacao, STRING_AGG(CONGRESSO.Nome, ', ') as nome_congresso
                FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO, Pesquisa, Fomenta, Vincula, Executa, CONGRESSO, Participa, Realiza, Financia
                WHERE ((Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) OR
                        (PROJETO.Cod_Proj = Realiza.Cod_Proj AND Realiza.Id_Estudante = MEMBRO.Id_Membro)) AND
                        ((PROJETO.Cod_Proj = Fomenta.Cod_Proj AND INSTITUICAO.CNPJ = Fomenta.CNPJ) OR
                        (PROJETO.Cod_Proj = Financia.Cod_Proj AND INSTITUICAO.CNPJ = Financia.CNPJ)) AND 
                        (AREA_ATUACAO.Id_Area_Atuacao = Vincula.Id_Area_Atuacao and Vincula.Cod_Proj = PROJETO.Cod_Proj) AND 
                        (PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj) AND 
                        (PROJETO.Cod_Proj = Executa.Cod_Proj AND Executa.Id_Linha_Pesquisa = LINHA_PESQUISA.Id_Linha_Pesquisa) AND 
                        (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj)
                group by PROJETO.Cod_Proj, Título, PROJETO.Resumo, Data_inicio, Data_final
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
    def __init__(self, id="", nome_instituicao="", sigla="", cnpj="", natureza_juridica="", uf="", localidade=""):
        self.id = id
        self.nome_instituicao = nome_instituicao
        self.cnpj = cnpj
        self.sigla = sigla
        self.natureza_juridica = natureza_juridica
        self.uf = uf
        self.localidade = localidade
    
    
    def info_instituicao(self, cursor):
        operacao = ""
        if self.id != "":
            operacao += f"INSTITUICAO.CNPJ = '{self.id}' AND "
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
    def __init__(self, cod_projeto="", titulo="", resumo="", data_inicio="", data_final="", id_t_projeto="",tipo_projeto="", localidade=None, linha_pesquisa=None, membro=None, area_atuacao=None, congresso=None, instituicao=None, patrimonio=None):
        # info projeto
        self.cod_projeto = cod_projeto
        self.titulo = titulo
        self.resumo = resumo
        self.data_inicio = data_inicio
        self.data_final = data_final

        # info tipo projeto
        self.id_t_projeto = id_t_projeto
        self.nome_tipo_projeto = tipo_projeto

        # info localizacao
        self.localidade = localidade

        # info linha pesquisa
        self.linha_pesquisa = linha_pesquisa

        # info membro
        self.membro = membro

        # info area atuacao
        self.area_atuacao = area_atuacao

        # info congresso
        self.congresso = congresso

        # info instituicao financeira
        self.instituicao = instituicao

        # info patrimonio
        self.patrimonio = patrimonio

    """
    ====================================================================================
    CRUD para o tipo de projeto
    ====================================================================================
    """
    def criar_t_projeto(self, cursor):
        try:
            script = f"CALL inserir_tipo_projeto('{self.nome_tipo_projeto}');"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar tipo de projeto: {e}")
            return False

    def lista_t_projetos(self, cursor):
        try:
            if self.id_t_projeto:
                script = f"SELECT Id_Tipo_Proj, Nome_Tipo FROM TIPO_PROJETO WHERE Id_Tipo_Proj = {self.id_t_projeto};"
                cursor.execute(script)
                tipos_projeto = cursor.fetchall()
                return tipos_projeto
            elif self.nome_tipo_projeto:
                script = f"SELECT Id_Tipo_Proj, Nome_Tipo FROM TIPO_PROJETO WHERE Nome_Tipo LIKE '%{self.nome_tipo_projeto}%';"
                cursor.execute(script)
                tipos_projeto = cursor.fetchall()
                return tipos_projeto
            else:
                script = "SELECT Id_Tipo_Proj, Nome_Tipo FROM TIPO_PROJETO;"
                cursor.execute(script)
                tipos_projeto = cursor.fetchall()
                return tipos_projeto
        except pyodbc.Error as e:
            print(f"Erro ao buscar tipos de projeto: {e}")
            return None
        
    def deleta_t_projeto(self, cursor):
        try:
            script = f"CALL deletar_tipo_projeto({self.id_t_projeto});"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao deletar tipo de projeto: {e}")
            return False

    """
    ==========================================================================================
        CRUD para o projeto
    ==========================================================================================
    """

    def cria_projeto(self, cursor):
        try:
            script = f"""CALL inserir_projeto({self.id_t_projeto}, '{self.titulo}', '{self.data_inicio}', '{self.data_final}');"""
            cursor.execute(script)
            cursor.commit()
            if self.resumo:
                script = f"UPDATE PROJETO SET Resumo = '{self.resumo}' WHERE Título = '{self.titulo}';"
                cursor.execute(script)
                cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar o projeto: {e}")
            return False
        
    def lista_projetos(self, cursor):
        try:
            script = """
            SELECT PROJETO.Cod_Proj, Título, Resumo, Data_inicio, Data_final, Nome_Tipo
            FROM PROJETO, TIPO_PROJETO
            WHERE PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj;
            """
            cursor.execute(script)
            projetos = cursor.fetchall()
            return projetos
        except pyodbc.Error as e:
            print(f"Erro ao buscar projetos: {e}")
            return None
    
    def busca_projeto(self, cursor):
        try:
            if self.cod_projeto:
                script = f"SELECT * FROM PROJETO WHERE Cod_Proj = {self.cod_projeto};"
                cursor.execute(script)
                projeto = cursor.fetchone()
                return projeto
            elif self.titulo:
                script = f"SELECT * FROM PROJETO WHERE Título LIKE '%{self.titulo}%';"
                cursor.execute(script)
                projeto = cursor.fetchall()
                return projeto
            else:
                print("Código do projeto não fornecido.")
                return None
        except pyodbc.Error as e:
            print(f"Erro ao buscar o projeto: {e}")
            return None

        
    def atualiza_projeto(self, cursor):
        try:
            operacao = ""
            if self.titulo:
                operacao += f"Título = '{self.titulo}', "
            if self.resumo:
                operacao += f"Resumo = '{self.resumo}', "
            if self.data_inicio:
                operacao += f"Data_inicio = '{self.data_inicio}', "
            if self.data_final:
                operacao += f"Data_final = '{self.data_final}', "
            if self.id_t_projeto:
                operacao += f"Id_Tipo_Proj = {self.id_t_projeto}, "
            
            operacao = operacao[:-2]  # Remove the last comma and space
            if not operacao:
                print("Nenhuma informação para atualizar.")
                return False
            script = f"""
            UPDATE PROJETO
            SET {operacao}
            WHERE Cod_Proj = {self.cod_projeto};
            """
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao atualizar o projeto: {e}")
            return False
        
    def deleta_projeto(self, cursor):
        try:
            script = f"CALL deletar_projeto({self.cod_projeto});"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao deletar projeto: {e}")
            return False
        
    def insere_localidade(self, cursor):
        if not self.localidade:
            print("Localidade não definida.")
            return False
        try:
            script = f"CALL vincular_projeto_localidade({self.cod_projeto}, {self.localidade.cod_postal});"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir localidade: {e}")
            return False
        
    def insere_linha_pesquisa(self, cursor):
        if not self.linha_pesquisa:
            print("Linha de pesquisa não definida.")
            return False
        try:
            script = f"CALL vincular_projeto_linha_pesquisa({self.cod_projeto}, {self.linha_pesquisa.id_linha});"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir linha de pesquisa: {e}")
            return False
    
    def insere_area_atuacao(self, cursor):
        if not self.area_atuacao:
            print("Área de atuação não definida.")
            return False
        try:
            script = f"CALL vincular_projeto_area_atuacao({self.cod_projeto}, {self.area_atuacao.id_area});"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir área de atuação: {e}")
            return False

    def insere_congresso(self, cursor):
        if not self.congresso:
            print("Congresso não definido.")
            return False
        try:
            script = f"CALL vincular_projeto_congresso({self.cod_projeto}, {self.congresso.id_congresso}, '{self.congresso.objetivo}');"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir congresso: {e}")
            return False
        
    def insere_instituicao(self, cursor):
        if not self.instituicao:
            print("Instituição não definida.")
            return False
        try:
            if self.instituicao.tipo_fomento == '':
                script = f"CALL instituicao_financia_projeto({self.instituicao.cnpj}, {self.cod_projeto});"
                cursor.execute(script)
                cursor.commit()
                return True
            else:
                script = f"CALL instituicao_fomenta_projeto({self.instituicao.cnpj}, {self.cod_projeto}, '{self.instituicao.tipo_fomento}');"
                cursor.execute(script)
                cursor.commit()
                return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir instituição: {e}")
            return False
    
    def insere_patrimonio(self, cursor):
        if not self.patrimonio:
            print("Patrimônio não definido.")
            return False
        try:
            script = f"CALL inserir_patrimonio({self.cod_projeto}, '{self.patrimonio.nome_patrimonio}', {self.patrimonio.custo_patrimonio}, '{self.patrimonio.especificacao_patrimonio}');"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir patrimônio: {e}")
            return False

    def insere_membro(self, cursor, tipo_membro=""):
        tipo_membro = tipo_membro.upper()
        if not self.membro:
            print("Membro não definido.")
            return False
        try:
            if tipo_membro == "ESTUDANTE":
                script = f"CALL vincular_estudante_projeto({self.cod_projeto}, {self.membro.id_membro});"
                cursor.execute(script)
                cursor.commit()
                return True
            else:
                script = f"CALL vincular_pesquisador_projeto({self.cod_projeto}, {self.membro.id_membro}, '{self.membro.funcao}');"
                cursor.execute(script)
                cursor.commit()
                return True
        except pyodbc.Error as e:
            print(f"Erro ao inserir membro: {e}")
            return False


class Localidade:
    def __init__(self, cod_postal="", pais="", uf="", cidade=""):
        self.cod_postal = cod_postal
        self.pais = pais
        self.uf = uf
        self.cidade = cidade

    def criar_localidade(self, cursor):
        try:
            if not self.cod_postal or not self.pais or not self.uf or not self.cidade:
                print("Todos os campos devem ser preenchidos para criar uma localidade.")
                return False
            script = f"CALL inserir_localidade('{self.cod_postal}', '{self.pais}', '{self.uf}', '{self.cidade}');"
            cursor.execute(script)
            cursor.commit()
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar localidade: {e}")
            return False

    def lista_localidades(self, cursor):
        try:
            script = "SELECT * FROM LOCALIDADE;"
            cursor.execute(script)
            localidades = cursor.fetchall()
            return localidades
        except pyodbc.Error as e:
            print(f"Erro ao buscar localidades: {e}")
            return None

class LinhaPesquisa:
    def __init__(self, id_linha="", nome_linha="", descricao_linha=""):
        self.id_linha = id_linha
        self.nome_linha = nome_linha
        self.descricao_linha = descricao_linha

    def criar_linha_pesquisa(self, cursor):
        try:
            script = f"CALL inserir_linha_pesquisa('{self.nome_linha}', '{self.descricao_linha}');"
            cursor.execute(script)
            cursor.commit()

            script = f"SELECT Id_Linha_Pesquisa FROM LINHA_PESQUISA WHERE Nome = '{self.nome_linha}';"
            cursor.execute(script)
            linha_pesquisa = cursor.fetchone()
            if linha_pesquisa:
                self.id_linha = linha_pesquisa[0]
            else:
                print("Linha de pesquisa não encontrada após criação.")
                return False
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar linha de pesquisa: {e}")
            return False

    def lista_linhas_pesquisa(self, cursor):
        try:
            script = "SELECT * FROM LINHA_PESQUISA;"
            cursor.execute(script)
            linhas_pesquisa = cursor.fetchall()
            return linhas_pesquisa
        except pyodbc.Error as e:
            print(f"Erro ao buscar linhas de pesquisa: {e}")
            return None      


class Membro:
    def __init__(self, id_membro="", funcao="pesquisador"):
        self.id_membro = id_membro
        self.funcao = funcao.lower()

    def lista_membros(self, cursor, tipo_membro):
        tipo_membro = tipo_membro.upper()
        try:
            if tipo_membro == "PESQUISADOR":
                
                script = "SELECT * FROM MEMBRO WHERE Departamento IS NOT NULL;"
                cursor.execute(script)
                pesquisadores = cursor.fetchall()
                return pesquisadores
                
            elif tipo_membro == "ESTUDANTE":

                script = "SELECT * FROM MEMBRO WHERE Matrícula IS NOT NULL;"
                cursor.execute(script)
                estudantes = cursor.fetchall()
                return estudantes
            
            else:

                script = "SELECT * FROM MEMBRO WHERE Matrícula IS NULL AND Departamento IS NULL;"
                cursor.execute(script)
                membros = cursor.fetchall()
                return membros
            
        except pyodbc.Error as e:
            print(f"Erro ao buscar membro: {e}")
            return None
        
class AreaAtuacao:
    def __init__(self, id_area="", abrangencia="", nome_area="", descricao_area=""):
        self.id_area = id_area
        self.abrangencia = abrangencia
        self.nome_area = nome_area
        self.descricao_area = descricao_area

    def criar_area_atuacao(self, cursor):
        try:
            script = f"CALL inserir_area_atuacao('{self.nome_area}', '{self.abrangencia}', '{self.descricao_area}');"
            cursor.execute(script)
            cursor.commit()

            script = f"SELECT Id_Area_Atuacao FROM AREA_ATUACAO WHERE Nome = '{self.nome_area}';"
            cursor.execute(script)
            area_atuacao = cursor.fetchone()
            if area_atuacao:
                self.id_area = area_atuacao[0]
            else:
                print("Área de atuação não encontrada após criação.")
                return False
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar área de atuação: {e}")
            return False

    def lista_areas_atuacao(self, cursor):
        try:
            script = "SELECT * FROM AREA_ATUACAO;"
            cursor.execute(script)
            areas_atuacao = cursor.fetchall()
            return areas_atuacao
        except pyodbc.Error as e:
            print(f"Erro ao buscar áreas de atuação: {e}")
            return None

class Congresso:
    def __init__(self, id_congresso="", nome_congresso="", desc_congresso="", objetivo=""):
        self.id_congresso = id_congresso
        self.nome_congresso = nome_congresso
        self.desc_congresso = desc_congresso
        self.objetivo = objetivo

    def criar_congresso(self, cursor):
        try:
            script = f"CALL inserir_congresso('{self.nome_congresso}', '{self.desc_congresso}');"
            cursor.execute(script)
            cursor.commit()

            script = f"SELECT Id_Congresso FROM CONGRESSO WHERE Nome = '{self.nome_congresso}';"
            cursor.execute(script)
            congresso = cursor.fetchone()
            if congresso:
                self.id_congresso = congresso[0]
            else:
                print("Congresso não encontrado após criação.")
                return False
            return True
        except pyodbc.Error as e:
            print(f"Erro ao criar congresso: {e}")
            return False

    def lista_congressos(self, cursor):
        try:
            script = "SELECT * FROM CONGRESSO;"
            cursor.execute(script)
            congressos = cursor.fetchall()
            return congressos
        except pyodbc.Error as e:
            print(f"Erro ao buscar congressos: {e}")
            return None
        
class Instituicao:
    def __init__(self, cnpj="", tipo_fomento=""):
        self.cnpj = cnpj
        self.tipo_fomento = tipo_fomento

    def lista_instituicoes(self, cursor):
        try:
            
            script = "SELECT * FROM INSTITUICAO;"
            cursor.execute(script)
            instituicoes = cursor.fetchall()
            return instituicoes
        
        except pyodbc.Error as e:
            print(f"Erro ao buscar instituições: {e}")
            return None
        
class Patrimonio:
    def __init__(self, id_patrimonio="", nome_patrimonio="", custo_patrimonio="", especificacao_patrimonio=""):
        self.id_patrimonio = id_patrimonio
        self.nome_patrimonio = nome_patrimonio
        self.custo_patrimonio = custo_patrimonio
        self.especificacao_patrimonio = especificacao_patrimonio

    def lista_patrimonios(self, cursor):
        try:
            script = "SELECT * FROM PATRIMONIO;"
            cursor.execute(script)
            patrimonios = cursor.fetchall()
            return patrimonios
        except pyodbc.Error as e:
            print(f"Erro ao buscar patrimônios: {e}")
            return None
        
    

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
