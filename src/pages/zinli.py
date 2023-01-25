
from src.pages import LoginPage, MyAccount, Transfers
from src.libraries.driver import Native
class ZinliAndroid:

    login_page = None
    common = None

    def __init__(self, driver) -> None:
        self.login_page = LoginPage(driver)
        self.my_acc_page = MyAccount(driver)
        self.transfers_page = Transfers(driver)
        self.common = Native(driver)