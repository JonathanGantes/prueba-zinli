
from src.libraries.driver import Native
from src.pages.locators import MyAccountLocators

class MyAccount(Native):
    
    
    def get_welcome_text(self):
        return self.get_element_text(MyAccountLocators.LABEL_WELCOME)
    
    def click_send_money_button(self):
        self.click_element(MyAccountLocators.BUTTON_SEND_MONEY)

    def click_allow(self):
        self.click_element(MyAccountLocators.MODAL_ALLOW)
