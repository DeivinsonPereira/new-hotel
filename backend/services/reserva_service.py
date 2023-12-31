from backend.entities.reserva import Reserva
from backend.entities.quarto import Quarto


class ReservaService:
    def __init__(self, session):
        self.session = session

    def criar_reserva(self, tutor_id, quarto_id, gatos_id, data_checkin, data_checkout, preco_total,
                      status_reserva, observacoes, data_criacao):

        reserva = Reserva(tutor_id=tutor_id, quarto_id=quarto_id, gatos_id=gatos_id, data_checkin=data_checkin,
                          data_checkout=data_checkout, preco_total=preco_total, status_reserva=status_reserva,
                          observacoes=observacoes, data_criacao=data_criacao)

        self.session.add(reserva)
        self.session.commit()
        return reserva

    def atualizar_reserva(self, reserva_id, tutor_id, quarto_id, gatos_id, data_checkin, data_checkout, preco_total,
                          status_reserva, observacoes):
        try:
            reserva = self.session.query(Reserva).filter_by(id=reserva_id).first()

            if reserva:
                reserva.reserva_id = reserva_id
                reserva.tutor_id = tutor_id
                reserva.quarto_id = quarto_id
                reserva.gatos_id = gatos_id
                reserva.data_checkin = data_checkin
                reserva.data_checkout = data_checkout
                reserva.preco_total = preco_total
                reserva.status_reserva = status_reserva
                reserva.observacoes = observacoes

                self.session.commit()
                return "Reserva atualizada com sucesso."
            else:
                return "Reserva não encontrada."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao atualizar o gato: {str(e)}"

    def deletar_reserva(self, reserva_id):
        try:
            reserva = self.session.query(Reserva).filter_by(id=reserva_id).first()

            if reserva:
                self.session.delete(reserva)
                self.session.commit()
                return "Reserva deletada com sucesso."
            else:
                return "Reserva não encontrada."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao deletar a reserva: {str(e)}"

    def buscar_reservas(self, checkin, checkout):
        if checkin >= checkout:
            print("A data de check-in deve ser anterior à data de check-out.")
        else:
            # Consulta para buscar quartos que não têm reservas dentro do intervalo de datas
            quartos_disponiveis = self.session.query(Quarto).filter(
                ~Quarto.reservas.any(
                    (Reserva.data_checkin <= checkout) &
                    (Reserva.data_checkout >= checkin)
                )
            ).all()

            if not quartos_disponiveis:
                print("Não há quartos disponíveis para as datas selecionadas.")
            else:
                # Agora você tem a lista de quartos disponíveis dentro do intervalo de datas
                for quarto in quartos_disponiveis:
                    print(f"Quarto ID: {quarto.id}")
                    # Acesse outras informações do quarto, se necessário

        # Não se esqueça de fechar a sessão quando terminar
        self.session.close()
