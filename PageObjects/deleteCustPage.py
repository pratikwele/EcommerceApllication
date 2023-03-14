import time

from selenium.webdriver.common.by import By


class DeleteCust:
   btn_delete_XPTH= '//*[@id="customer-delete"]'
   Pop_up_dlt_XPTH="//button[@class='btn btn-danger float-right']"
   Pop_up_Cancel_XPTH="//span[@class='btn btn-default']"
   Msg_XPTH ="/html/body/div[3]/div[1]/div[1]"


   def __init__(self, driver):
    self.driver = driver

   def  clckDeleteButton(self, action):
     self.driver.find_element(By.XPATH,self.btn_delete_XPTH).click()
     if action=='Delete':
         time.sleep(3)
         self.driver.find_element(By.XPATH, self.Pop_up_dlt_XPTH).click()
     elif action=='Cancel':
         self.driver.find_element(By.XPATH, self.Pop_up_Cancel_XPTH).click()
   #
   # def clckToPopUpDelete(self):
   #
   # def clckToPopUpCancel(self):

   def getMsg(self):
     return self.driver.find_element(By.XPATH, self.Msg_XPTH).text






