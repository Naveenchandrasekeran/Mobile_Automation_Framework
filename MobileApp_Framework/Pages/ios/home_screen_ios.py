from appium.webdriver.common.mobileby import MobileBy
from ConfigData.DriverConfig import Driver
from ConfigData.Baseclass import *



class Home_Screen_ios(App):
    """
    home screen locators
    """
    allow_notification_button=(MobileBy.ACCESSIBILITY_ID,"Allow")

    dontallow_notification_button=(MobileBy.ACCESSIBILITY_ID,"Don’t Allo")
  
    # swipeMenu = {'ANDROID': (MobileBy.ACCESSIBILITY_ID, "Swipe"),'IOS': (MobileBy.ACCESSIBILITY_ID, "Swipe")}

    def __init__(self, driver):
        super().__init__(driver)

    def select_allow_notification(self):
        App.is_displayed(self,self.allow_notification_button)
        App.click(self,self.allow_notification_button)
        self.logger.info("Clicked Allow Notification")

    def select_dontallow_notification(self):
        App.is_displayed(self,self.dontallow_notification_button)
        App.click(self,self.dontallow_notification_button)
        self.logger.info("Clicked dont'Allow Notification")
