# Banco de Dados de Projetos de Pesquisa da UnB

Projeto da disciplina Banco de Dados, turma 01, ministrada pela professora
Maristela Terto de Holanda.

# Modelagem

Os modelos [MER](media/MER.png) e [MR](media/MR.png) que representam a
estrutura do banco de dados desenvolvido e os códigos SQL usados para estruturá
-lo estão disponíveis no diretório [media](media).

# Códigos SQL

Os códigos SQL base para criar o banco de dados estão também em `media`:
- [script_db.sql](media/script_db.sql) - criação das tabelas do banco de dados
- [script_procedure.sql](media/script_procedure.sql) - criação das procedures
utilizadas
- [script_view.sql](media/script_view.sql) - criação das views utilizadas para
pesquisa de projetos e visualização de membros e instituições

Porém, além deles, o CRUD de contas utiliza códigos SQL próprios para suas
funções.

# Manual de uso

### Requisitos:
Requisitos disponiveis em: [requirements.txt](requirements.txt)

Para instalar os pacotes Python:
- Certifique-se de que está no ambiente virtual
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```
- Execute o comando:
    ```sh
    pip install -r requirements.txt
    ```

### Execução

Para rodar o programa, execute na raíz do diretório o comando:
```sh
python main.py
```

O sistema permite que você crie uma conta de um dos tipos disponíveis
(Instituição, Pesquisador, Estudante, Colaborador Externo), crie um projeto
e pesquise projetos no banco de dados.
