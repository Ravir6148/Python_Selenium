from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageObject:
#Locators
    textBox_UserName_Id = "email"
    textBox_Password_Id = "pass"
    button_SignIn_Xpath = "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"

#Constructor
    def __init__(self, driver):
        self.driver = driver

#Action Methods
    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.ID, self.textBox_UserName_Id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self, pwd):
        passwordtxt = self.driver.find_element(By.ID, self.textBox_Password_Id)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_SignIn_Xpath).click()