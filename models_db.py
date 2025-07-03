"""
    Aqui estão as definições dos modelos do banco de dados.
    Esses modelos serão usados para fazer o CRUD dos dados das tabelas e demais funções relacionadas.
"""
import pyodbc
from backend_db import create_database
from utils import *
from interfaces.i_account import IAccount

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
            operacao += f"Título LIKE '%{self.projeto}%' AND"
        
        if self.nome_instituicao != "":
            operacao += f"Nome_instituicao LIKE '%{self.nome_instituicao}%' AND"

        if self.nome_membro != "":
            operacao += f"Nome_membro LIKE '%{self.nome_membro}%' AND"
        
        if self.tipo_projeto != "":
            operacao += f"Nome_Tipo LIKE '%{self.tipo_projeto}%' AND"
        
        if self.linha_pesquisa != "":
            operacao += f"linha_pesquisa LIKE '%{self.linha_pesquisa}%' AND"
        
        if self.area_atuacao != "":
            operacao += f"Nome_area_atuacao LIKE '%{self.area_atuacao}%' AND"

        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
Select * 
FROM (
    SELECT Título titulo, Resumo, Data_inicio, Data_final, MEMBRO.Nome Nome_membro, Funcao Funcao_membro, INSTITUICAO.Nome Nome_instituicao, Fomenta.Tipo Tipo_fomento, Nome_Tipo, LINHA_PESQUISA.Nome linha_pesquisa, LINHA_PESQUISA.Descrição Descrição_linha_pesquisa, AREA_ATUACAO.Nome Nome_area_atuacao, CONGRESSO.Nome nome_congresso
    FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO, Pesquisa, Fomenta, Vincula, Executa, CONGRESSO, Participa
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND 
            (PROJETO.Cod_Proj = Fomenta.Cod_Proj AND INSTITUICAO.CNPJ = Fomenta.CNPJ) AND 
            (AREA_ATUACAO.Id_Area_Atuacao = Vincula.Id_Area_Atuacao and Vincula.Cod_Proj = PROJETO.Cod_Proj) AND 
            (PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj) AND 
            (PROJETO.Cod_Proj = Executa.Cod_Proj AND Executa.Id_Linha_Pesquisa = LINHA_PESQUISA.Id_Linha_Pesquisa) AND 
            (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj)) 
WHERE {operacao}
order by titulo;"""
            
        else:
            script = f"""
Select * 
FROM (
    SELECT Título titulo, Resumo, Data_inicio, Data_final, MEMBRO.Nome Nome_membro, Funcao Funcao_membro, INSTITUICAO.Nome Nome_instituicao, Fomenta.Tipo Tipo_fomento, Nome_Tipo, LINHA_PESQUISA.Nome linha_pesquisa, LINHA_PESQUISA.Descrição Descrição_linha_pesquisa, AREA_ATUACAO.Nome Nome_area_atuacao, CONGRESSO.Nome nome_congresso
    FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO, Pesquisa, Fomenta, Vincula, Executa, CONGRESSO, Participa
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND 
            (PROJETO.Cod_Proj = Fomenta.Cod_Proj AND INSTITUICAO.CNPJ = Fomenta.CNPJ) AND 
            (AREA_ATUACAO.Id_Area_Atuacao = Vincula.Id_Area_Atuacao and Vincula.Cod_Proj = PROJETO.Cod_Proj) AND 
            (PROJETO.Id_Tipo_Proj = TIPO_PROJETO.Id_Tipo_Proj) AND 
            (PROJETO.Cod_Proj = Executa.Cod_Proj AND Executa.Id_Linha_Pesquisa = LINHA_PESQUISA.Id_Linha_Pesquisa) AND 
            (CONGRESSO.Id_Congresso = Participa.Id_Congresso AND Participa.Id_Proj = PROJETO.Cod_Proj))
order by titulo;"""

        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return [resultados]
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

class Pesquisa_pesquisador:
    def __init__(self, nome_membro="", nome_instituicao="", area_atuacao=""):
        self.nome_membro = nome_membro
        self.nome_instituicao = nome_instituicao
        self.area_atuacao = area_atuacao

    @classmethod
    def info_pesquisador(self, cursor):
        operacao = ""
        if self.nome_membro != "":
            operacao += f"Nome_membro LIKE '%{self.nome_membro}%' AND"
        
        if self.nome_instituicao != "":
            operacao += f"Departamento LIKE '%{self.nome_instituicao}%' AND"

        if self.area_atuacao != "":
            operacao += f"Nome_area_atuacao LIKE '%{self.area_atuacao}%' AND"
        
        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
SELECT *
FROM (
    SELECT MEMBRO.Nome Nome_membro, Titulação titulacao, MEMBRO.Descrição descricao_membro, Departamento, AREA_ATUACAO.Nome Nome_area_atuacao, Email, País pais, UF
    FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
            (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
            (Email.id_membro = MEMBRO.Id_Membro) AND
            (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro))
WHERE {operacao}
order by Nome_membro;"""

            
        else:
            script = f"""
SELECT *
FROM (
    SELECT MEMBRO.Nome Nome_membro, Titulação titulacao, MEMBRO.Descrição descricao_membro, Departamento, AREA_ATUACAO.Nome Nome_area_atuacao, Email, País pais, UF
    FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
            (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
            (Email.id_membro = MEMBRO.Id_Membro) AND
            (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro))
order by Nome_membro;
"""
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    @classmethod
    def info_pesquisador_detalhado(self, cursor):
        operacao = ""
        if self.nome_membro != "":
            operacao += f"Nome_membro LIKE '%{self.nome_membro}%' AND"
        
        if self.nome_instituicao != "":
            operacao += f"Departamento LIKE '%{self.nome_instituicao}%' AND"

        if self.area_atuacao != "":
            operacao += f"Nome_area_atuacao LIKE '%{self.area_atuacao}%' AND"
        
        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
SELECT *
FROM (
    SELECT MEMBRO.Nome Nome_membro, Titulação, Descrição, Departamento, AREA_ATUACAO.Nome Nome_area_atuacao, PROJETO.Título Título_projeto, PROJETO.Resumo Resumo_projeto, Email, País, UF
    FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
            (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
            (Email.id_membro AND MEMBRO.Id_Membro) AND
            (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro))
WHERE {operacao}
order by Nome_membro;"""

        else:
            script = f"""
SELECT *
FROM (
    SELECT MEMBRO.Nome Nome_membro, Titulação, Descrição, Departamento, AREA_ATUACAO.Nome Nome_area_atuacao PROJETO.Título Título_projeto, PROJETO.Resumo Resumo_projeto, Email, País, UF
    FROM  PROJETO, Pesquisa, AREA_ATUACAO, Atua, MEMBRO, LOCALIDADE, Origem, Email
    WHERE (Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro) AND
            (MEMBRO.Id_Membro = Origem.Id_Membro AND Origem.Cod_postal = LOCALIDADE.Cod_postal) AND
            (Email.id_membro AND MEMBRO.Id_Membro) AND
            (AREA_ATUACAO.Id_Area_Atuacao = Atua.Id_Area_Atuacao AND Atua.Id_Pesquisador = MEMBRO.Id_Membro))
order by Nome_membro;"""
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        
class Pesquisa_instituicao:
    def __init__(self, nome_instituicao="", sigla="", CNPJ=""):
        self.nome_instituicao = nome_instituicao
        self.CNPJ = CNPJ
        self.sigla = sigla
    
    @classmethod
    def info_instituicao(self, cursor):
        operacao = ""
        if self.CNPJ != "":
            operacao += f"CNPJ = {self.CNPJ} AND"

        if self.nome_instituicao != "":
            operacao += f"Nome LIKE '%{self.nome_instituicao}%' AND"

        if self.sigla != "":
            operacao += f"Sigla LIKE '%{self.sigla}%' AND"
        

        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
SELECT Nome, CNPJ, Sigla, UF, Localidade, Descrição
FROM INSTITUICAO
WHERE {operacao}
order by Nome;"""
        
        else:
            script = f"""
SELECT Nome, CNPJ, Sigla, UF, Localidade, Descrição
FROM INSTITUICAO
order by Nome;"""
            
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        
    @classmethod
    def info_instituicao_detalhado(self, cursor):
        operacao = ""
        if self.CNPJ != "":
            operacao += f"CNPJ = {self.CNPJ} AND"

        if self.nome_instituicao != "":
            operacao += f"Nome LIKE '%{self.nome_instituicao}%' AND"

        if self.sigla != "":
            operacao += f"Sigla LIKE '%{self.sigla}%' AND"
        
        if operacao != "":
            operacao = operacao[:-4]

            script = f"""
SELECT *
FROM (
    SELECT Nome, INSTITUICAO.CNPJ CNPJ, Sigla, UF, Localidade, Natureza_Juríd, Descrição, CNAE, COUNT(Fomenta.CNPJ) AS qtd_projetos_fomentados, count(Financia.CNPJ) AS qtd_projetos_financiados
    FROM INSTITUICAO, CNAE, Financia, Fomenta
    WHERE (INSTITUICAO.CNPJ = CNAE.CNPJ_Instituicao) AND
            (INSTITUICAO.CNPJ = Fomenta.CNPJ OR INSTITUICAO.CNPJ = Financia.CNPJ)
    group by INSTITUICAO.CNPJ, CNAE
    )
WHERE {operacao}
order by Nome;"""
        
        else:
            script = f"""
SELECT *
FROM (
    SELECT Nome, INSTITUICAO.CNPJ CNPJ, Sigla, UF, Localidade, Natureza_Juríd, Descrição, CNAE, COUNT(Fomenta.CNPJ) AS qtd_projetos_fomentados, count(Financia.CNPJ) AS qtd_projetos_financiados
    FROM INSTITUICAO, CNAE, Financia, Fomenta
    WHERE (INSTITUICAO.CNPJ = CNAE.CNPJ_Instituicao) AND
            (INSTITUICAO.CNPJ = Fomenta.CNPJ OR INSTITUICAO.CNPJ = Financia.CNPJ)
    group by INSTITUICAO.CNPJ, CNAE
    )
order by Nome;"""
            
        try:
            cursor.execute(script)
            resultados = cursor.fetchall()
            return resultados
        except pyodbc.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None