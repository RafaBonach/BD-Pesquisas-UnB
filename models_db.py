"""
    Esse arquivo define os modelos de dados para o banco de dados de pesquisas.
    Ele utiliza SQLAlchemy para definir as tabelas e suas relações.
"""
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from backend_db import Base, SessionLocal

class BaseModel:
    @classmethod
    def create (cls, **kwargs):
        db = SessionLocal()
        try:
            instance = cls(**kwargs)
            db.add(instance)
            db.commit()
            db.refresh(instance)
            return instance
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    def update(self, **kwargs):
        db = SessionLocal()
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.add(self)
            db.commit()
            db.refresh(self)
            return self
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    def delete(self):
        db = SessionLocal()
        try:
            db.delete(self)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    @classmethod
    def get_all(cls):
        db = SessionLocal()
        try:
            return db.query(cls).all()
        except Exception as e:
            raise e
        finally:
            db.close()
    
    @classmethod
    def get_by_id(cls, id):
        db = SessionLocal()
        try:
            return db.query(cls).filter(cls.id == id).first()
        except Exception as e:
            raise e
        finally:
            db.close()

class Membro(Base):
    __tablename__ = 'membros'

    id_membro = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), index=True, nullable=False)
    titulacao = Column(String(15), index=True, nullable=False)
    descricao = Column(Text)
    departamento = Column(String(30))
    matricula = Column(Integer, unique=True, nullable=False)
    Curso_estudante = Column(String)

class TipoProjeto(Base, BaseModel):
    __tablename__ = 'tipo_projeto'

    id_tipo_proj = Column(Integer, primary_key=True)
    nome_tipo = Column(String(20), nullable=False)

class Projeto(Base, BaseModel):
    __tablename__ = 'projeto'

    cod_proj = Column(Integer, primary_key=True)
    id_tipo_proj = Column(Integer, ForeignKey('tipo_projeto.id_tipo_proj'), primary_key=True)
    titulo = Column(String(75), nullable=False)
    data_final = Column(Date, nullable=False)
    data_inicio = Column(Date, nullable=False)
    resumo = Column(Text)

class Instituicao(Base, BaseModel):
    __tablename__ = 'instituicao'

    cnpj = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    sigla = Column(String(10))
    natureza_jurid = Column(String(20))
    uf = Column(String(2), nullable=False)
    localidade = Column(String(30), nullable=False)
    recursos_investidos = Column(Integer)
    descricao = Column(Text)

class Congresso(Base, BaseModel):
    __tablename__ = 'congresso'

    id_congresso = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)
    descricao = Column(Text)

class LinhaPesquisa(Base, BaseModel):
    __tablename__ = 'linha_pesquisa'

    id_linha_pesquisa = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)
    descricao = Column(Text)

class AreaAtuacao(Base, BaseModel):
    __tablename__ = 'area_atuacao'

    id_area_atuacao = Column(Integer, primary_key=True)
    abrangencia = Column(String(12), nullable=False)
    nome = Column(String(45), nullable=False)
    descricao = Column(Text)

class Localidade(Base, BaseModel):
    __tablename__ = 'localidade'

    cod_postal = Column(Integer, primary_key=True)
    pais = Column(String(45), nullable=False)
    uf = Column(String(2), nullable=False)
    cidade = Column(String(45), nullable=False)

class Patrimonio(Base, BaseModel):
    __tablename__ = 'patrimonio'

    id_patrimonio = Column(Integer, primary_key=True)
    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    nome = Column(String(30), nullable=False)
    custo = Column(Integer, nullable=False)
    especificacao = Column(Text)

class Email(Base, BaseModel):
    __tablename__ = 'email'

    email = Column(String(30), primary_key=True)
    id_membro = Column(Integer, ForeignKey('membro.id_membro'), primary_key=True)

class Origem(Base, BaseModel):
    __tablename__ = 'origem'

    id_membro = Column(Integer, ForeignKey('membro.id_membro'), primary_key=True)
    cod_postal = Column(Integer, ForeignKey('localidade.cod_postal'), primary_key=True)

class Atua(Base, BaseModel):
    __tablename__ = 'atua'

    id_pesquisador = Column(Integer, ForeignKey('membro.id_membro'), primary_key=True)
    id_area_atuacao = Column(Integer, ForeignKey('area_atuacao.id_area_atuacao'), primary_key=True)

class Pesquisa(Base, BaseModel):
    __tablename__ = 'pesquisa'

    id_pesquisador = Column(Integer, ForeignKey('membro.id_membro'), primary_key=True)
    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    funcao = Column(String(12), nullable=False)

class Realiza(Base, BaseModel):
    __tablename__ = 'realiza'

    id_estudante = Column(Integer, ForeignKey('membro.id_membro'), primary_key=True)
    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)

class Possui(Base, BaseModel):
    __tablename__ = 'possui'

    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    cod_postal = Column(Integer, ForeignKey('localidade.cod_postal'), primary_key=True)

class Vincula(Base, BaseModel):
    __tablename__ = 'vincula'

    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    id_area_atuacao = Column(Integer, ForeignKey('area_atuacao.id_area_atuacao'), primary_key=True)

class Executa(Base, BaseModel):
    __tablename__ = 'executa'

    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    id_linha_pesquisa = Column(Integer, ForeignKey('linha_pesquisa.id_linha_pesquisa'), primary_key=True)

class Participa(Base, BaseModel):
    __tablename__ = 'participa'

    id_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    id_congresso = Column(Integer, ForeignKey('congresso.id_congresso'), primary_key=True)
    objetivo = Column(Text)

class CNAE(Base, BaseModel):
    __tablename__ = 'cnae'

    cnpj_instituicao = Column(Integer, ForeignKey('instituicao.cnpj'), primary_key=True)
    cnae = Column(String(20), primary_key=True)

class Financia(Base, BaseModel):
    __tablename__ = 'financia'

    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    cnpj = Column(Integer, ForeignKey('instituicao.cnpj'), primary_key=True)

class Fomenta(Base, BaseModel):
    __tablename__ = 'fomenta'

    cnpj = Column(Integer, ForeignKey('instituicao.cnpj'), primary_key=True)
    cod_proj = Column(Integer, ForeignKey('projeto.cod_proj'), primary_key=True)
    tipo = Column(String(20), nullable=False)

class Edicao(Base, BaseModel):
    __tablename__ = 'edicao'

    id_congresso = Column(Integer, ForeignKey('congresso.id_congresso'), primary_key=True)
    cod_edicao = Column(Integer, primary_key=True)
