from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.repositories.database import Base


class Tutor(Base):
    __tablename__ = 'tutor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    instagram = Column(String)
    identidade_foto = Column(String)
    comprovante_residencia_foto = Column(String)

    gatos = relationship("Gato", back_populates="tutor")
