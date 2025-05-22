from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class HomePageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_home_conteudo_principal_container(self)-> WebElement:
        return self.driver.find_element(By.ID, "single-spa-application:@unicred/app-home")

    def get_pagar_transferir_menu(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//div[contains(@aria-label, "Pagar e transferir")]')

    def get_pix_submenu(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//div[contains(@aria-label, "Pix")]')

    def get_pagar_e_transferir_pix_submenu(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//div[contains(@aria-label, "Pagar e Transferir ")]')