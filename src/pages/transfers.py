from src.libraries.driver import Native
from src.pages.locators import TransfersLocators

class Transfers(Native):
    
    
    def get_transfers_section_text(self):
        return self.get_element_text(TransfersLocators.LABEL_TRANSFERS)
    
    def write_user_in_finder(self, user):
        self.send_keys_to_element(TransfersLocators.INPUT_FIND_USER, user)

    def click_find_user(self):
        self.click_element(TransfersLocators.BUTTON_FIND_USER)
    
    def select_first_user(self):
        self.click_element(TransfersLocators.BUTTON_SELECT_USER)

    def get_amount_section_text(self):
        return self.get_element_text(TransfersLocators.LABEL_AMOUNT_SECTION)

    def get_current_money(self):
        return self.get_element_text(TransfersLocators.LABEL_CURRENT_MONEY)
    
    def write_amount_money(self, money):
        self.send_keys_to_element(TransfersLocators.INPUT_AMOUNT, money)
    
    def click_send_button(self):
        self.click_element(TransfersLocators.BUTTON_SEND)

    def send_button_is_enabled(self):
        return self.element_is_enabled(TransfersLocators.BUTTON_SEND)
    
    def send_button_is_disabled(self):
        return self.element_not_interactable(TransfersLocators.BUTTON_SEND)

    def write_description(self, desc):
        self.send_keys_to_element(TransfersLocators.INPUT_DESCRIPTION, desc)
    
    def write_cvv(self, cvv):
        self.send_keys_to_element(TransfersLocators.INPUT_CVV, cvv)

    def click_cvv_button(self):
        self.click_element(TransfersLocators.BUTTON_CONFIRM_CVV)

    def get_sended_amount(self):
        return self.get_element_text(TransfersLocators.LABEL_AMOUNT)

    def get_masked_card(self):
        return self.get_element_text(TransfersLocators.LABEL_CARD)
    
    def click_confirm_send_button(self):
        self.click_element(TransfersLocators.BUTTON_CONFIRM_SEND)

    def get_successfull_send(self):
        return self.get_element_text(TransfersLocators.LABEL_SUCCESSFUL)

    def click_back_to_home_button(self):
        self.click_element(TransfersLocators.BUTTON_BACK_TO_HOME)