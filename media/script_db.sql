CREATE TABLE MEMBRO (
  Id_Membro        SERIAL       PRIMARY KEY,
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
  Nome_Tipo     VARCHAR(40)  NOT NULL,

  PRIMARY KEY  (Id_Tipo_Proj) /*Modifiquei a chave primaria*/
);

CREATE TABLE PROJETO (
  Cod_Proj        INT          GENERATED ALWAYS AS IDENTITY,  /*Modifiquei id para serial*/
  Id_Tipo_Proj    INT,
  Título          VARCHAR(200)  NOT NULL,
  Data_final      DATE         NOT NULL,
  Data_inicio     DATE         NOT NULL,
  Resumo          text,
  relatorio       bytea,

  PRIMARY KEY  (Cod_Proj, Id_Tipo_Proj),
  UNIQUE	   (Cod_Proj),
  FOREIGN KEY  (Id_Tipo_Proj)    REFERENCES TIPO_PROJETO(Id_Tipo_Proj) ON DELETE CASCADE
);

CREATE TABLE INSTITUICAO (
  CNPJ                 bigint       PRIMARY KEY,
  Nome                 VARCHAR(50)  NOT NULL,
  Sigla                VARCHAR(10),
  Natureza_Juríd       VARCHAR(60),
  UF                   CHAR(2)      NOT NULL,
  Localidade           VARCHAR(50)  NOT NULL,
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
  Nome               VARCHAR(120)  NOT NULL,
  Descrição          text,

  PRIMARY KEY  (Id_Linha_Pesquisa) /* Transformei id em PK */
);

CREATE TABLE AREA_ATUACAO (
  Id_Area_Atuacao  INT          GENERATED ALWAYS AS IDENTITY, /*Modifiquei id para serial*/
  Abrangencia      VARCHAR(40)  NOT NULL,
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
  Id_Patrimonio  INT          GENERATED ALWAYS AS IDENTITY, /*Modifiquei id para serial*/
  Nome           VARCHAR(30)  NOT NULL,
  Custo          INT          NOT NULL,
  Especificacao  text,

  PRIMARY KEY  (Id_Patrimonio, Cod_Proj),
  FOREIGN KEY  (Cod_Proj)  REFERENCES  PROJETO(Cod_Proj) ON DELETE CASCADE
);


/* Email de membro (multivalorado) */
CREATE TABLE Email (
  Email      VARCHAR(30),
  id_membro  INT,

  PRIMARY KEY (Email, id_membro),
  FOREIGN KEY (id_membro) REFERENCES MEMBRO(id_Membro) ON DELETE CASCADE
);

/* Membro tem origem em Localidade */
CREATE TABLE Origem (
  Cod_postal  INT,
  Id_Membro   INT,

  PRIMARY KEY  (Id_Membro, Cod_postal),
  FOREIGN KEY  (Id_Membro)   REFERENCES MEMBRO(Id_Membro) ON DELETE CASCADE,
  FOREIGN KEY  (Cod_postal)  REFERENCES LOCALIDADE(Cod_postal) ON DELETE CASCADE
);

/* Pesquisador atua em Área de atuação */
CREATE TABLE Atua (
  Id_Pesquisador   INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (Id_Pesquisador, Id_Area_Atuacao),
  FOREIGN KEY  (Id_Pesquisador)   REFERENCES  MEMBRO(Id_Membro) ON DELETE CASCADE,
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES  AREA_ATUACAO(Id_Area_Atuacao) ON DELETE CASCADE
);

/* Pesquisador pesquisa Projeto */
CREATE TABLE Pesquisa (
  Id_Pesquisador  INT,
  Cod_Proj        INT,
  Funcao          VARCHAR(12)  NOT NULL,

  PRIMARY KEY  (Id_Pesquisador, Cod_Proj),
  FOREIGN KEY  (Id_Pesquisador)  REFERENCES MEMBRO(Id_Membro) ON DELETE CASCADE,
  FOREIGN KEY  (Cod_Proj)        REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE
);

/* Estudante realiza Projeto */
CREATE TABLE Realiza (
  Id_Estudante  INT,
  Cod_Proj      INT,

  PRIMARY KEY  (Id_Estudante, Cod_Proj),
  FOREIGN KEY  (Id_Estudante)  REFERENCES MEMBRO(Id_Membro) ON DELETE CASCADE,
  FOREIGN KEY  (Cod_Proj)      REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE
);


/* Projeto possui Localidade */
CREATE TABLE Possui (
  Cod_Proj    INT,
  Cod_postal  INT,

  PRIMARY KEY  (Cod_Proj, Cod_postal),
  FOREIGN KEY  (Cod_Proj)    REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE,
  FOREIGN KEY  (Cod_postal)  REFERENCES LOCALIDADE(Cod_postal) ON DELETE CASCADE
);

/* Projeto vincula Área de atuação */
CREATE TABLE Vincula (
  Cod_Proj         INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (Cod_Proj, Id_Area_Atuacao),
  FOREIGN KEY  (Cod_Proj)         REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE,
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES AREA_ATUACAO(Id_Area_Atuacao) ON DELETE CASCADE
);

/* Projeto executa uma Linha de pesquisa */
CREATE TABLE Executa (
  Cod_Proj           INT,
  Id_Linha_Pesquisa  INT,

  PRIMARY KEY  (Cod_Proj, Id_Linha_Pesquisa),
  FOREIGN KEY  (Cod_Proj)           REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE,
  FOREIGN KEY  (Id_Linha_Pesquisa)  REFERENCES LINHA_PESQUISA(Id_Linha_Pesquisa) ON DELETE CASCADE
);

/* Projeto participa de um Congresso */
CREATE TABLE Participa (
  Id_Proj       INT,
  Id_Congresso  INT,
  Objetivo      text,

  PRIMARY KEY (Id_Proj, Id_Congresso),
  FOREIGN KEY (Id_Proj)       REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE,
  FOREIGN KEY (Id_Congresso)  REFERENCES CONGRESSO(Id_Congresso) ON DELETE CASCADE
);


/* Instituição tem múltiplos CNAE */
CREATE TABLE CNAE (
  CNPJ_Instituicao  bigint,
  CNAE              VARCHAR(20),
  
  PRIMARY KEY  (CNPJ_Instituicao, CNAE),
  FOREIGN KEY  (CNPJ_Instituicao)  REFERENCES  INSTITUICAO(CNPJ) ON DELETE CASCADE
);

/* Instituição financia Projeto */
CREATE TABLE Financia (
  Cod_Proj  INT,
  CNPJ      bigint,

  PRIMARY KEY  (Cod_Proj, CNPJ),
  FOREIGN KEY  (Cod_Proj)  REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE,
  FOREIGN KEY  (CNPJ)      REFERENCES INSTITUICAO(CNPJ) ON DELETE CASCADE
);

/* Instituição fomenta Projeto */
CREATE TABLE Fomenta (
  CNPJ      bigint,
  Cod_Proj  INT,
  Tipo      VARCHAR(20)  NOT NULL,

  PRIMARY KEY  (CNPJ, Cod_Proj),
  FOREIGN KEY  (CNPJ)      REFERENCES INSTITUICAO(CNPJ) ON DELETE CASCADE,
  FOREIGN KEY  (Cod_Proj)  REFERENCES PROJETO(Cod_Proj) ON DELETE CASCADE
);


/* Congresso tem edição */
CREATE TABLE Edicao (
  Id_Congresso  INT,
  Cod_edicao    INT,

  PRIMARY KEY  (Id_Congresso, Cod_edicao),
  FOREIGN KEY  (Id_Congresso)  REFERENCES CONGRESSO(Id_Congresso) ON DELETE CASCADE
);


/* Contas de usuário do sistema */
/* Tipo: 0, 1, 2, 3 -> instituiçao, pesquisador, estudante, colaborador externo */
CREATE TABLE Conta (
  Id_Conta     SERIAL       PRIMARY KEY,
  Tipo         INT          NOT NULL,
  Nome         VARCHAR(15)  NOT NULL,
  Senha        CHAR(6)      NOT NULL,
  Id_Entidade  INT,

  UNIQUE (Nome, Senha, Id_Entidade)
);