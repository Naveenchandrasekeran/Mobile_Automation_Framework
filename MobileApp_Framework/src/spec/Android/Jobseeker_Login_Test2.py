import pytest
from Pages.Android.home_screen import *
from Pages.Android.login_screen import *
from ConfigData import TestData_Cofig

class Test_Jobseeker_Login(logincheck):


    def __init__(self,driver):
        super().__init__(driver)

    @pytest.mark.smoke(order=2)
    @pytest.mark.regression
    def test_VerifygmailLogins(self):

      self.select_Jobseeker()
      self.select_Continuewithemail()
      self.enter_Login_Credentials(TestData_Cofig.jobseeker_login_email,TestData_Cofig.jobseeker_password)


