from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from backend.repositories.database import Base


class Gato(Base):
    __tablename__ = 'gato'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    tipo = Column(Enum("Cliente", "Resgatado"))
    idade = Column(Integer)
    sexo = Column(Enum("Macho", "Fêmea"))
    raca = Column(String)
    castrado = Column(Enum("sim", "não"))
    vacinado = Column(Enum("sim", "não"))
    vermifugado = Column(Enum("sim", "não"))
    antiparasitado = Column(Enum("sim", "não"))
    historico_saude = Column(Text)
    comportamento = Column(Text)
    uso_medicacao = Column(Enum("sim", "não"))
    tipo_medicacao = Column(String)
    criacao = Column(Enum("indoor", "outdoor"))
    exame_fiv_felv = Column(Enum("sim", "não"))
    foto_gato = Column(String)
    foto_exame = Column(String)
    foto_carteira = Column(String)
    tutor_id = Column(Integer, ForeignKey('tutor.id'))

    tutor = relationship("Tutor", back_populates="gatos")

    def __init__(self, nome, tipo, idade, sexo, raca, castrado, vacinado, vermifugado, antiparasitado, historico_saude,
                 comportamento, uso_medicacao, tipo_medicacao, criacao, exame_fiv_felv, foto_gato, foto_exame,
                 foto_carteira, tutor_id):

        self.nome = nome
        self.tipo = tipo
        self.idade = idade
        self.sexo = sexo
        self.raca = raca
        self.castrado = castrado
        self.vacinado = vacinado
        self.vermifugado = vermifugado
        self.antiparasitado = antiparasitado
        self.historico_saude = historico_saude
        self.comportamento = comportamento
        self.uso_medicacao = uso_medicacao
        self.tipo_medicacao = tipo_medicacao if self.uso_medicacao == "sim" else "não usa medicamento"
        self.criacao = criacao
        self.exame_fiv_felv = exame_fiv_felv
        self.foto_gato = foto_gato
        self.foto_exame = foto_exame
        self.foto_carteira = foto_carteira
        self.tutor_id = tutor_id
