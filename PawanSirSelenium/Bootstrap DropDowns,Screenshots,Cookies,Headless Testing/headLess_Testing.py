import time

from selenium import webdriver

from selenium.webdriver.common.by import By

def chrome_Headless_Testing():
    from selenium.webdriver.chrome.service import Service
    svj = Service("")
    opt = webdriver.ChromeOptions()
    opt.headless =True
    my_driver = webdriver.Chrome(service=svj, options=opt)
    return my_driver

driver = chrome_Headless_Testing()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()