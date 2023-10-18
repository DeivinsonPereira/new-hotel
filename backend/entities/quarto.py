from sqlalchemy import Column, Integer, String, Enum, Text, Float
from sqlalchemy.orm import relationship
from backend.repositories.database import Base


class Quarto(Base):
    __tablename__ = 'quarto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    tamanho = Column(String)
    tipo_quarto = Column(Enum("Premium", "Gatil Social"))
    descricao = Column(Text)
    valor_cliente = Column(Float)
    valor_resgate = Column(Float)
    imagem_quarto = Column(String)
    disponivel = Column(Enum("Sim", "Não"))

    reservas = relationship("Reserva", back_populates="quarto")
