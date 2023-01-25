import json
import os
from typing import Union
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
# type: ignore    
BS_STACK_OPTIONS = "bstack:options"

class DriverFactory:

    #Driver must be a RemoteWebDriver from appium or selenium
    __driver: Union[appium_webdriver.Remote, selenium_webdriver.Remote]

    def create_bstack_driver(self, device: str, scenario_name: str, feature_name: str):
        browserstack_url = str(os.environ.get("BSTACK_URL"))
        capabilities = self.set_driver_capabilities(device, scenario_name, feature_name)

        if device in ('android', 'ios'):
            self.__driver = appium_webdriver.Remote(
                command_executor=browserstack_url, desired_capabilities=capabilities
            )
        elif device in ('desktop'):
            self.__driver = selenium_webdriver.Remote(
                command_executor=browserstack_url, desired_capabilities=capabilities
            )

        if self.current_platform() == "WINDOWS":
            self.__driver.maximize_window()

        return self.__driver

    def create_local_driver(self):
        deviceName = str(os.environ.get("DEVICE_NAME"))
        capabilities = {
                "appium:deviceName": f"{deviceName}",
                "appium:platformName": "android",
                "appium:appPackage": "io.mftech.biipsta",
                "appium:appActivity": "io.mftech.biipsta.MainActivity"
        }
        url = "http://127.0.0.1:4723/wd/hub"
        self.__driver = appium_webdriver.Remote(
                command_executor=url, desired_capabilities=capabilities)
        return self.__driver


    @staticmethod
    def set_driver_capabilities(device: str, scenario_name: str, feature_name:str):

        if device == 'android':
            with open("resources/devices/android.json", "r", encoding="utf8") as file:
                capabilities = json.load(file)
            capabilities["app"] = os.environ.get("APP_ID")
        elif device == 'desktop':

            with open("resources/devices/chrome.json", "r", encoding="utf8") as file:
                capabilities = json.load(file)
        else:
            print("Porfavor introduzca un dispositivo valido")

        capabilities[BS_STACK_OPTIONS]["sessionName"] = feature_name + \
            " : " + scenario_name
        capabilities[BS_STACK_OPTIONS]["projectName"] = os.environ.get(
            "PROJECT_NAME")
        capabilities[BS_STACK_OPTIONS]["buildName"] = os.environ.get(
            "ENVIROMENT")
        capabilities[BS_STACK_OPTIONS]["userName"] = os.environ.get(
            "BSTACK_USER")
        capabilities[BS_STACK_OPTIONS]["accessKey"] = os.environ.get(
            "BSTACK_PASSWORD")
        capabilities[BS_STACK_OPTIONS]["idleTimeout"] = os.environ.get(
            "IDLE_TIMEOUT")

        return capabilities

    def current_platform(self):

        if 'platformName' in self.__driver.capabilities:
            platform : str = self.__driver.capabilities['platformName']
        else:
            platform: str = self.__driver.capabilities['platform']

        return platform.upper()
