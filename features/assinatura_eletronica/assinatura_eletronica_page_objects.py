from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class AssinaturaEletronicaPageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_senha_button(self, digito: str)-> WebElement:
        return self.driver.find_element(By.XPATH, f"//button[@data-testid='uds-button-component' and contains(text(), '{digito}')]")

    def get_confirmar_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@data-testid='uds-button-component' and text()='Confirmar']")