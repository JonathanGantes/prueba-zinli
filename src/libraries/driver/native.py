import time
from src.libraries.driver import RemoteDriver

TIMEOUT = 25
NASSA_QA_POLL_TIMER = 1


class Native(RemoteDriver):
    # pylint: disable=broad-except

    def wait_present_element(self, element_locator, retries=TIMEOUT, poll=NASSA_QA_POLL_TIMER):
        element = None
        for _ in range(retries):
            try:
                time.sleep(poll)
                element = self.driver.find_element(*element_locator)
                break
            except Exception:
                pass
        return element

    def wait_interactable_element(self, element_locator, retries=TIMEOUT, poll=NASSA_QA_POLL_TIMER):
        element = None
        for _ in range(retries):
            try:
                time.sleep(poll)
                element = self.driver.find_element(*element_locator)
                if element.is_enabled():
                    break
            except Exception:
                pass
        return element

    def wait_displayed_element(self, element_locator, retries=TIMEOUT, poll=NASSA_QA_POLL_TIMER):
        element = None
        for _ in range(retries):
            try:
                time.sleep(poll)
                element = self.driver.find_element(*element_locator)
                element.is_displayed()
                print("xd")
                if element.is_displayed():
                    break
            except Exception:
                pass
        return element

    def click_element(self, locator):
        self.wait_displayed_element(locator).click()

    def send_keys_to_element(self, locator, value):
        self.wait_displayed_element(locator).send_keys(value)

    def send_keys_to_element_by_key(self, element_locator, text):
        element = self.wait_displayed_element(element_locator)
        for key in text:
            element.send_keys(key)

    def get_element_text(self, locator, wait_time=TIMEOUT):
        return self.wait_displayed_element(locator, retries=wait_time).text

    def get_element_attribute(self, locator, atributte):
        return self.wait_displayed_element(locator).get_attribute(atributte)

    def element_is_displayed(self, locator):
        return self.driver.find_element(locator).is_displayed()

    def get_elemets_list(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def element_is_enabled(self, locator):
        return self.wait_displayed_element(locator).is_enabled()

    def close_keyboard(self):
        if self.driver.capabilities['platform'] == "LINUX":
            self.driver.hide_keyboard()

    def switch_window(self, window):
        self.driver.switch_to.context(window)

    def switch_to_iframe(self, locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default_iframe(self):
        self.driver.switch_to.default_content()

    def swipe_up(self):
        if self.driver.capabilities['platform'] == "LINUX":
            self.driver.swipe(50, 500, 50, 1200)

    def swipe_down(self):
        if self.driver.capabilities['platform'] == "LINUX":
            self.driver.swipe(50, 1500, 50, 200)

    def scroll_down(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def element_not_interactable(self, locator):
        element = self.wait_displayed_element(locator)

        try:
            element.click()
            return False
        except Exception:
            return True

    # pylint: enable=broad-except
