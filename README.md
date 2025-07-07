# Banco de Dados de Projetos de Pesquisa da UnB

Projeto da disciplina Banco de Dados, turma 01, ministrada pela professora
Maristela Terto de Holanda.

# Modelagem

Os modelos MER e MR que representam a estrutura do banco de dados desenvolvido
e os códigos SQL usados para estruturá-lo estão disponíveis na diretório
`media`.

# Como utilizar

### Requisitos:
- PostgreSQL
- Devart ODBC Driver for PostgreSQL
- Python 3.10+
- pyodbc
- psycopg2-binary

Para instalar os pacotes Python:
```sh
pip install pyodbc psycopg2-binary
```

### Execução

Para rodar o programa, execute na raíz do diretório o comando:
```sh
python main.py
```

O sistema permite que você crie uma conta de um dos tipos disponíveis
(Instituição, Pesquisador, Estudante, Colaborador Externo), crie um projeto
e pesquise projetos no banco de dados.
