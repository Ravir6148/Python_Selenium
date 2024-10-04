import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

bottomLinks = driver.find_elements(By.XPATH, "/html/body/div[2]/footer/div/div/div/ul/li/a")
for i in bottomLinks:
    i.click()
# Getting all window IDs.
windowIDs = driver.window_handles

# switching to the all child windows.

# for win in windowIDs:
#     driver.switch_to.window(win)
#     print(driver.title)

# switching to the Particular browser windows and close it.

for win in windowIDs:
    driver.switch_to.window(win)
    if driver.title == "Subscribe - Software Testing Board" or driver.title == "Practice API Testing using Magento 2 - Software Testing Board":
        driver.close()


