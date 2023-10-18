from sqlalchemy import Column, Integer, Float, Enum, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.repositories.database import Base
from pytz import timezone


class Reserva(Base):

    tz = timezone('America/Sao_Paulo')

    __tablename__ = 'reserva'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tutor_id = Column(Integer, ForeignKey('tutor.id'), nullable=False)
    quarto_id = Column(Integer, ForeignKey('quarto.id'), nullable=False)
    gatos_id = Column(Integer, ForeignKey('gato.id'), nullable=False)
    data_checkin = Column(DateTime, nullable=False)
    data_checkout = Column(DateTime, nullable=False)
    preco_total = Column(Float)
    status_reserva = Column(Enum("pendente", "confirmada", "cancelada"))
    observacoes = Column(Text)
    data_criacao = Column(DateTime(timezone=True), default=func.now(tz))

    quarto = relationship("Quarto", back_populates="reservas")
    tutor = relationship("Tutor", back_populates="reservas")
    gatos = relationship("Gato", back_populates="reserva")
