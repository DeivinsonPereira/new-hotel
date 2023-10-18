from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.repositories.database import Base


class Orcamento(Base):
    __tablename__ = 'orcamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reserva_id = Column(Integer, ForeignKey('reserva.id'), nullable=False)
    reserva_quarto_id = Column(Integer, nullable=False)
    reserva_tutor_id = Column(Integer, nullable=False)
    valor_diario = Column(Float, nullable=False)

    # Crie o relacionamento com a classe Reserva
    reserva = relationship("Reserva", back_populates="orcamento")

    def __init__(self, reserva, reserva_quarto_id, reserva_tutor_id):
        self.reserva = reserva
        self.reserva_quarto_id = reserva_quarto_id
        self.reserva_tutor_id = reserva_tutor_id
        # Calcule o valor_diario com base no tipo do gato na reserva
        if reserva.gatos[0].tipo == "Cliente":
            self.valor_diario = reserva.quarto.valor_cliente
        elif reserva.gatos[0].tipo == "Resgate":
            self.valor_diario = reserva.quarto.valor_resgate
