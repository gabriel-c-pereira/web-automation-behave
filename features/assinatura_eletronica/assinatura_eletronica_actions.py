import time

from features.assinatura_eletronica.assinatura_eletronica_page_objects import AssinaturaEletronicaPageObjects


class AssinaturaEletronicaActions:
    def __init__(self):
        self.assinatura_eletronica_page_objects = AssinaturaEletronicaPageObjects()

    def preencher_assinatura_eletronica(self, senha: str):
        for digito in senha:
            self.assinatura_eletronica_page_objects.get_senha_button(digito).click()
            time.sleep(0.5)

        self.assinatura_eletronica_page_objects.get_confirmar_button().click()