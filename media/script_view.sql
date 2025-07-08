-- View que mostra os detalhes de um projeto com dados agrupados
CREATE OR REPLACE VIEW vw_detalhes_projetos_agrupada AS
SELECT
  p.Cod_Proj,
  p.Título,
  p.Data_inicio,
  p.Data_final,
  p.Resumo,
  tp.Nome_Tipo AS Tipo_Projeto,

  -- Lista de pesquisadores
  STRING_AGG(DISTINCT pesq.Nome, ', ') AS Pesquisadores,

  -- Lista de estudantes
  STRING_AGG(DISTINCT est.Nome, ', ') AS Estudantes,

  -- Lista de áreas de atuação
  STRING_AGG(DISTINCT aa.Nome, ', ') AS Areas_Atuacao,

  -- Lista de congressos
  STRING_AGG(DISTINCT cg.Nome, ', ') AS Congressos,

  -- Lista de instituições financiadoras
  STRING_AGG(DISTINCT instf.Nome, ', ') AS Instituicoes_Financiadoras,

  -- Lista de instituições fomentadoras
  STRING_AGG(DISTINCT instfo.Nome, ', ') AS Instituicoes_Fomentadoras,

  -- Lista de patrimônios com nomes + custo
  STRING_AGG(DISTINCT pat.Nome || ' (R$' || pat.Custo || ')', ', ') AS Patrimonios,

  -- Localidades (pais, UF, cidade)
  STRING_AGG(DISTINCT l.País || ' - ' || l.UF || ' - ' || l.Cidade, ', ') AS Localizacoes,

  -- Linha de pesquisa
  STRING_AGG(DISTINCT lp.Nome, ', ') AS Linhas_Pesquisa

FROM PROJETO p
LEFT JOIN TIPO_PROJETO tp ON p.Id_Tipo_Proj = tp.Id_Tipo_Proj

LEFT JOIN PESQUISA pe ON p.Cod_Proj = pe.Cod_Proj
LEFT JOIN MEMBRO pesq ON pe.Id_Pesquisador = pesq.Id_Membro

LEFT JOIN REALIZA re ON p.Cod_Proj = re.Cod_Proj
LEFT JOIN MEMBRO est ON re.Id_Estudante = est.Id_Membro

LEFT JOIN VINCULA v ON p.Cod_Proj = v.Cod_Proj
LEFT JOIN AREA_ATUACAO aa ON v.Id_Area_Atuacao = aa.Id_Area_Atuacao

LEFT JOIN PARTICIPA part ON p.Cod_Proj = part.Id_Proj
LEFT JOIN CONGRESSO cg ON part.Id_Congresso = cg.Id_Congresso

LEFT JOIN FINANCIA fin ON p.Cod_Proj = fin.Cod_Proj
LEFT JOIN INSTITUICAO instf ON fin.CNPJ = instf.CNPJ

LEFT JOIN FOMENTA fom ON p.Cod_Proj = fom.Cod_Proj
LEFT JOIN INSTITUICAO instfo ON fom.CNPJ = instfo.CNPJ

LEFT JOIN PATRIMONIO pat ON p.Cod_Proj = pat.Cod_Proj

LEFT JOIN POSSUI pos ON p.Cod_Proj = pos.Cod_Proj
LEFT JOIN LOCALIDADE l ON pos.Cod_postal = l.Cod_postal

LEFT JOIN EXECUTA ex ON p.Cod_Proj = ex.Cod_Proj
LEFT JOIN LINHA_PESQUISA lp ON ex.Id_Linha_Pesquisa = lp.Id_Linha_Pesquisa

GROUP BY
  p.Cod_Proj,
  p.Título,
  p.Data_inicio,
  p.Data_final,
  p.Resumo,
  tp.Nome_Tipo;



-- View que mostra os detalhes de um membro com dados agrupados
CREATE OR REPLACE VIEW vw_detalhes_membros_agrupada AS
SELECT
  m.Id_Membro,
  m.Nome,
  m.Titulação,
  m.Descrição,
  m.Departamento,
  m.Matrícula,
  m.Curso_estudante,

  -- Localidades (país - UF - cidade)
  STRING_AGG(DISTINCT l.País || ' - ' || l.UF || ' - ' || l.Cidade, ', ') AS Localidades,

  -- Emails
  STRING_AGG(DISTINCT e.Email, ', ') AS Emails,

  -- Áreas de atuação
  STRING_AGG(DISTINCT a.Nome, ', ') AS Areas_Atuacao,

  -- Projetos pesquisados
  STRING_AGG(DISTINCT ppesq.Título, ', ') AS Projetos_Pesquisados,

  -- Projetos realizados
  STRING_AGG(DISTINCT prel.Título, ', ') AS Projetos_Realizados

FROM MEMBRO m

-- Localidades
LEFT JOIN Origem o ON m.Id_Membro = o.Id_Membro
LEFT JOIN LOCALIDADE l ON o.Cod_postal = l.Cod_postal

-- Emails
LEFT JOIN Email e ON m.Id_Membro = e.id_membro

-- Áreas de atuação
LEFT JOIN Atua atua ON m.Id_Membro = atua.Id_Pesquisador
LEFT JOIN AREA_ATUACAO a ON atua.Id_Area_Atuacao = a.Id_Area_Atuacao

-- Projetos pesquisados
LEFT JOIN Pesquisa pesq ON m.Id_Membro = pesq.Id_Pesquisador
LEFT JOIN PROJETO ppesq ON pesq.Cod_Proj = ppesq.Cod_Proj

-- Projetos realizados
LEFT JOIN Realiza rel ON m.Id_Membro = rel.Id_Estudante
LEFT JOIN PROJETO prel ON rel.Cod_Proj = prel.Cod_Proj

GROUP BY
  m.Id_Membro,
  m.Nome,
  m.Titulação,
  m.Descrição,
  m.Departamento,
  m.Matrícula,
  m.Curso_estudante;




-- View que mostra os detalhes de uma instituição com dados agrupados
CREATE OR REPLACE VIEW vw_detalhes_instituicoes_agrupada AS
SELECT
  i.CNPJ,
  i.Nome,
  i.Sigla,
  i.Natureza_Juríd,
  i.UF,
  i.Localidade,
  i.Recursos_Investidos,
  i.Descrição,

  -- CNAEs
  STRING_AGG(DISTINCT c.CNAE, ', ') AS CNAEs,

  -- Projetos fomentados com tipo (ex: "1 - Projeto X (Bolsas)")
  STRING_AGG(DISTINCT f.Cod_Proj || ' - ' || pf.Título || ' (' || f.Tipo || ')', ', ') AS Projetos_Fomentados,

  -- Projetos financiados (ex: "2 - Projeto Y")
  STRING_AGG(DISTINCT fi.Cod_Proj || ' - ' || pfi.Título, ', ') AS Projetos_Financiados

FROM INSTITUICAO i

-- CNAEs
LEFT JOIN CNAE c ON i.CNPJ = c.CNPJ_Instituicao

-- Projetos fomentados
LEFT JOIN FOMENTA f ON i.CNPJ = f.CNPJ
LEFT JOIN PROJETO pf ON f.Cod_Proj = pf.Cod_Proj

-- Projetos financiados
LEFT JOIN FINANCIA fi ON i.CNPJ = fi.CNPJ
LEFT JOIN PROJETO pfi ON fi.Cod_Proj = pfi.Cod_Proj

GROUP BY
  i.CNPJ,
  i.Nome,
  i.Sigla,
  i.Natureza_Juríd,
  i.UF,
  i.Localidade,
  i.Recursos_Investidos,
  i.Descrição;