import pytest
from ConfigData.DriverConfig import Driver
from Pages.ios.home_screen_ios import *
from ConfigData.Baseclass import *


class Test_Base_class(Home_Screen_ios):


    def __init__(self,driver):
        super().__init__(driver)

    @pytest.mark.regression
    def App_Check(self):
     self.logger.info("Small check")


