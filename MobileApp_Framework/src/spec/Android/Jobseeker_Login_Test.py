import pytest
from Pages.Android.home_screen import *
from Pages.Android.login_screen import *
from ConfigData import TestData_Cofig

class Test_Jobseeker_Login(logincheck):


    def __init__(self,driver):
        super().__init__(driver)

    @pytest.mark.smoke(order=2)
    def test_VerifygmailLogin(self):

      self.select_Jobseeker()
      self.select_Continuewithemail()
      self.enter_Login_Credentials(TestData_Cofig.jobseeker_login_email,TestData_Cofig.jobseeker_password)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_VerifyGoogleLogin(self):
     self.select_Jobseeker()
     self.select_Continuewithemail()
     self.enter_Login_Credentials(TestData_Cofig.jobseeker_login_email,TestData_Cofig.jobseeker_password)



        #self.select_Jobseeker()
       # self.select_Continuewithemail()
       # self.enter_Login_Credentials(TestData_Cofig.jobseeker_login_email,TestData_Cofig.jobseeker_password)


#curl -H "Authorization: Bearer ${TOKEN}" -F "file=@TestSuites.xml;type=application/xml" https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey="JQA"&autoCreateTestCases=true

