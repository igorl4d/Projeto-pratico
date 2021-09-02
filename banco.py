from sqlalchemy import create_engine, Column, Integer, Numeric, String, DateTime, text
from sqlalchemy.sql import select
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from datetime import date
from sqlalchemy.engine import result
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import Date, DateTime

# Variáveis para inicializar Banco de dados
engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Modelo do banco de dados


class Usuarios(Base):

    __tablename__ = "Usuarios"

    Nome = Column(String(50))
    Sobrenome = Column(String(50))
    id = Column(Integer, primary_key=True)
    id_telegram = Column(Integer)


# Procura se já existe um banco de dados
def init():

    if not database_exists(engine.url):
        Base.metadata.create_all(engine)
    else:
        return


# Retorna todas as informações dos usuarios
def query_all():

    con = engine.connect()
    query = select(Usuarios)
    rows = con.execute(query)

    list_dict = [dict((key, value)
                      for key, value in row.items()) for row in rows]

    return list_dict

# Insere informações nos bancos de dados


def inserir(usuario_nome, usuario_sobrenome, id_telegram):

    inserir_usuario = Usuarios(
        Nome=usuario_nome, Sobrenome=usuario_sobrenome, id_telegram=id_telegram)
    session.add(inserir_usuario)
    session.commit()

    return
