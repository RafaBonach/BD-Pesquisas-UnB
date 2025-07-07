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

/* MEMBRO */
/* pesquisa */
CREATE OR REPLACE PROCEDURE vincular_pesquisador_projeto(
    p_cod_proj INT,
    p_id_pesquisador INT,
    p_funcao VARCHAR(12)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO PESQUISA (Cod_Proj, Id_Pesquisador, Funcao)
    VALUES (p_cod_proj, p_id_pesquisador, p_funcao);
END;
$$;

/* realiza */
CREATE OR REPLACE PROCEDURE vincular_estudante_projeto(
    p_cod_proj INT,
    p_id_estudante INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO REALIZA (Cod_Proj, Id_Estudante)
    VALUES (p_cod_proj, p_id_estudante);
END;
$$;