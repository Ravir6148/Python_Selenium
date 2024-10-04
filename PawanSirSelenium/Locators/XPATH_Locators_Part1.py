import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

# Xpath with operators
# or, and

# driver.find_element(By.XPATH, '//input[@id="search_query_top" or @name="search_query"]').send_keys("T-Shirts")
# driver.find_element(By.XPATH, '//button[@name="submit_search" and @class="btn btn-default button-search"]').click()

# contains() and starts-with()
# driver.find_element(By.XPATH, '//input[contains(@id,"search")]').send_keys("T-Shirts")
# driver.find_element(By.XPATH, '//button[starts-with(@name,"submit_")]').click()

# text()
driver.find_element(By.XPATH, '//a[text()="Women"]').click()

time.sleep(5)
driver.close()