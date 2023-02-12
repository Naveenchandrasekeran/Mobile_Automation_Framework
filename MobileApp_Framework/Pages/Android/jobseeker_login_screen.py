from appium.webdriver.common.mobileby import MobileBy
from ConfigData.DriverConfig import Driver
from Pages.Android.home_screen import *


class jobseeker_login(home_screen):
    """
    jobseeker login  locators
    """
    continue_with_email = (MobileBy.ID, "signin-email")



    def __init__(self, driver):
        super().__init__(driver)

    def select_Continuewithemail(self):
        App.is_displayed(self, self.continue_with_email)
        App.assert_text(self,self.continue_with_email,"Continue with Email")
        App.click(self, self.continue_with_email)
        self.logger.info("selected continue with email")

