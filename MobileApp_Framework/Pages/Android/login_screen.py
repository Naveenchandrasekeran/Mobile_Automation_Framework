from appium.webdriver.common.mobileby import MobileBy
from ConfigData.DriverConfig import Driver
from Pages.Android.jobseeker_login_screen import *


class logincheck(jobseeker_login):
    """
    login screen locators
    """
    jobseeker_emailid_input= (MobileBy.ID, "/email-email")
    jobseeker_password_input= (MobileBy.ID, "email-password")
    jobseeker_next_button=(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.TextView")
    jobseeker_submit_button=(MobileBy.ID, "email-submit")

    # swipeMenu = {'ANDROID': (MobileBy.ACCESSIBILITY_ID, "Swipe"),'IOS': (MobileBy.ACCESSIBILITY_ID, "Swipe")}

    def __init__(self, driver):
        super().__init__(driver)


    def enter_Login_Credentials(self,email,password):
        App.is_displayed(self,self.jobseeker_emailid_input)
        App.send_keys(self,self.jobseeker_emailid_input,email)
        self.logger.info("Entered emailid")
       # App.is_displayed(self,self.jobseeker_next_button,"Next")
        App.click(self,self.jobseeker_submit_button)
        App.is_displayed(self,self.jobseeker_password_input)
        App.send_keys(self,self.jobseeker_password_input,password)
        self.logger.info("Entered Password")
        App.is_displayed(self,self.jobseeker_submit_button)
        App.click(self,self.jobseeker_submit_button)
        self.logger.info("Selected submit button")
        App.is_displayed("Naveen")

