import pytest
from ConfigData.DriverConfig import Driver
from Pages.Android.login_screen import *

class Test_BaseClass(logincheck):


    def __init__(self,driver):
        super().__init__(driver)

    @pytest.mark.smoke
    def App_Check(self):
        self.logger.info("Ignore this TC")
