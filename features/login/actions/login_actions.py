from features.login.page_objects.login_page_objects import LoginPageObjects


class LoginActions:
    def __init__(self):
        self.login_page_objects = LoginPageObjects()

    def preencher_agencia(self, agencia: str):
        self.login_page_objects.get_agencia_input().send_keys(agencia)

    def preencher_conta(self, conta: str):
        self.login_page_objects.get_conta_input().send_keys(conta)

    def clicar_avancar(self):
        self.login_page_objects.get_avancar_button().click()

    def preencher_senha(self, senha: str):
        for digito in senha:
            self.login_page_objects.get_senha_button(digito).click()

    def clicar_entrar(self):
        self.login_page_objects.get_entrar_button().click()
