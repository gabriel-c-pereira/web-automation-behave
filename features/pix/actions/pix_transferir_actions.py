from features.pix.page_objects.pix_transferir_page_objects import PixTransferirPageObjects


class PixTransferirActions:
    def __init__(self):
        self.pix_transferir_page_object = PixTransferirPageObjects()

    def preencher_chave_pix(self, chave: str):
        self.pix_transferir_page_object.get_chave_pix_input().send_keys(chave)

    def clicar_avancar(self):
        self.pix_transferir_page_object.get_avancar_button().click()

    def selecionar_identificacao_chave(self, tipo_chave: str):
        self.pix_transferir_page_object.get_tipo_chave_button(tipo_chave).click()

    def preencher_valor(self, valor: float):
        self.pix_transferir_page_object.get_valor_input().send_keys(str(valor))