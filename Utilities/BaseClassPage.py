import inspect
import logging
import random
import string

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class BaseClass:
    # baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @staticmethod
    def getlogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('.//Logs//logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def explicitwait(self, locator):
         WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((locator))).click()


    def explicitwaitSet(self, locator):
       return   WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((locator)))

        # element = WebDriverWait(self.driver, 120).until(
        #     EC.presence_of_element_located((locator)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def random_generator(self,size=8,chars=string.ascii_lowercase+ string.digits):
        return ''.join(random.choice(chars) for x in range(size))


    def loginCommon(self):
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

    #
    # def loginCommon(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.baseurl)
    #     lp = LoginPage(self.driver)
    #     lp.setUsername(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()

    # def screen_shot(self,name):
    #     self.driver.save_screenshot(".\\Screenshots\\" + name)
