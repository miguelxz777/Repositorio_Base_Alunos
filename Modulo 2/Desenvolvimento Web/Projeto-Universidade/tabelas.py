import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
DATABASE_URL = "postgresql://posgtes:1234@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SESSIONLOCAL = sessionmaker(autocommit=False,bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer,primary_kay=True,index=True,autoincrement=True)
    nome = Column(String(255),nullable=False)
    email = Column(String(255),nullable=False)
    senha_hash = Column(String(255),nullable=False)
    criado_em = Column(DateTime(timezone=True),default=datetime.datetime.now)
    notas = relationship("nota",back_populates="autor")
    usuarios_enderecos = relationship("enderecos",
        secundary_enderecos=usuarios_enderecos_associaçao,
        back_populates="moradores")
    class Nota(Base):
        __tablename__ = "notas"
        id = Column(Integer,primary_kay=True,index=True,autoincrement=True)
        id_usuario = Column(Integer, ForeignKey("usuarios.id"),nullable = False)
        titulo = column(Text)
        criado_em = Column(DateTime(timezone=True),default=datetime.datetime.now)
        autor = relationship("Usuario",back_populates="notas")