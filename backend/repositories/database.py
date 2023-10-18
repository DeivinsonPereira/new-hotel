from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
import os

# Determine o caminho relativo para o arquivo de banco de dados
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'hotel_pet_bigodinhos.db')

# Crie a conexão com o banco de dados usando o caminho relativo
engine = create_engine(f'sqlite:///{db_path}')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Crie uma função para criar uma sessão do SQLAlchemy
def criar_sessao():
    session = sessionmaker(bind=engine)
    return session()


# Função para criar o banco de dados e as tabelas
def criar_banco_dados():
    try:
        from backend.entities.tutor import Base
        from backend.entities.gato import Base
        from backend.entities.quarto import Base
        from backend.entities.reserva import Base
        from backend.entities.orcamento import Base

        reserva_gato_association = Table(
            'reserva_gato_association',
            Base.metadata,
            Column('reserva_id', Integer, ForeignKey('reserva.id')),
            Column('gato_id', Integer, ForeignKey('gato.id'))
        )

        Base.metadata.create_all(engine)
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print("Erro ao criar tabelas:", str(e))


if __name__ == "__main__":
    criar_banco_dados()
