class TestLogin:
    def test_login_chrome(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Chrome(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()

    def test_login_edge(self):
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Edge(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()

    def test_login_firefox(self):
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.common.by import By

        self.svj = Service("")
        self.driver = webdriver.Firefox(service=self.svj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")
        self.driver.find_element(By.ID, "submit").click()
        self.title = self.driver.title
        assert self.title == "Logged In Successfully | Practice Test Automation"
        self.driver.quit()
