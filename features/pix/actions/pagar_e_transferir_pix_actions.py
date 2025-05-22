from features.pix.page_objects.pagar_e_transferir_pix_page_objects import PagarETransferirPixPageObjects


class PagarETransferirPixActions:
    def __init__(self):
        self.pagar_e_transferir_pix_page_objects = PagarETransferirPixPageObjects()

    def selecionar_transferir_com_chave_pix(self):
        self.pagar_e_transferir_pix_page_objects.get_transferir_com_chave_pix_button().click()
