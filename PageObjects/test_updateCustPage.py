from selenium.webdriver.common.by import By

from PageObjects.SearchCustPage import Test_search_cust


class Test_Update_cust:
    msg_XPTH="/html/body/div[3]/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def getMsg(self):
       return  self.driver.find_element(By.XPATH, self.msg_XPTH)
    def getEdit(self):
      sc = Test_search_cust(self.driver)
      for i in range(1, sc.getLenRow() + 1):
         for j in range(7, 8):
             ele = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr [" + str( i) + "]/td[" + str(j) + "]")
             ele.click()
