CREATE TABLE MEMBRO (
  Id_Membro        INT          PRIMARY KEY,
  Nome             VARCHAR(45)  NOT NULL,
  Titulação        VARCHAR(15)  NOT NULL,
  Descrição        text,

  /* Atributo de Pesquisador da UnB */
  Departamento     VARCHAR(30),

  /* Atributos de Estudante da UnB */
  Matrícula        INT          UNIQUE,
  Curso_estudante  VARCHAR(30)
);

/* Projeto tem um tipo */
CREATE TABLE TIPO_PROJETO (
  Id_Tipo_Proj  INT          GENERATED ALWAYS AS IDENTITY, /*Modifiquei id para serial*/
  Nome_Tipo     VARCHAR(20)  NOT NULL,

  PRIMARY KEY  (Id_Tipo_Proj) /*Modifiquei a chave primaria*/
);

CREATE TABLE PROJETO (
  Cod_Proj        INT          GENERATED ALWAYS AS IDENTITY,  /*Modifiquei id para serial*/
  Id_Tipo_Proj    INT,
  Título          VARCHAR(75)  NOT NULL,
  Data_final      DATE         NOT NULL,
  Data_inicio     DATE         NOT NULL,
  Resumo          text,
  relatorio       bytea,

  PRIMARY KEY  (Cod_Proj, Id_Tipo_Proj),
  UNIQUE	   (Cod_Proj),
  FOREIGN KEY  (Id_Tipo_Proj)    REFERENCES TIPO_PROJETO(Id_Tipo_Proj)
);

CREATE TABLE INSTITUICAO (
  CNPJ                 INT          PRIMARY KEY,
  Nome                 VARCHAR(40)  NOT NULL,
  Sigla                VARCHAR(10),
  Natureza_Juríd       VARCHAR(20),
  UF                   CHAR(2)      NOT NULL,
  Localidade           VARCHAR(30)  NOT NULL,
  Recursos_Investidos  INT,
  Descrição            text
);

CREATE TABLE CONGRESSO (
  Id_Congresso  INT          GENERATED ALWAYS AS IDENTITY,  /*Modifiquei id para serial*/
  Nome          VARCHAR(45)  NOT NULL,
  Descricao     text,

  PRIMARY KEY  (Id_Congresso) /*Modifiquei a chave primaria*/
);

CREATE TABLE LINHA_PESQUISA (
  Id_Linha_Pesquisa  INT          GENERATED ALWAYS AS IDENTITY, /*Modifiquei id para serial*/
  Nome               VARCHAR(45)  NOT NULL,
  Descrição          text,

  PRIMARY KEY  (Id_Linha_Pesquisa) /* Transformei id em PK */
);

CREATE TABLE AREA_ATUACAO (
  Id_Area_Atuacao  INT          GENERATED ALWAYS AS IDENTITY, /*Modifiquei id para serial*/
  Abrangencia      VARCHAR(12)  NOT NULL,
  Nome             VARCHAR(45)  NOT NULL,
  Descrição        text,

  PRIMARY KEY  (Id_Area_Atuacao) /* Transformei id em PK */
);

CREATE TABLE LOCALIDADE (
  Cod_postal  INT          PRIMARY KEY,
  País        VARCHAR(45)  NOT NULL,
  UF          CHAR(2)      NOT NULL,
  Cidade      VARCHAR(45)  NOT NULL
);

CREATE TABLE PATRIMONIO (
  Cod_Proj       INT,
  Id_Patrimonio  INT,
  Nome           VARCHAR(30)  NOT NULL,
  Custo          INT          NOT NULL,
  Especificacao  text,

  PRIMARY KEY  (Id_Patrimonio, Cod_Proj),
  FOREIGN KEY  (Cod_Proj)  REFERENCES  PROJETO(Cod_Proj)
);


/* Email de membro (multivalorado) */
CREATE TABLE Email (
  Email      VARCHAR(30),
  id_membro  INT,

  PRIMARY KEY (Email, id_membro),
  FOREIGN KEY (id_membro) REFERENCES MEMBRO(id_Membro)
);

/* Membro tem origem em Localidade */
CREATE TABLE Origem (
  Cod_postal  INT,
  Id_Membro   INT,

  PRIMARY KEY  (Id_Membro, Cod_postal),
  FOREIGN KEY  (Id_Membro)   REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (Cod_postal)  REFERENCES LOCALIDADE(Cod_postal)
);

/* Pesquisador atua em Área de atuação */
CREATE TABLE Atua (
  Id_Pesquisador   INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (Id_Pesquisador, Id_Area_Atuacao),
  FOREIGN KEY  (Id_Pesquisador)   REFERENCES  MEMBRO(Id_Membro),
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES  AREA_ATUACAO(Id_Area_Atuacao)
);

/* Pesquisador pesquisa Projeto */
CREATE TABLE Pesquisa (
  Id_Pesquisador  INT,
  Cod_Proj        INT,
  Funcao          VARCHAR(12)  NOT NULL,

  PRIMARY KEY  (Id_Pesquisador, Cod_Proj),
  FOREIGN KEY  (Id_Pesquisador)  REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (Cod_Proj)        REFERENCES PROJETO(Cod_Proj)
);

/* Estudante realiza Projeto */
CREATE TABLE Realiza (
  Id_Estudante  INT,
  Cod_Proj      INT,

  PRIMARY KEY  (Id_Estudante, Cod_Proj),
  FOREIGN KEY  (Id_Estudante)  REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (Cod_Proj)      REFERENCES PROJETO(Cod_Proj)
);


/* Projeto possui Localidade */
CREATE TABLE Possui (
  Cod_Proj    INT,
  Cod_postal  INT,

  PRIMARY KEY  (Cod_Proj, Cod_postal),
  FOREIGN KEY  (Cod_Proj)    REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (Cod_postal)  REFERENCES LOCALIDADE(Cod_postal)
);

/* Projeto vincula Área de atuação */
CREATE TABLE Vincula (
  Cod_Proj         INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (Cod_Proj, Id_Area_Atuacao),
  FOREIGN KEY  (Cod_Proj)         REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES AREA_ATUACAO(Id_Area_Atuacao)
);

/* Projeto executa uma Linha de pesquisa */
CREATE TABLE Executa (
  Cod_Proj           INT,
  Id_Linha_Pesquisa  INT,

  PRIMARY KEY  (Cod_Proj, Id_Linha_Pesquisa),
  FOREIGN KEY  (Cod_Proj)           REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (Id_Linha_Pesquisa)  REFERENCES LINHA_PESQUISA(Id_Linha_Pesquisa)
);

/* Projeto participa de um Congresso */
CREATE TABLE Participa (
  Id_Proj       INT,
  Id_Congresso  INT,
  Objetivo      text,

  PRIMARY KEY (Id_Proj, Id_Congresso),
  FOREIGN KEY (Id_Proj)       REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY (Id_Congresso)  REFERENCES CONGRESSO(Id_Congresso)
);


/* Instituição tem múltiplos CNAE */
CREATE TABLE CNAE (
  CNPJ_Instituicao  INT,
  CNAE              VARCHAR(20),
  
  PRIMARY KEY  (CNPJ_Instituicao, CNAE),
  FOREIGN KEY  (CNPJ_Instituicao)  REFERENCES  INSTITUICAO(CNPJ)
);

/* Instituição financia Projeto */
CREATE TABLE Financia (
  Cod_Proj  INT,
  CNPJ      INT,

  PRIMARY KEY  (Cod_Proj, CNPJ),
  FOREIGN KEY  (Cod_Proj)  REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (CNPJ)      REFERENCES INSTITUICAO(CNPJ)
);

/* Instituição fomenta Projeto */
CREATE TABLE Fomenta (
  CNPJ      INT,
  Cod_Proj  INT,
  Tipo      VARCHAR(20)  NOT NULL,

  PRIMARY KEY  (CNPJ, Cod_Proj),
  FOREIGN KEY  (CNPJ)      REFERENCES INSTITUICAO(CNPJ),
  FOREIGN KEY  (Cod_Proj)  REFERENCES PROJETO(Cod_Proj)
);


/* Congresso tem edição */
CREATE TABLE Edicao (
  Id_Congresso  INT,
  Cod_edicao    INT,

  PRIMARY KEY  (Id_Congresso, Cod_edicao),
  FOREIGN KEY  (Id_Congresso)  REFERENCES CONGRESSO(Id_Congresso)
);


/* Contas de usuário do sistema */
/* Tipo: 0, 1, 2, 3 -> instituiçao, pesquisador, estudante, colaborador externo */
CREATE TABLE Conta (
  Id_Conta  SERIAL       PRIMARY KEY,
  Tipo      INT          NOT NULL,
  Nome      VARCHAR(15)  NOT NULL,
  Senha     CHAR(8)      NOT NULL,

  UNIQUE (Nome, Senha)
);







/* PROJETO */
/* Cria Projeto */
CREATE OR REPLACE PROCEDURE inserir_projeto(
    p_id_tipo_proj INT,
    p_titulo VARCHAR(75),
    p_data_inicio DATE,
    p_data_final DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO PROJETO (Id_Tipo_Proj, Título, Data_inicio, Data_final)
    VALUES (p_id_tipo_proj, p_titulo, p_data_inicio, p_data_final);
END;
$$;

/* Deleta Projeto */
CREATE OR REPLACE PROCEDURE deletar_projeto(
    p_cod_proj INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM PROJETO WHERE Cod_Proj = p_cod_proj;
EXCEPTION
    WHEN foreign_key_violation THEN
        RAISE NOTICE 'Não é possível deletar o projeto com código % porque ele está vinculado a outras tabelas.', p_cod_proj;
    WHEN others THEN
        RAISE EXCEPTION 'Erro ao deletar projeto: %', SQLERRM;
END;
$$;



/* TIPO DE PROJETO */
/* Cria Tipo de Projeto */
CREATE OR REPLACE PROCEDURE inserir_tipo_projeto(
    p_nome_tipo VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO TIPO_PROJETO (Nome_Tipo)
    VALUES (p_nome_tipo);
    
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Tipo de projeto com ID % já existe.', p_id_tipo_proj;
    WHEN others THEN
        RAISE EXCEPTION 'Erro ao inserir tipo de projeto: %', SQLERRM;
END;
$$;

/* Deleta Tipo de Projeto */
CREATE OR REPLACE PROCEDURE deletar_tipo_projeto(
    p_id_tipo_proj INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM TIPO_PROJETO WHERE Id_Tipo_Proj = p_id_tipo_proj;
EXCEPTION
    WHEN foreign_key_violation THEN
        RAISE NOTICE 'Não é possível deletar o tipo de projeto com ID % porque ele está vinculado a outros projetos.', p_id_tipo_proj;
    WHEN others THEN
        RAISE EXCEPTION 'Erro ao deletar tipo de projeto: %', SQLERRM;
END;
$$;


/* LOCALIDADE */
/* Cria Localidade */
CREATE OR REPLACE PROCEDURE inserir_localidade(
    Cod_postal  INT,
    País        VARCHAR(45),
    UF          CHAR(2),
    Cidade      VARCHAR(45)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO LOCALIDADE (Cod_postal, País, UF, Cidade)
    VALUES (Cod_postal, País, UF, Cidade);
END;
$$;


/* POSSUI */
/* Vincula Projeto a Localidade */
CREATE OR REPLACE PROCEDURE vincular_projeto_localidade(
    p_cod_proj INT,
    p_cod_postal INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO POSSUI (Cod_Proj, Cod_postal)
    VALUES (p_cod_proj, p_cod_postal);
END;
$$;

/* LINHA_PESQUISA */
CREATE OR REPLACE PROCEDURE inserir_linha_pesquisa(
    p_nome_linha VARCHAR(45),
    p_descricao TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO LINHA_PESQUISA (Nome, Descrição)
    VALUES (p_nome_linha, p_descricao);
END;
$$;

/* EXECUTA */
/* Vincula Projeto a Linha de Pesquisa */
CREATE OR REPLACE PROCEDURE vincular_projeto_linha_pesquisa(
    p_cod_proj INT,
    p_id_linha_pesquisa INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO EXECUTA (Cod_Proj, Id_Linha_Pesquisa)
    VALUES (p_cod_proj, p_id_linha_pesquisa);
END;
$$;

/* Area de Atuação */
CREATE OR REPLACE PROCEDURE inserir_area_atuacao(
    p_nome_area VARCHAR(45),
    p_abranencia VARCHAR(12),
    p_descricao TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO AREA_ATUACAO (Nome, Abrangencia, Descrição)
    VALUES (p_nome_area, p_abranencia, p_descricao);
END;
$$;

/* Vincula Projeto a Área de Atuação */
CREATE OR REPLACE PROCEDURE vincular_projeto_area_atuacao(
    p_cod_proj INT,
    p_id_area_atuacao INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO VINCULA (Cod_Proj, Id_Area_Atuacao)
    VALUES (p_cod_proj, p_id_area_atuacao);
END;
$$;

/* CONGRESSO */
CREATE OR REPLACE PROCEDURE inserir_congresso(
    p_nome_congresso VARCHAR(45),
    p_descricao TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO CONGRESSO (Nome, Descricao)
    VALUES (p_nome_congresso, p_descricao);
END;
$$;

/* Vincula Projeto a Congresso */
CREATE OR REPLACE PROCEDURE vincular_projeto_congresso(
    p_cod_proj INT,
    p_id_congresso INT,
    p_objetivo TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO PARTICIPA (Id_Proj, Id_Congresso, Objetivo)
    VALUES (p_cod_proj, p_id_congresso, p_objetivo);
END;
$$;

/* PARTICIPA */
CREATE OR REPLACE PROCEDURE vincular_projeto_congresso(
    p_cod_proj INT,
    p_id_congresso INT,
    p_objetivo TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO PARTICIPA (Id_Proj, Id_Congresso, Objetivo)
    VALUES (p_cod_proj, p_id_congresso, p_objetivo);
END;
$$;

/* INSTITUIÇÃO */
/* FOMENTA */
CREATE OR REPLACE PROCEDURE instituicao_fomenta_projeto(
    p_cnpj INT,
    p_cod_proj INT,
    p_tipo VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO FOMENTA (CNPJ, Cod_Proj, Tipo)
    VALUES (p_cnpj, p_cod_proj, p_tipo);
END;
$$;

/* FINANCIA */
CREATE OR REPLACE PROCEDURE instituicao_financia_projeto(
    p_cnpj INT,
    p_cod_proj INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO FINANCIA (Cod_Proj, CNPJ)
    VALUES (p_cod_proj, p_cnpj);
END;
$$;

/* PATRIMONIO */
CREATE OR REPLACE PROCEDURE inserir_patrimonio(
    p_cod_proj INT,
    p_nome VARCHAR(30),
    p_custo INT,
    p_especificacao TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO PATRIMONIO (Cod_Proj, Nome, Custo, Especificacao)
    VALUES (p_cod_proj, p_nome, p_custo, p_especificacao);
END;
$$;