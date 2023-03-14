import time

import pytest

from PageObjects.AddCustPage import AddCust
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchCustPage import Test_search_cust
from PageObjects.test_updateCustPage import Test_Update_cust
from Utilities.BaseClassPage import BaseClass
from Utilities.readProperties import ReadConfig


class Test_005_updateCust(BaseClass):
    # baseurl = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getPassword()

    # old method
    # def test_updateCust(self,setup):
    #     self.loginCommon(setup)
    #     self.driver=setup
    #     log=self.getlogger()
    #     # self.driver=setu
    @pytest.mark.regression
    def test_updateCust(self):
        self.loginCommon()
        log=self.getlogger()
        # self.driver=setup
        # self.driver.get(self.baseurl)
        # lp =LoginPage(self.driver)
        # lp.setUsername(self.username)
        # lp.setPassword(self.password)
        # lp.clickLogin()
        log.info("--------Test_005_updateCust---------------------")
        log.info("----------verfying test_updateCust------------------------")
        ac=AddCust(self.driver)
        time.sleep(5)
        self.explicitwait(ac.clickmenu_customer())
        time.sleep(5)
        self.explicitwait(ac.click_sub_menu_customer())
        log.info("----------start of test_updateCust test------------")
        sc=Test_search_cust(self.driver)
        time.sleep(3)
        sc.setEmailid_updt_Cust()
        sc.clickSearch()
        # self.row=sc.getLenRow()
        # print('row=',self.row)
        # self.col=sc.getLenCol()
        # print('col=',self.col)
        uc=Test_Update_cust(self.driver)
        time.sleep(3)
        uc.getEdit()
        ac.setFirstNameUpdate()
        ac.clickOnSave()
        time.sleep(2)
        self.msg=uc.getMsg().text
        print(self.msg)
        # close without driver
        if "updated" in self.msg  :
            assert  True
            log.info("----test updatecust --test --is- paased---")
        else:
            self.screen_shot("test_updateCust11.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_updateCust11.png")
            log.error("----test updatecust test is Failed")
            assert False

        #  close with driver
        # if "updated" in self.msg  :
        #     assert  True
        #     log.info("----test updatecust --test --is- paased---")
        #     self.driver.close()
        # else:
        #     self.screen_shot("test_updateCust11.png")
        #     # self.driver.save_screenshot(".\\Screenshots\\" + "test_updateCust11.png")
        #     self.driver.close()
        #     log.error("----test updatecust test is Failed")
        #     assert False