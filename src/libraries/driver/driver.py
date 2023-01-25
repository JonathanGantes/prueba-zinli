from typing import Union
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from src.libraries.utils import Utils

BS_STACK_OPTIONS = "bstack:options"
DRIVER = None


class RemoteDriver():

    # Driver must be a RemoteWebDriver from appium or selenium
    __driver: Union[appium_webdriver.Remote, selenium_webdriver.Remote]

    def __init__(self, driver: Union[appium_webdriver.Remote, selenium_webdriver.Remote]):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    def quit_driver(self):
        try:
            screenshot_path = 'resources/last_screenshot.png'
            self.driver.save_screenshot(screenshot_path)
            self.driver.quit()

        except (Exception):
            print("info: Another process has already closed the app process.")

    def log_info_to_browser_stack(self, message, level="info"):
        """
        Sends logs to BrowserStack
        @param message : str
        @param level : str = (info | debug | warn | error)
        """
        script = ('browserstack_executor: {"action": "annotate", '
                  '"arguments": {"data":"' + message + '","level": "' + level + '"}}')
        self.driver.execute_script(script)

    def set_test_status(self, status: str, reason: str):
        """
        Sends to BrowserStack the scenario status
        @param status String: (passed | failed)
        @param reason String
        """
        script = f'''browserstack_executor:{{
            "action": "setSessionStatus",
            "arguments": {{"status": "{status}", "reason": "{Utils.clear_string_for_excecutor(reason)}"}}
        }}'''
        self.driver.execute_script(script)

    def element_is_present(self, locator) -> bool:
        elemen = self.driver.find_elements(*locator)
        if len(elemen) > 0:
            return True
        return False

    def get_elemet_amount(self, locator) -> int:
        elements = self.driver.find_elements(*locator)
        return len(elements)
