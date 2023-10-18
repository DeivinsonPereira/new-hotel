from backend.entities.quarto import Quarto


class QuartoService:
    def __init__(self, session):
        self.session = session

    def criar_quarto(self, nome, tamanho, tipo_quarto, descricao, valor_cliente, valor_resgate,
                     imagem_quarto, disponivel):

        quarto = Quarto(nome=nome, tamanho=tamanho, tipo_quarto=tipo_quarto, descricao=descricao,
                        valor_cliente=valor_cliente, valor_resgate=valor_resgate,
                        imagem_quarto=imagem_quarto, disponivel=disponivel)

        self.session.add(quarto)
        self.session.commit()
        return quarto

    def atualizar_quarto(self, quarto_id, nome, tamanho, tipo_quarto, descricao, valor_cliente, valor_resgate,
                       imagem_quarto, disponivel):
        try:
            gato = self.session.query(Quarto).filter_by(id=quarto_id).first()

            if gato:
                gato.nome = nome
                gato.tamanho = tamanho
                gato.tipo_quarto = tipo_quarto
                gato.descricao = descricao
                gato.valor_cliente = valor_cliente
                gato.valor_resgate = valor_resgate
                gato.imagem_quarto = imagem_quarto
                gato.disponivel = disponivel

                self.session.commit()
                return "Quarto atualizado com sucesso."
            else:
                return "Quarto não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao atualizar o gato: {str(e)}"

    def deletar_quarto(self, quarto_id):
        try:
            quarto = self.session.query(Quarto).filter_by(id=quarto_id).first()

            if quarto:
                self.session.delete(quarto)
                self.session.commit()
                return "Quarto deletado com sucesso."
            else:
                return "Gato não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao deletar o quarto: {str(e)}"
