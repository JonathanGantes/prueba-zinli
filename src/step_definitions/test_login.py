from pytest_bdd import scenarios, step, parsers
from src.libraries.utils.utils import Utils
from src.pages.zinli import ZinliAndroid

scenarios("login.feature",
          features_base_dir="src/features/")


@step('the login button is disabled')
def login_button_disabled(zinli: ZinliAndroid):
     assert not zinli.login_page.login_button_is_disabled()


@step('the login button is enabled')
def login_button_enabled(zinli: ZinliAndroid):
    assert zinli.login_page.login_button_is_enabled()
