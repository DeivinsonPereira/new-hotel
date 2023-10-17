from backend.entities.gato import Gato


class GatoService:
    def __init__(self, session):
        self.session = session

    def criar_gato(self, nome, tipo, idade, sexo, raca, castrado, vacinado, vermifugado, antiparasitado, historico_saude,
                   comportamento, uso_medicacao, tipo_medicacao, criacao, exame_fiv_felv, foto_gato, foto_exame,
                   foto_carteira, tutor_id):

        gato = Gato(nome=nome, tipo=tipo, idade=idade, sexo=sexo, raca=raca, castrado=castrado,
                    vacinado=vacinado, vermifugado=vermifugado, antiparasitado=antiparasitado,
                    historico_saude=historico_saude, comportamento=comportamento, uso_medicacao=uso_medicacao,
                    tipo_medicacao=tipo_medicacao, criacao=criacao, exame_fiv_felv=exame_fiv_felv, foto_gato=foto_gato,
                    foto_exame=foto_exame, foto_carteira=foto_carteira, tutor_id=tutor_id)

        self.session.add(gato)
        self.session.commit()
        return gato

    def atualizar_gato(self, gato_id, nome, tipo, idade, sexo, raca, castrado, vacinado,
                       vermifugado, antiparasitado, historico_saude, comportamento,
                       uso_medicacao, tipo_medicacao, criacao, exame_fiv_felv,
                       foto_gato, foto_exame, foto_carteira, tutor_id):
        try:
            gato = self.session.query(Gato).filter_by(id=gato_id).first()

            if gato:
                gato.nome = nome
                gato.tipo = tipo
                gato.idade = idade
                gato.sexo = sexo
                gato.raca = raca
                gato.castrado = castrado
                gato.vacinado = vacinado
                gato.vermifugado = vermifugado
                gato.antiparasitado = antiparasitado
                gato.historico_saude = historico_saude
                gato.comportamento = comportamento
                gato.uso_medicacao = uso_medicacao
                gato.tipo_medicacao = tipo_medicacao
                gato.criacao = criacao
                gato.exame_fiv_felv = exame_fiv_felv
                gato.foto_gato = foto_gato
                gato.foto_exame = foto_exame
                gato.foto_carteira = foto_carteira
                gato.tutor_id = tutor_id

                self.session.commit()
                return "Gato atualizado com sucesso."
            else:
                return "Gato não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao atualizar o gato: {str(e)}"

    def deletar_gato(self, gato_id):
        try:
            gato = self.session.query(Gato).filter_by(id=gato_id).first()

            if gato:
                self.session.delete(gato)
                self.session.commit()
                return "Gato deletado com sucesso."
            else:
                return "Gato não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao deletar o gato: {str(e)}"
