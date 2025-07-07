# Banco de Dados de Projetos de Pesquisa da UnB

Projeto da disciplina Banco de Dados, turma 01, ministrada pela professora
Maristela Terto de Holanda.

# Modelagem

Os modelos MER e MR que representam a estrutura do banco de dados desenvolvido
e os códigos SQL usados para estruturá-lo estão disponíveis na diretório
`media`.

# Como utilizar

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
