import pytest
from selenium.webdriver.common.by import By

class TestCLI:
    @pytest.mark.parametrize('user, password',
                             [("student", "Password123"), ("studnt", "Password123"), ("student", "Password12")])
    def test_login_chrome(self, setup, user, password):
        self.driver = setup
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        try:
            self.title = self.driver.title
            self.driver.close()
            assert self.title == "Logged In Successfully | Practice Test Automation"
        except:
            self.driver.close()
            assert False
