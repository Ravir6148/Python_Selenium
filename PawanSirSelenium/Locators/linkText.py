import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer"
           "/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/%22")
driver.maximize_window()

# Link Text
# driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
# time.sleep(5)
# Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "Forg").click()
time.sleep(5)
driver.close()