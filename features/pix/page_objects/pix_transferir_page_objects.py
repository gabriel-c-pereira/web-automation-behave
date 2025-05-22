from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class PixTransferirPageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_chave_pix_input(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//span[text()="Digite uma Chave Pix"]/ancestor::div[1]/input')

    def get_avancar_button(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//button[text()="Avançar"]')

    def get_tipo_chave_button(self, tipo_chave: str)-> WebElement:
        return self.driver.find_element(By.XPATH, f'//div[@data-testid="uds-list-item-button-component"]//span[contains(text(), "{tipo_chave}")]')

    def get_valor_input(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//input[@value="0,00"]')
