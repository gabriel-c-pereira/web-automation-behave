from behave import given, when, then

@given("que o usuário está logado no IB")
def logar_no_ib(context):
    agencia = "1706"
    conta = "1007033"
    senha = "1122"
    context.login_actions.preencher_agencia(agencia)
    context.login_actions.preencher_conta(conta)
    context.login_actions.clicar_avancar()
    context.login_actions.preencher_senha(senha)
    context.login_actions.clicar_entrar()
    context.home_validation_points.validar_home_carregou()


@given("que acessa o menu de pagamentos e transferências pix")
def acessar_menu_pagamentos_e_transferencias(context):
    context.home_actions.selecionar_menu_pagar_transferir()
    context.home_actions.selecionar_submenu_pix()
    context.home_actions.selecionar_submenu_pagar_e_transferir_pix()


@when("é feita uma transferência para chave {chave} do tipo {tipo_chave}")
def transferir_para_chave(context, chave: str, tipo_chave: str):
    context.loader_actions.esperar_loader_sumir()
    context.pagar_e_transferir_pix_actions.selecionar_transferir_com_chave_pix()
    context.pix_transferir_actions.preencher_chave_pix(chave)
    context.pix_transferir_actions.clicar_avancar()
    context.pix_transferir_actions.selecionar_identificacao_chave(tipo_chave)
    context.pix_transferir_actions.preencher_valor(1.64)
    context.pix_transferir_actions.clicar_avancar()
    context.loader_actions.esperar_loader_sumir()
    context.pix_transferir_actions.clicar_avancar()
    context.loader_actions.esperar_loader_sumir()
    context.assinatura_eletronica_actions.preencher_assinatura_eletronica("88995566")


@then("deve aparecer o comprovante da transação")
def step_impl():
    pass