from backend.entities.tutor import Tutor

class TutorService:

    def __init__(self, session):
        self.session = session

    def criar_tutor(self, nome, telefone, endereco, cpf, instagram, identidade_foto,
                    comprovante_residencia_foto):
        try:
            tutor = Tutor(
                nome=nome,
                telefone=telefone,
                endereco=endereco,
                cpf=cpf,
                instagram=instagram,
                identidade_foto=identidade_foto,
                comprovante_residencia_foto=comprovante_residencia_foto
            )
            self.session.add(tutor)
            self.session.commit()
            return tutor

        except Exception as e:
            self.session.rollback()
            return f"Erro ao criar um tutor: {str(e)}"

    def atualizar_tutor(self, tutor_id, nome, telefone, endereco, cpf, instagram, identidade_foto,
                        comprovante_residencia_foto):
        try:
            tutor = self.session.query(Tutor).filter_by(id=tutor_id).first()

            if tutor:
                tutor.nome = nome
                tutor.telefone = telefone
                tutor.endereco = endereco
                tutor.cpf = cpf
                tutor.instagram = instagram
                tutor.identidade_foto = identidade_foto
                tutor.comprovante_residencia_foto = comprovante_residencia_foto

                self.session.commit()
                return "Tutor atualizado com sucesso."
            else:
                return "Tutor não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao atualizar o tutor: {str(e)}"

    def deletar_tutor(self, tutor_id):
        try:
            tutor = self.session.query(Tutor).filter_by(id=tutor_id).first()

            if tutor:
                if not tutor.gatos:
                    self.session.delete(tutor)
                    self.session.commit()
                    return "Tutor deletado com sucesso."
                else:
                    return "Não é possível deletar o tutor. Existem gatos relacionados a ele."
            else:
                return "Tutor não encontrado."

        except Exception as e:
            self.session.rollback()
            return f"Erro ao deletar o tutor: {str(e)}"



