"""
    Aqui estão as definições dos modelos do banco de dados.
    Esses modelos serão usados para fazer o CRUD dos dados das tabelas e demais funções relacionadas.
"""
import pyodbc
import time
from backend_db import create_database
from utils import *
from interfaces.i_account import IAccount

class pesquisa_projeto:
    def __init__(self, projeto="", nome_instituicao="", nome_membro="", tipo_projeto="", linha_pesquisa="", area_atuacao=""):
        self.projeto = projeto
        self.nome_instituicao = nome_instituicao
        self.nome_membro = nome_membro
        self.tipo_projeto = tipo_projeto
        self.linha_pesquisa = linha_pesquisa
        self.area_atuacao = area_atuacao

    @classmethod
    def resultado_pesquisa(cursor):
        script = f"""Select * 
                    FROM (
                        SELECT Título, Resumo, Data_inicio, Data_final, MEMBRO.Nome Nome_membro, INSTITUICAO.Nome Nome_instituicao, Nome_Tipo, LINHA_PESQUISA.Nome linha_pesquisa, AREA_ATUACAO.Nome
                        FROM PROJETO, MEMBRO, INSTITUICAO, TIPO_PROJETO, LINHA_PESQUISA, AREA_ATUACAO
                        WHERE Pesquisa.Cod_Proj = PROJETO.Cod_Proj AND Pesquisa.Id_Pesquisador = MEMBRO.Id_Membro AND ) WHERE {operacao} """
