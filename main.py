from backend.services.gato_service import GatoService
from backend.services.tutor_service import TutorService
from backend.services.quarto_service import QuartoService
from backend.entities.reserva import Reserva
from backend.repositories.database import criar_sessao


if __name__ == "__main__":
    session = criar_sessao()
    tutor_service = TutorService(session)
    gato_service = GatoService(session)
    quarto_service = QuartoService(session)

    '''
    tutor = tutor_service.criar_tutor("Aristolfo", "123-123-123", "Rua 123", "123.123.123-00",
                                    "@aristolfinho", "identidade.png", "comprovante.png")

    gato = gato_service.criar_gato("Bartolomeu", "Cliente", 2, "Macho",
                                   "Shnowzer", "não", "não", "sim",
                                   "sim", "nunca teve doeça", "dócil",
                                   "não", None, "indoor", "sim",
                                   "gato.png", "exame.png", "carteira.png", 1)

    gato = gato_service.atualizar_gato(2, "teste", "Cliente", 2, "Macho",
                                       "Shnowzer", "não", "não", "sim",
                                       "sim", "nunca teve doeça", "dócil",
                                       "não", None, "indoor", "sim",
                                       "gato.png", "exame.png", "carteira.png", 2)
    
    tutor = tutor_service.atualizar_tutor(1, "Matheus", "123-123-123", "Rua 123", "123.123.123-00",
                                          "@aristolfinho", "identidade.png", "comprovante.png")
    
    
    tutor_service.deletar_tutor(2)
    gato_service.deletar_gato(2)

    quarto = quarto_service.criar_quarto("Cat World", "1,73 x 2", "Premium",
                                         "Gatil para gatos de clientes", 90.0, 80.0,
                                         "quarto.png", "Sim")
    
    quarto = quarto_service.atualizar_quarto(1, "Cat Beach", "1.5 x 1.79", "Premium",
                                             "Quarto para gatos de clientes", 70.0, 60.0,
                                             "img.png", "Não")
    
    quarto_service.deletar_quarto(1)
    '''
    