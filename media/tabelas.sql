CREATE TABLE MEMBRO (
  Id_Membro        INT          PRIMARY KEY,
  Nome             VARCHAR(45)  NOT NULL,
  Titulação        VARCHAR(15)  NOT NULL,
  Descrição        text,

  Departamento     VARCHAR(30),

  Matrícula        INT,
  Curso_estudante  VARCHAR(30),

  UNIQUE (Matrícula)
);

/* Projeto tem um tipo */
CREATE TABLE TIPO_PROJETO (
  Id_Tipo_Proj  INT          PRIMARY KEY,
  Nome_Tipo     VARCHAR(20)  NOT NULL
);

CREATE TABLE PROJETO (
  Cod_Proj        INT unique,
  Id_Tipo_Proj    INT unique,
  Título          VARCHAR(75)  NOT NULL,
  Data_final      DATE         NOT NULL,
  Data_inicio     DATE         NOT NULL,
  Id_Coordenador  INT          NOT NULL,
  Resumo          text,

  PRIMARY KEY  (Cod_Proj, Id_Tipo_Proj),
  FOREIGN KEY  (Id_Tipo_Proj)    REFERENCES TIPO_PROJETO(Id_Tipo_Proj),
  FOREIGN KEY  (Id_Coordenador)  REFERENCES MEMBRO(Id_Membro)
);

CREATE TABLE INSTITUICAO (
  CNPJ                 INT          PRIMARY KEY,
  CNAE                 VARCHAR(20)  NOT NULL,
  Nome                 VARCHAR(40)  NOT NULL,
  Sigla                VARCHAR(10),
  Natureza_Juríd       VARCHAR(20),
  UF                   CHAR(2)      NOT NULL,
  Localidade           VARCHAR(30)  NOT NULL,
  Recursos_Investidos  INT,
  Descrição            text
);

CREATE TABLE CONGRESSO (
  Id_Congresso  INT PRIMARY KEY,
  Nome          VARCHAR(45) NOT NULL,
  Descricao     text
);

CREATE TABLE EDICAO (
  Id_Congresso  INT,
  Cod_edicao    INT,
  Data_inicio   DATE  NOT NULL,
  Data_fim      DATE,
  Descricao     text,

  PRIMARY KEY (Id_Congresso, Cod_edicao),
  FOREIGN KEY (Id_Congresso)  REFERENCES CONGRESSO(Id_Congresso)
);

CREATE TABLE LINHA_PESQUISA (
  Id_Linha_Pesquisa  INT PRIMARY  KEY,
  Nome               VARCHAR(45)  NOT NULL,
  Descrição          text
);

CREATE TABLE AREA_ATUACAO (
  Id_Area_Atuacao  INT          PRIMARY KEY,
  Abrangencia      VARCHAR(12)  NOT NULL,
  Nome             VARCHAR(45)  NOT NULL,
  Descrição        text
);

CREATE TABLE LOCAL (
  CEP     INT          PRIMARY KEY,
  País    VARCHAR(45)  NOT NULL,
  UF      CHAR(2)      NOT NULL,
  Cidade  VARCHAR(45)  NOT NULL
);



/* Email de membro (multivalorado) */
CREATE TABLE Email (
  Email      VARCHAR(30),
  id_membro  INT,

  PRIMARY KEY (Email, id_membro),
  FOREIGN KEY (id_membro) REFERENCES MEMBRO(id_Membro)
);

/* Pesquisador orienta Estudante */
CREATE TABLE Orienta (
  id_Pesquisador  INT,
  id_Estudante    INT,

  PRIMARY KEY (id_Pesquisador, id_Estudante),
  FOREIGN KEY (id_Pesquisador)  REFERENCES  MEMBRO(id_Membro),
  FOREIGN KEY (id_Estudante)    REFERENCES  MEMBRO(id_Membro)
);

/* Pesquisador co-coordena Projeto */
CREATE TABLE Co_coordena (
  Id_Pesquisador  INT,
  Cod_Proj        INT,

  PRIMARY KEY  (Id_Pesquisador, Cod_Proj),
  FOREIGN KEY  (Id_Pesquisador)  REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (Cod_Proj)        REFERENCES PROJETO(Cod_Proj)
);

/* Pesquisador pesquisa Projeto */
CREATE TABLE Pesquisa (
  Id_Pesquisador  INT,
  Cod_Proj        INT,

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


/* Membro tem origem em Local */
CREATE TABLE Origem (
  CEP        INT,
  Id_Membro  INT,

  PRIMARY KEY  (Id_Membro, CEP),
  FOREIGN KEY  (Id_Membro)  REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (CEP)        REFERENCES LOCAL(CEP)
);

/* Membro atua em Área de atuação */
CREATE TABLE Trabalha (
  id_Membro        INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (id_Membro, Id_Area_Atuacao),
  FOREIGN KEY  (id_Membro)        REFERENCES MEMBRO(Id_Membro),
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES AREA_ATUACAO(Id_Area_Atuacao)
);


/* Projeto possui Local */
CREATE TABLE Possui (
  Cod_Proj  INT,
  CEP       INT,

  PRIMARY KEY  (Cod_Proj, CEP),
  FOREIGN KEY  (Cod_Proj)  REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (CEP)       REFERENCES LOCAL(CEP)
);

/* Projeto vincula Área de atuação */
CREATE TABLE Vincula (
  Cod_Proj         INT,
  Id_Area_Atuacao  INT,

  PRIMARY KEY  (Cod_Proj, Id_Area_Atuacao),
  FOREIGN KEY  (Cod_Proj)         REFERENCES PROJETO(Cod_Proj),
  FOREIGN KEY  (Id_Area_Atuacao)  REFERENCES AREA_ATUACAO(Id_Area_Atuacao)
);


/* Projeto atua em Linha de pesquisa */
CREATE TABLE Atua (
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
