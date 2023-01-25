import os
from pytest_bdd import step, parsers
from src.libraries.utils.utils import Utils
from src.libraries.driver import DriverFactory
from src.pages.zinli import ZinliAndroid
from src import TEST_DATA

def pytest_bdd_before_scenario(feature, scenario):
    TEST_DATA.feature_name = feature.name
    TEST_DATA.test_name = scenario.name


@step(parsers.parse('i open the app in [{device}]'), target_fixture="zinli")
def open_app(device):
    
    envir = str(os.environ.get("EJECUTAR_LOCAL"))
    if envir.lower() == "true":
        driver = DriverFactory().create_local_driver()
    else:
        driver = DriverFactory().create_bstack_driver(device, TEST_DATA.test_name, TEST_DATA.feature_name)

    zinli = ZinliAndroid(driver)
    return zinli


@step('i click the omit button', target_fixture="login_page")
def click_omit(zinli: ZinliAndroid):
    zinli.login_page.click_omit_button()


@step(parsers.parse('i write the email [{email}]'))
def write_email(email, zinli: ZinliAndroid):
    zinli.login_page.write_email(email)


@step(parsers.parse('i write the password [{password}]'))
def write_password(password, zinli: ZinliAndroid):
    zinli.login_page.write_password(password)


@step('i am redirected to the MyAcount screen')
def account_screen(zinli: ZinliAndroid):
    assert "Hola" in zinli.my_acc_page.get_welcome_text()


@step('i click the login button')
def click_login_button(zinli: ZinliAndroid):
    zinli.login_page.click_login_button()

@step('i click the transfers button')
def click_transfers(zinli: ZinliAndroid):
    zinli.my_acc_page.click_send_money_button()
    