import time

from features.loader.page_objects import LoaderPageObjects


class LoaderActions:
    def __init__(self):
        self.loader_page_objects = LoaderPageObjects()

    def esperar_loader_sumir(self):
        loader_esta_visivel = False
        for _ in range(5):
            loader_esta_visivel = self.loader_page_objects.get_loader().get_attribute("visibility") != "hidden"
            if not loader_esta_visivel:
                break
            time.sleep(1)