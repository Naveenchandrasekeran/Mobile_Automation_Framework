from appium.webdriver.common.mobileby import MobileBy
from ConfigData.DriverConfig import Driver
from ConfigData.Baseclass import *


class home_screen(App):


    jobseeker_button = (MobileBy.ID, "landing-text")
    employer_button = (MobileBy.ID, "landing-text")

    def __init__(self, driver):
        super().__init__(driver)

    def select_Jobseeker(self):
      App.is_displayed(self, self.jobseeker_button)
      App.assert_text(self,self.jobseeker_button,"Job")
      App.click(self, self.jobseeker_button)
      self.logger.info("Selected test")

    def select_Employer(self):
        App.is_displayed(self, self.employer_button)
        App.assert_text(self, self.employer_button, "test")
        App.click(self, self.employer_button)
        self.logger.info("text")



