import pytest
from  selenium import  webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClassPage import BaseClass
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_login(BaseClass):
    # baseurl = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getPassword()

    #  old method
    # def test_homePage_Title(self,setup):
    #     log=self.getlogger()
    #     log.info("------------Test_001_Login---------------------")
    #     log.info("----------verfying homepage_title--------------")
    #     self.driver=setup
    #     self.driver.get(self.baseurl)
    #

    @pytest.mark.sanity
    def test_homePage_Title(self):
        log=self.getlogger()
        log.info("------------Test_001_Login---------------------")
        log.info("----------verfying homepage_title--------------")
        self.act_title=self.driver.title
        # close withhout driver
        if self.act_title == "Your store. Login" :
            assert True
            log.info('--------------homepage_title test is passed-----------')
        else:
            self.screen_shot("test_homepageTite.png")
            # self.driver.save_screenshot(".\\Screenshots\\"+ "test_homepageTite.png")
            log.error("-----home page_title is failed--------------------")
            assert False
        #  close with driver
        # if act_title == "Your store. Login":
        #     assert True
        #     log.info('--------------homepage_title test is passed-----------')
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTite.png")
        #     self.driver.close()
        #     log.error("-----home page_title is failed--------------------")
        #     assert False

    # @pytest.mark.skip
    #  old method
    # def test_login(self,setup):
    #     log=self.getlogger()
    #     log.info("---------Verifying Login Test--------------------")
    #     self.driver=setup
    #     self.driver.get(self.baseurl)
    #     self.lp =LoginPage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogi
    @pytest.mark.sanity
    def test_login(self):
        log=self.getlogger()
        log.info("---------Verifying Login Test--------------------")
        self.loginCommon()
        self.act_title=self.driver.title

        # assert act_title=="from se/lenium.webdriver.common.by import By"

        # # close without driver
        if self.act_title == "from selenium.webdriver.common.by import By" :
            assert  True
            log.info('------login test is passed----------------------')
        else:

            # self.screen_shot("test_login.png")
            # save screenshot in screenshot folder
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            log.error("--------login test is failed-------------------")
            assert  False




        # close with driver
        # if act_title=="from selenium.webdriver.common.by import By" :
        #     assert  True
        #     log.info('------login test is passed----------------------')
        #     self.driver.close()
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        #     self.driver.close()
        #     log.error("--------login test is failed-----------------------")
        #     assert  False
