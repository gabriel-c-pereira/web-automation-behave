from features.assinatura_eletronica.assinatura_eletronica_actions import AssinaturaEletronicaActions
from features.home.actions.home_actions import HomeActions
from features.home.validation_points.home_validation_points import HomeValidationPoints
from features.loader.loader_actions import LoaderActions
from features.login.actions.login_actions import LoginActions
from features.pix.actions.pagar_e_transferir_pix_actions import PagarETransferirPixActions
from features.pix.actions.pix_transferir_actions import PixTransferirActions
from framework.drive_manager import DriverManager


def before_scenario(context, scenario):
    driver = DriverManager().get_driver()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("")

    context.loader_actions = LoaderActions()
    context.login_actions = LoginActions()
    context.home_actions = HomeActions()
    context.home_validation_points = HomeValidationPoints()
    context.pagar_e_transferir_pix_actions = PagarETransferirPixActions()
    context.pix_transferir_actions = PixTransferirActions()
    context.assinatura_eletronica_actions = AssinaturaEletronicaActions()


def after_scenario(context, scenario):
    DriverManager().quit_driver()
