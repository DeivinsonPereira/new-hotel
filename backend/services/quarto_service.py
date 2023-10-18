from backend.entities.quarto import Quarto


class QuartoService:
    def __init__(self, session):
        self.session = session

    def criar_quarto(self, nome, tamanho, tipo_quarto, descricao, valor_cliente, valor_resgate,
                     imagem_quarto):

        quarto = Quarto(nome=nome, tamanho=tamanho, tipo_quarto=tipo_quarto, descricao=descricao,
                        valor_cliente=valor_cliente, valor_resgate=valor_resgate,
                        imagem_quarto=imagem_quarto)

        self.session.add(quarto)
        self.session.commit()
        return quarto

    def atualizar_quarto(self, quarto_id, nome, tamanho, tipo_quarto, descricao, valor_cliente, valor_resgate,
                         imagem_quarto):
        try:
            quarto = self.session.query(Quarto).filter_by(id=quarto_id).first()

            if quarto:
                quarto.nome = nome
                quarto.tamanho = tamanho
                quarto.tipo_quarto = tipo_quarto
                quarto.descricao = descricao
                quarto.valor_cliente = valor_cliente
                quarto.valor_resgate = valor_resgate
                quarto.imagem_quarto = imagem_quarto


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
