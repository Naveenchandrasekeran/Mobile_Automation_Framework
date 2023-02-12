from allure_commons._allure import attach
from appium import webdriver
import unittest
import os
from datetime import datetime
import pytest
from appium.webdriver.appium_service import AppiumService
from pytest_html_reporter import attach
from ConfigData import device_config
from settings import UDID


class Driver(unittest.TestCase):

    def startAppium(self):
        self.appium_service = AppiumService()
        self.appium_service.start()

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global desired_caps

        self.startAppium()
        self.logger.info("Configuring desired capabilities")
        if os.getenv('PYTEST_XDIST_WORKER'):
            if self.app == 'ios':
                desired_caps = {
                    'platformName': 'iOS',
                    'platformVersion': '16.2',
                    'deviceName': 'iPhone 14 Pro Max',
                    'automationName': 'XCUITest',
                    'app': f'{os.popen("pwd").read().rstrip()}/Apps/ios.app'
                }
            elif self.app == 'android':
                desired_caps = {
                    'platformName': device_config.platformName,
                    'platformVersion': device_config.platformVersion,
                    'deviceName': device_config.deviceName,
                    'wdaLocalPort': Driver.wda_port(self),
                    'udid': Driver.android_device_name(self),
                    "automationName": "UiAutomator2",
                    'appPackage': device_config.appPackage,
                    'appActivity': device_config.appActivity,
                    'app': f'{os.popen("pwd").read().rstrip()}/Apps/Apk.apk',
                    'noReset': True
                }
        else:
            if self.app == 'ios':
                desired_caps = self.ios()

            elif self.app == 'android':
                desired_caps = self.android()

        self.logger.info("Initiating Appium driver")
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub",desired_caps)
        self.logger.info("App launch succcessfully")
        self.driver.implicitly_wait(10)

    def android(self):
        if self.device == 'emulator':
            return dict(platformName=device_config.platformName, platformVersion=device_config.platformVersion,
                        deviceName=device_config.deviceName,
                        app=f'{os.popen("pwd").read().rstrip()}/Apps/.apk',noReset=True)
        elif self.device == 'real device':
            return dict(platformName=device_config.platformName, platformVersion='',
                        deviceName=device_config.deviceName,
                        app=f'{os.popen("pwd").read().rstrip()}/Apps/_.apk',noReset=True)

    def ios(self):
        if self.device == 'simulator':
            return dict(platformName='iOS', platformVersion='16.2', deviceName='iPhone 14 Pro Max',
                        app=f'{os.popen("pwd").read().rstrip()}/Apps/.app',
                        automationName='XCUITest')
        elif self.device == 'real device':
            return dict(platformName='iOS', platformVersion='16.2', deviceName='iPhone 14 Pro Max',
                        udid=f'{UDID}', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/Apps/.app',
                        automationName='XCUITest')

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device, get_logger):
        self.app = app
        self.device = device
        self.logger = get_logger

    def wda_port(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 8101
        else:  # include 'master' and 'gw0'
            return 8100

    def android_device_name(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
            return 'emulator-5554'
        elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 'emulator-5556'
        else:  # default
            return 'emulator-5554'

if __name__ == '__main__':
    unittest.main()
