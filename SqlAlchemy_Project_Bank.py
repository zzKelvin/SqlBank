from select import select
from sqlalchemy import Column, create_engine, func
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente_data"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False)
    endereco = Column(String(20), nullable=False)

    cliente_account = relationship("Contas", back_populates="cliente_data", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"


class Contas(Base):
    __tablename__ = "cliente_account"
    id = Column(Integer)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente_data.id"), primary_key=True)
    saldo = Column(String)

    cliente_data = relationship("Cliente", back_populates="cliente_account")

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia},num={self.num}, " \
               f"id_cliente={self.id_cliente}, saldo={self.saldo})"


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    evelyn = Cliente(
        name='Evelyn Souza',
        cpf='12345678901',
        endereco='Rua 123, Bairro 321',
        cliente_account=[Contas(saldo='1998,2')]
    )

    sandy = Cliente(
        name='Sandy Oliveira',
        cpf='12345678901',
        endereco='Rua 13, Bairro 21',
        cliente_account=[Contas(saldo='32,1')]
    )

    patrick = Cliente(
        name='Patrick Marcio',
        cpf='12345678901',
        endereco='Rua 1234, Bairro 3210',
        cliente_account=[Contas(saldo='9658,58')]
    )

    session.add_all([evelyn, sandy, patrick])
    session.commit()
