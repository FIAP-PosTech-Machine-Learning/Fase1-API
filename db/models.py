from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class Comercio(Base):
    __tablename__ = 'comercio'

    id = Column(Integer, primary_key=True, index=True)
    control = Column(String, index=True)
    produto = Column(String, index=True)

    anos = relationship("ComercioAno", back_populates="comercio")


class ComercioAno(Base):
    __tablename__ = 'comercio_ano'

    id = Column(Integer, primary_key=True, index=True)
    comercio_id = Column(Integer, ForeignKey('comercio.id'))
    ano = Column(String, index=True)
    valor = Column(Integer)

    comercio = relationship("Comercio", back_populates="anos")


class ExpVinho(Base):
    __tablename__ = 'exp_vinho'

    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, index=True)

    anos = relationship("ExpVinhoAno", back_populates="exp_vinho")


class ExpVinhoAno(Base):
    __tablename__ = 'exp_vinho_ano'

    id = Column(Integer, primary_key=True, index=True)
    exp_vinho_id = Column(Integer, ForeignKey('exp_vinho.id'))
    ano = Column(String, index=True)
    valor = Column(Integer)

    exp_vinho = relationship("ExpVinho", back_populates="anos")


class ImpVinhos(Base):
    __tablename__ = 'imp_vinhos'

    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, index=True)

    anos = relationship("ImpVinhosAno", back_populates="imp_vinhos")


class ImpVinhosAno(Base):
    __tablename__ = 'imp_vinhos_ano'

    id = Column(Integer, primary_key=True, index=True)
    imp_vinhos_id = Column(Integer, ForeignKey('imp_vinhos.id'))
    ano = Column(String, index=True)
    valor = Column(Integer)

    imp_vinhos = relationship("ImpVinhos", back_populates="anos")


class ProcessaViniferas(Base):
    __tablename__ = 'processa_viniferas'

    id = Column(Integer, primary_key=True, index=True)
    control = Column(String, index=True)
    cultivar = Column(String, index=True)

    anos = relationship("ProcessaViniferasAno", back_populates="processa_vinifera")


class ProcessaViniferasAno(Base):
    __tablename__ = 'processa_viniferas_ano'

    id = Column(Integer, primary_key=True, index=True)
    processa_vinifera_id = Column(Integer, ForeignKey('processa_viniferas.id'))
    ano = Column(String, index=True)
    valor = Column(Integer)

    processa_vinifera = relationship("ProcessaViniferas", back_populates="anos")


class Producao(Base):
    __tablename__ = 'producao'

    id = Column(Integer, primary_key=True, index=True)
    control = Column(String, index=True)
    produto = Column(String, index=True)

    anos = relationship("ProducaoAno", back_populates="producao")


class ProducaoAno(Base):
    __tablename__ = 'producao_ano'

    id = Column(Integer, primary_key=True, index=True)
    producao_id = Column(Integer, ForeignKey('producao.id'))
    ano = Column(String, index=True)
    valor = Column(Integer)

    producao = relationship("Producao", back_populates="anos")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)