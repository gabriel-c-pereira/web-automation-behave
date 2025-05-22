import time
from features.home.page_objects.home_page_objects import HomePageObjects


class HomeValidationPoints:
    def __init__(self):
        self.home_page_objects = HomePageObjects()

    def validar_home_carregou(self):
        estou_na_home = False
        for _ in range(5):
            try:
                estou_na_home = self.home_page_objects.get_home_conteudo_principal_container().is_displayed()
            except Exception as _:
                time.sleep(2)

        if estou_na_home is not True:
            raise Exception("Não estou na Home!!!")
