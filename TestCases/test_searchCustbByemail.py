import time

import pytest

from PageObjects.AddCustPage import AddCust
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchCustPage import Test_search_cust
from Utilities.BaseClassPage import BaseClass
from Utilities.readProperties import ReadConfig


class Test_004_SearchCustByemail(BaseClass):
    # baseurl = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getPassword()

    # old method
    # def test_searchCustByemail(self,setup):
    #     self.loginCommon(setup)
    #     log=self.getlogger()
    #     self.driver=setup
    @pytest.mark.regression
    def test_searchCustByemail(self):
        self.loginCommon()
        log=self.getlogger()
        # self.driver.get(self.baseurl)
        # lp =LoginPage(self.driver)
        # lp.setUsername(self.username)
        # lp.setPassword(self.password)
        # lp.clickLogin()
        log.info("--------Test_004_SearchCustByemail---------------------")
        log.info("----------verfying test_search_CustByemail------------------------")
        ac=AddCust(self.driver)
        time.sleep(5)
        self.explicitwait(ac.clickmenu_customer())
        time.sleep(5)
        self.explicitwait(ac.click_sub_menu_customer())
        log.info("----------start of searchcustByemail test------------")
        sc=Test_search_cust(self.driver)
        sc.setEmailid_Srch_Cust()
        sc.clickSearch()
        self.row=sc.getLenRow()
        print('row=',self.row)
        self.col=sc.getLenCol()
        print('col=',self.col)
        self.searchemail=sc.getsearchemail()
        # print(self.searchemail)
        # close without driver
        if  self.searchemail == "james_pan@nopCommerce.com":
            assert True
            log.info("-----test_search_CustByemail is passed----------")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search_CustByemail.png")
            log.error("--------test_search_CustByemail is failed-----------------------")
            assert False

        # close with driver
        # if  self.searchemail == "james_pan@nopCommerce.com":
        #     assert True
        #     log.info("-----test_search_CustByemail is passed----------")
        #     self.driver.close()
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_search_CustByemail.png")
        #     self.driver.close()
        #     log.error("--------test_search_CustByemail is failed-----------------------")
        #     assert False












