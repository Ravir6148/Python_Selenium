import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer"
           "/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/%22")
driver.maximize_window()

# Tag and ID
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("bittuboss603@gmail.com")
# time.sleep(5)

# Tag and Class
# driver.find_element(By.CSS_SELECTOR, "input.input-text").send_keys("bittuboss603@gmail.com")
# time.sleep(5)

# Tag and attributes
# driver.find_element(By.CSS_SELECTOR, 'input[title="Email"]').send_keys("bittuboss603@gmail.com")
# time.sleep(5)

# Tag, Class and attributes
driver.find_element(By.CSS_SELECTOR, 'input.input-text[title="Email"]').send_keys("bittuboss603@gmail.com")
time.sleep(5)
driver.close()
