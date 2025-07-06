import unittest
from unittest.mock import MagicMock
from interfaces.i_project import IProject
from models_db import Projeto, Localidade, LinhaPesquisa, AreaAtuacao, Congresso, Instituicao, Patrimonio

class TestIProject(unittest.TestCase):
    def setUp(self):
        self.cursor = MagicMock()
        self.i_project = IProject(self.cursor)
        self.projeto = Projeto(titulo="Projeto Teste", resumo="Resumo", data_inicio="2024-01-01", data_final="2024-12-31", id_t_projeto=1, tipo_projeto="Pesquisa")

    def test_create_project_success(self):
        self.cursor.execute.return_value = None
        self.cursor.commit.return_value = None

        self.projeto.criar_t_projeto = MagicMock(return_value=True)
        self.projeto.lista_t_projetos = MagicMock(return_value=[(1, "Pesquisa")])
        self.projeto.cria_projeto = MagicMock(return_value=True)
        self.projeto.busca_projeto = MagicMock(return_value=[(1,)])

        self.i_project.create_project(self.projeto)
        self.assertEqual(self.projeto.cod_projeto, 1)

    def test_update_project(self):
        self.projeto.atualiza_projeto = MagicMock(return_value=True)
        self.i_project.update_project(self.projeto)
        self.projeto.atualiza_projeto.assert_called_once()

    def test_delete_project(self):
        self.projeto.deleta_projeto = MagicMock(return_value=True)
        self.i_project.delete_project(self.projeto)
        self.projeto.deleta_projeto.assert_called_once()

    def test_create_localidade(self):
        localidade = Localidade(cod_postal="12345", pais="Brasil", uf="DF", cidade="Brasília")
        localidade.criar_localidade = MagicMock(return_value=True)
        self.i_project.create_localidade(localidade)
        localidade.criar_localidade.assert_called_once()

    def test_connect_projeto_localidade(self):
        self.projeto.localidade = Localidade(cod_postal="12345")
        self.projeto.insere_localidade = MagicMock(return_value=True)
        self.i_project.connect_projeto_localidade(self.projeto)
        self.projeto.insere_localidade.assert_called_once()

if __name__ == '__main__':
    unittest.main()
