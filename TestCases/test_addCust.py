import time

import pytest

from PageObjects.AddCustPage import AddCust
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClassPage import BaseClass
from Utilities.readProperties import ReadConfig
#
# class Test_003_AddCust(BaseClass):
#     # baseurl = ReadConfig.getApplicationUrl()
#     # username = ReadConfig.getUserEmail()
#     # password = ReadConfig.getPassword()
#     def test_addCust(self,setup):
#         self.loginCommon(setup)
#         log=self.getlogger()
#         self.driver=setup




class Test_003_AddCust(BaseClass):
    # baseurl = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getPassword()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCust(self):
        self.loginCommon()
        log=self.getlogger()
        # self.driver.get(self.baseurl)
        # lp =LoginPage(self.driver)
        # lp.setUsername(self.username)
        # lp.setPassword(self.password)
        # lp.clickLogin()
        log.info("------------Test_003_AddCust---------------------")
        log.info("----------verfying test_addCust------------------------")
        ac=AddCust(self.driver)
        time.sleep(5)
        self.explicitwait(ac.clickmenu_customer())
        time.sleep(5)
        self.explicitwait(ac.click_sub_menu_customer())
        time.sleep(5)
        self.explicitwait(ac.clickAddNew())
        self.explicitwaitSet(ac.setEmail()).clear()
        self.email=self.random_generator() + '@gmail.com'
        # self.email="pratik100@gmail.com"
        time.sleep(5)
        self.explicitwaitSet(ac.setEmail()).send_keys(self.email)
        self.explicitwaitSet(ac.setPaaword()).clear()
        self.explicitwaitSet(ac.setPaaword()).send_keys("46564y6566")
        self.explicitwaitSet(ac.setFirstName()).clear()
        self.explicitwaitSet(ac.setFirstName()).send_keys("satisah")
        self.explicitwaitSet(ac.setLastName()).clear()
        self.explicitwaitSet(ac.setLastName()).send_keys("malhotra")
        ac.clickOnGender('Female')
        time.sleep(2)
        ac.setOnDate()
        ac.selectDate()
        ac.setCompany()
        ac.clickOnIsTaxExempt()
        ac.clickOnNewsletter("Your store name")
        # time.sleep(4)
        ac.clickOnNewsletter("Test store 2")
        ac.clickOnCustomer_roles("Registered")
        self.selectOptionByText(ac.clickOnmanager_of_vendor(),"Vendor 2")
        ac.clickOnactive()
        ac.setAdminComment()
        ac.clickOnSave()
        self.msg = ac.getMsg()
        print(self.msg)
        # close without driver
        if 'customer has been added successfully.' in self.msg:
            assert  True==True
            log.info('--------------test_addCust test is passed-----------')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCust_scr.png")
            log.error("----------test_addCust test is failed--------------------")
            assert  True==False

        # close with driver
        # if 'customer has been added successfully.' in self.msg:
        #     assert  True==True
        #     log.info('--------------test_addCust test is passed-----------')
        #      self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_addCust_scr.png")
        #     self.driver.close()
        #     log.error("----------test_addCust test is failed--------------------")
        #     assert  True==False


