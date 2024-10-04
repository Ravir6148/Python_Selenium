import pytest


class TestLogin:

    @pytest.mark.parametrize('user, password',
                             [("student", "Password123"), ("studnt", "Password123"), ("student", "Password12")])
    def test_login_chrome(self, user, password):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Chrome(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()

    @pytest.mark.parametrize('user, password',
                             [("student", "Password123"), ("studnt", "Password123"), ("student", "Password12")])
    def test_login_edge(self, user, password):
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Edge(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()

    @pytest.mark.parametrize('user, password',
                             [("student", "Password123"), ("studnt", "Password123"), ("student", "Password12")])
    def test_login_firefox(self, user, password):
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Firefox(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()
