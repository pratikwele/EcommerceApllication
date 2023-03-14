from selenium.webdriver.common.by import By


class Test_search_cust:
    txt_emailid_XPTH="//*[@id='SearchEmail']"
    txt_name_XPTH="//*[@id='SearchFirstName']"
    txt_lastname_XPTH ="//*[@id='SearchLastName']"
    btn_search_XPTH="//*[@id='search-customers']"
    tble_row_XPTH="/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr"
    tble_col_XPTH="/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td"

    def __init__(self, driver):
            self.driver = driver

    def setEmailid_dlt_Cust(self):
        self.driver.find_element(By.XPATH, self.txt_emailid_XPTH).send_keys("arthur_holmes@nopCommerce.com")
    def setEmailid_Srch_Cust(self):
        self.driver.find_element(By.XPATH, self.txt_emailid_XPTH).send_keys("james_pan@nopCommerce.com")
    def setEmailid_updt_Cust(self):
        self.driver.find_element(By.XPATH, self.txt_emailid_XPTH).send_keys("victoria_victoria@nopCommerce.com")




    def setName(self):
        self.driver.find_element(By.XPATH, self.txt_name_XPTH)


    def setLastName(self):
        self.driver.find_element(By.XPATH, self.txt_lastname_XPTH)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_XPTH).click()

    def getLenRow(self):
       self.row=len(self.driver.find_elements(By.XPATH,self.tble_row_XPTH))
       return  self.row
       # return len(self.driver.find_elements(By.XPATH,self.tble_row_XPTH))


    def getLenCol(self):
        # self.col = len(self.driver.find_elements(By.XPATH, self.tble_col_XPTH))
        # print(self.col)
        return len(self.driver.find_elements(By.XPATH, self.tble_col_XPTH))

    def getsearchemail(self):
        for i in range(1,self.getLenRow()+1):
            for j in range(2, 3):
                ele = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr [" + str(i) + "]/td[" + str( j) + "]").get_attribute("innerHTML")
                return ele



