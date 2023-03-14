import time

import pytest

from PageObjects.AddCustPage import AddCust
from PageObjects.SearchCustPage import Test_search_cust
from PageObjects.deleteCustPage import DeleteCust
from PageObjects.test_updateCustPage import Test_Update_cust
from Utilities.BaseClassPage import BaseClass


class Test_006_deleteCust(BaseClass):
    # old method
    # def test_deleteCust(self,setup):
    #     self.loginCommon(setup)
    #     self.driver=setup
    #     log=self.getlogger()


    @pytest.mark.regression
    def test_deleteCust(self):
        self.loginCommon()
        log=self.getlogger()
        log.info("--------Test_005_delete_Cust---------------------")
        log.info("----------verfying test_delete_Cust------------------------")
        ac=AddCust(self.driver)
        time.sleep(5)
        self.explicitwait(ac.clickmenu_customer())
        time.sleep(5)
        self.explicitwait(ac.click_sub_menu_customer())
        log.info("----------start of test_delete_Cust test------------")
        sc=Test_search_cust(self.driver)
        time.sleep(3)
        sc.setEmailid_dlt_Cust()
        sc.clickSearch()
        uc=Test_Update_cust(self.driver)
        time.sleep(3)
        uc.getEdit()
        dc=DeleteCust(self.driver)
        dc.clckDeleteButton("Delete")
        # dc.clckDeleteButton("Cancel")
        self.msg=dc.getMsg()
        self.act_title='Dashboard / nopCommerce administration'
        print(self.msg)
        # close without driver
        if "deleted " in self.msg  :
            assert  True
            log.info("----test deletecust --test --is- paased---")
        elif "Dashboard" in self.act_title :
            assert True
            log.info("----test deletecust_canceled --test --is- paased---")
        else:
            self.screen_shot("test_deleteCust.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_updateCust11.png")
            log.error("----test deletecust test is Failed")
            assert False

        # close with driver
        # if "deleted " in self.msg  :
        #     assert  True
        #     log.info("----test deletecust --test --is- paased---")
        #     self.driver.close()
        # elif "Dashboard" in self.act_title :
        #     assert True
        #     log.info("----test deletecust_canceled --test --is- paased---")
        #     self.driver.close()
        # else:
        #     self.screen_shot("test_deleteCust.png")
        #     # self.driver.save_screenshot(".\\Screenshots\\" + "test_updateCust11.png")
        #     self.driver.close()
        #     log.error("----test deletecust test is Failed")
        #     assert False