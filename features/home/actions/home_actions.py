from features.home.page_objects.home_page_objects import HomePageObjects


class HomeActions:
    def __init__(self):
        self.home_page_objects = HomePageObjects()

    def selecionar_menu_pagar_transferir(self):
        self.home_page_objects.get_pagar_transferir_menu().click()

    def selecionar_submenu_pix(self):
        self.home_page_objects.get_pix_submenu().click()

    def selecionar_submenu_pagar_e_transferir_pix(self):
        self.home_page_objects.get_pagar_e_transferir_pix_submenu().click()
