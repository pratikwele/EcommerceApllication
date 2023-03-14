from selenium.webdriver.common.by import By
from  selenium import  webdriver


class LoginPage:
    Textbox_username_id="Email"
    Textbox_password_id="Password"
    btn_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    btn_logout_linktext ="Logout"
    # self.driver = webdriver.Firefox()
    def __init__( self , driver):
        self.driver = driver

    # def setUsername(self,username):
    #     self.driver.find_element(By.ID,self.Textbox_username_id).clear()
    #     self.driver.find_element(By.ID,self.Textbox_username_id).send_keys(username)

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.Textbox_username_id).clear()
        self.driver.find_element(By.ID,self.Textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.Textbox_password_id).clear()
        self.driver.find_element(By.ID,self.Textbox_password_id).send_keys(password)

    def clickLogin(self):
         self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_logout_linktext).click()