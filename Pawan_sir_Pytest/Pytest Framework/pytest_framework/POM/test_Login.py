from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from POM_Login import LoginPageObject

class TestLogin:
    def test_login(self):
        svj = Service("")
        self.driver = webdriver.Chrome(service=svj)
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer"
                        "/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/")
        self.driver.maximize_window()

        self.lp = LoginPageObject(self.driver)
        self.lp.setUserName("bittuboss603@gmail.com")
        self.lp.setPassword("Pass@123")
        self.lp.clickLogin()
        self.actual_Title = self.driver.title
        self.driver.close()
        assert self.actual_Title == "My Account"
