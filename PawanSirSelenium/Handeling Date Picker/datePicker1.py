import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# Selecting the dat by using send_keys.

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/15/2024")

# Selecting date by using datepicker
month = input("Please enter your month: ")
year = input("Please enter your year: ")
date = input("Please enter your date: ")

# For selecting the Month and Year.

while True:
    driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        # For selecting the Future Month and year.
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        # For selecting the Past Month and year.
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

# For selecting the Date.
dt = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dat in dt:
    if dat.text == date:
        dat.click()
        break
time.sleep(5)
