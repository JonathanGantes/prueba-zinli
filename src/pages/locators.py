
from dataclasses import dataclass
from appium.webdriver.common.appiumby import AppiumBy

@dataclass
class LoginLocators:
    
    BUTTON_OMIT = (AppiumBy.XPATH, "//*[contains(@text, 'OMITIR')]")
    BUTTON_CHAT = (AppiumBy.XPATH, "//*[@resource-id='chat-bot-button']")
    INPUTS_EMAIL = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    INPUTS_PASSWD_1 = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    INPUTS_PASSWD_2 = (AppiumBy.XPATH, "(//android.widget.EditText)[1]") #This for when remember password is enabled
    LABEL_GREETINGS = (AppiumBy.XPATH, "//*[@resource-id='login_greeting_title']")
    BUTTON_FORGOT = (AppiumBy.XPATH, "//*[@resource-id='login_forgot_text']")
    TOGGLE_REMEMBER = (AppiumBy.XPATH, "//*[@resource-id='kitten-switch']")
    BUTTON_LOGIN = (AppiumBy.XPATH, "//*[@resource-id='login_accept_btn']")
    BUTTON_REGISTER = (AppiumBy.XPATH, "//*[@resource-id='login_create_account_btn']")




@dataclass
class MyAccountLocators:
    LABEL_WELCOME = (AppiumBy.XPATH, "//*[contains(@text, 'Hola')]")
    BUTTON_SEND_MONEY = (AppiumBy.XPATH, "//*[@resource-id='btn-tab_cash_out']")
    MODAL_ALLOW = (AppiumBy.XPATH, "//*[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")


@dataclass
class TransfersLocators:
    LABEL_TRANSFERS = (AppiumBy.XPATH, "//*[contains(@text, 'Enviar')]")
    INPUT_FIND_USER = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    BUTTON_FIND_USER = (AppiumBy.XPATH, "//*[@resource-id='p2p_contact_input__action']")
    BUTTON_SELECT_USER = (AppiumBy.XPATH, "(//*[@resource-id='p2p_contact_btn'])[1]")

    LABEL_AMOUNT_SECTION = (AppiumBy.XPATH, "//*[contains(@text, 'Monto')]")
    LABEL_CURRENT_MONEY = (AppiumBy.XPATH, "//*[contains(@text, 'Tu Saldo')]")
    INPUT_AMOUNT = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    BUTTON_SEND = (AppiumBy.XPATH, "//*[@resource-id='p2p_next_automatic_btn']")
    INPUT_DESCRIPTION = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    INPUT_CVV = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    BUTTON_CONFIRM_CVV = (AppiumBy.XPATH, "//*[@resource-id='card__modal_btn']")
    LABEL_AMOUNT = (AppiumBy.XPATH, "//*[starts-with(@text, '$')]")
    LABEL_CARD = (AppiumBy.XPATH, "//*[starts-with(@text, '•••• •••• •••')]")
    BUTTON_CONFIRM_SEND = (AppiumBy.XPATH, "//*[@resource-id='p2p_confirm_next_btn']")
    LABEL_SUCCESSFUL = (AppiumBy.XPATH, "//*[@resource-id='SABTitle']")
    BUTTON_BACK_TO_HOME = (AppiumBy.XPATH, "//*[@resource-id='SAFSecondaryBtn']")

    




    

