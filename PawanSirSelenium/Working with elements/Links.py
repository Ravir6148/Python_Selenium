import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer"
           "/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/")
driver.maximize_window()

# Internal Link
driver.find_element(By.XPATH, "//a[@class='action remind']//span[contains(text(),'Forgot Your Password?')]").click()
time.sleep(5)
driver.back()

# External Link
driver.find_element(By.XPATH, "//a[@href='https://softwaretestingboard.com/magento-store-notes/?utm_source"
                              "=magento_store&utm_medium=banner&utm_campaign=notes_promo&utm_id=notes_promotion"
                              "']").click()
time.sleep(5)
driver.quit()




