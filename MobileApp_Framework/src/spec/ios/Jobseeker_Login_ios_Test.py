import pytest
from Pages.ios.home_screen_ios import *

class Test_ios(Home_Screen_ios):


    def __init__(self,driver):
        super().__init__(driver)


    @pytest.mark.regression
    def test_VerifyGoogleLogin(self):
        self.select_allow_notification()

    @pytest.mark.smoke
    def test_VerifyfacebookLogin(self):
        self.select_dontallow_notification()

    @pytest.mark.regression
    def test_VerifygmailLogin(self):
        self.select_allow_notification()






