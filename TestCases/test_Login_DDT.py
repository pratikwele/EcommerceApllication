import time

import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.BaseClassPage import  BaseClass
# from Utilities.customLogger import LogGen
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities.XLUTILS import XLUtils
# from  Utilities.BaseClassPage import Base
import openpyxl
class Test_002(BaseClass):
    # baseurl = ReadConfig.getApplicationUrl()

    path="./Testdata/TestDataexl.xlsx"

    # old method
    # def test_DDT(self,setup):
    #     log=self.getlogger()
    #     log.info("------------Test_002_Login-DDT----------------------")
    #     log.info("_____________Verifying Login Test--DDT__________________")
    #     self.driver = setup
    #     self.lp =LoginPage(self.driver)
    #     self.driver.get(self.baseurl)
    #
    @pytest.mark.sanity
    def test_DDT(self):
        log=self.getlogger()
        log.info("------------Test_002_Login-DDT----------------------")
        log.info("_____________Verifying Login Test--DDT__________________")
        self.lp =LoginPage(self.driver)
        for r in range(1,2):
          self.username= XLUtils.readData(self.path ,'Sheet1',r,1)
          self.password=XLUtils.readData(self.path ,'Sheet1',r,2)
          self.lp.setUsername(self.username)
          self.lp.setPassword(self.password)
          self.lp.clickLogin()
          self.act_title=self.driver.title
          # close without driver
          if self.act_title=="Dashboard / nopCommerce administration" :
             assert True
             log.info("...Login Test-DDT is passed ")
             time.sleep(3)
             self.lp.clickLogout()
          else:
              self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt.png")
              log.error("...Login Test-DDT is failed ")
              assert False

        # close with driver
        # if self.act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     log.info("...Login Test-DDT is passed ")
        #     self.lp.clickLogout()
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt.png")
        #     log.error("...Login Test-DDT is failed ")
        #     self.driver.close()
        #     assert False

