import time

from selenium.webdriver.common.by import By


class AddCust:
    lnk_menu_customer_XPTH = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnk_submenu_customer_XPTH = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    lnk_addNew_XPTH = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_email_XPTH = '//*[@id="Email"]'
    txt_password_id = 'Password'
    txt_Firstname_id = 'FirstName'
    txt_Lastname_id = 'LastName'
    rdb_gender_male_id = 'Gender_Male'
    rdb_gender_Female_id = 'Gender_Female'
    Dte_pckrbox_XPTH = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[6]/div[2]/span[1]/span/span/span"
    txt_compny_id = 'Company'
    check_box_IsTaxExempt_id = 'IsTaxExempt'
    dropdown_Newsletter_XPTH = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
    dropdown_Customer_roles_XPTH = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div"
    dropdwn_manager_of_vendor_compny_xpth = "//*[@id='VendorId']"
    check_box_active_id = "Active"
    txt_AdminComment_id = "AdminComment"
    btn_save_XPTH = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    msg_XPTH = "/html/body/div[3]/div[1]/div[1]"
    selct_dt_XPTH ="/html/body/div[4]/div/div/div[2]/table/tbody/tr[3]/td[4]/a"

    def __init__( self , driver):
        self.driver = driver

    def clickmenu_customer(self):
        return By.XPATH,self.lnk_menu_customer_XPTH

    def click_sub_menu_customer(self):
        return By.XPATH,self.lnk_submenu_customer_XPTH

    def clickAddNew(self):
        return By.XPATH,self.lnk_addNew_XPTH

    def setEmail(self):
       return  By.XPATH,self.txt_email_XPTH
        # self.driver.find_element(By.XPATH,self.txt_email_XPTH).send_keys("pratikks@gmail.com")

        # return (By.XPATH,self.txt_email_XPTH).clear()
        # return (By.XPATH,self.txt_email_XPTH).send_keys("pratikks@gmail.com")


    def setPaaword(self):

       return By.ID, self.txt_password_id
        # self.driver.find_element(By.ID, self.txt_password_id).send_keys("3356ikks@gmail.com")

    def setFirstName(self):
       return  (By.ID, self.txt_Firstname_id)


    def setFirstNameUpdate(self):
       self.driver.find_element(By.ID, self.txt_Firstname_id).send_keys("ramesh")


    def setLastName(self):
       return  By.ID, self.txt_Lastname_id
        # self.driver.find_element(By.ID, self.txt_Lastname_id).send_keys("raut")

    def clickOnGender(self,Gender):
        if Gender == "Male":
          self.driver.find_element(By.ID, self.rdb_gender_male_id).click()
        elif Gender == "Female":
            self.driver.find_element(By.ID, self.rdb_gender_Female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdb_gender_Female_id).click()

    def clickOnFeMale(self):
        self.driver.find_element(By.ID, self.rdb_gender_Female_id).click()

    def setOnDate(self):
        # return By.XPATH, self.Dte_pckrbox_XPTH
        self.driver.find_element(By.XPATH, self.Dte_pckrbox_XPTH).click()
    def selectDate(self):
        self.driver.find_element(By.XPATH, self.selct_dt_XPTH).click()

    def setCompany(self):
        self.driver.find_element(By.ID, self.txt_compny_id).clear()
        self.driver.find_element(By.ID, self.txt_compny_id).send_keys("apple")

    def clickOnIsTaxExempt(self):
        self.driver.find_element(By.ID, self.check_box_IsTaxExempt_id).click()

    def clickOnNewsletter(self,role):
        self.driver.find_element(By.XPATH, self.dropdown_Newsletter_XPTH).click()
        if role=="Your store name":
          self.list= self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/ul/li[1]")
          self.list.click()
        elif role== "Test store 2":
          # time.sleep(3)
          self.list = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/ul/li[2]")
          # return By.XPATH, "//*[@id='1330f89f-46ef-4e80-b959-2e07d976d49a']"
          # time.sleep(3)
          # self.driver.execute_script("arguments[0].click();" ,self.list)
          self.list.click()
    def clickOnCustomer_roles(self,role):
        self.customer=self.driver.find_element(By.XPATH, self.dropdown_Customer_roles_XPTH)
        self.customer.click()
        if role == "Forum Moderators":
            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/ul/li[2]").click()

        elif role == "Administrators":
            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/ul/li[1]").click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li/span[2]').click()
            self.customer.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/ul/li[3]").click()

        elif role == "Guests":
            self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/ul/li[3]').click()

        elif role == "TESTTIER":
            self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/ul/li[5]').click()

        else:
            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/ul/li[6]").click()


    def clickOnmanager_of_vendor(self):
        return self.driver.find_element(By.XPATH, self.dropdwn_manager_of_vendor_compny_xpth)

    def clickOnactive(self):
        self.driver.find_element(By.ID, self.check_box_active_id).click()

    def setAdminComment(self):
        self.driver.find_element(By.ID, self.txt_AdminComment_id).clear()
        self.driver.find_element(By.ID, self.txt_AdminComment_id).send_keys("Good Morning")


    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_XPTH).click()

    def getMsg(self):
        return self.driver.find_element(By.XPATH, self.msg_XPTH).text

























