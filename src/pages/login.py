from src.libraries.driver import Native
from src.pages.locators import LoginLocators

class LoginPage(Native):
    
    
    def click_omit_button(self):
        self.click_element(LoginLocators.BUTTON_OMIT)
    
    def click_chat_bot_button(self):
        self.click_element(LoginLocators.BUTTON_CHAT)

    def get_greeting_text(self):
        return self.get_element_text(LoginLocators.LABEL_GREETINGS)
    
    def write_email(self, email):
        self.send_keys_to_element(LoginLocators.INPUTS_EMAIL, email)

    def write_password(self, passwd):
        if ("buenas") in self.get_greeting_text().lower():
            self.send_keys_to_element(LoginLocators.INPUTS_PASSWD_1, passwd)
        else:
            self.send_keys_to_element(LoginLocators.INPUTS_PASSWD_2, passwd)

    def click_forgot_password(self):
        self.click_element(LoginLocators.BUTTON_FORGOT)
    
    def click_toggle_remember(self):
        self.click_element(LoginLocators.TOGGLE_REMEMBER)
    
    def click_login_button(self):
        self.click_element(LoginLocators.BUTTON_LOGIN)

    def login_button_is_enabled(self):
        return self.element_is_enabled(LoginLocators.BUTTON_LOGIN)

    def click_register(self):
        self.click_element(LoginLocators.BUTTON_REGISTER)

    def login_button_is_disabled(self):
        return self.element_not_interactable(LoginLocators.BUTTON_LOGIN)
