from pytest_bdd import scenarios, step, parsers
from src.libraries.utils.utils import Utils
from src.pages.zinli import ZinliAndroid

scenarios("transfers.feature",
          features_base_dir="src/features/")


@step('i click the transfers button')
def click_transfers(zinli: ZinliAndroid):
    zinli.my_acc_page.click_send_money_button()
    zinli.my_acc_page.click_allow()


@step('i select the first frecuent contact')
def select_frist_contact(zinli: ZinliAndroid):
    zinli.transfers_page.select_first_user()


@step(parsers.parse('i check if amount to send showed equals[{money}]'))
def check_amount_of_money(zinli: ZinliAndroid, money):
    assert money in zinli.transfers_page.get_sended_amount()


@step('i click the send button')
def click_send_button(zinli: ZinliAndroid):
    zinli.transfers_page.click_send_button()

@step('i confirm the cvv')
def click_cvv_button(zinli: ZinliAndroid):
    zinli.transfers_page.click_cvv_button()


@step('i confirm the send')
def click_confirm_send(zinli: ZinliAndroid):
    zinli.transfers_page.click_confirm_send_button()


@step(parsers.parse('i write [{money}] to send'))
def _(zinli: ZinliAndroid, money):
    zinli.transfers_page.write_amount_money(money)


@step(parsers.parse('i write a description [{desc}]'))
def write_send_desc(zinli: ZinliAndroid, desc):
    zinli.transfers_page.write_description(desc)


@step(parsers.parse('i write the cvv [{cvv}]'))
def _(zinli: ZinliAndroid, cvv):
    zinli.transfers_page.write_cvv(cvv)


@step('i click the back to my account button')
def click_back_to_my_acc(zinli: ZinliAndroid):
    zinli.transfers_page.click_back_to_home_button()


@step('the successful send message is displayed')
def _(zinli: ZinliAndroid):
    print(zinli.transfers_page.get_successfull_send())