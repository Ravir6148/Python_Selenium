import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(12)

driver.find_element(By.XPATH, "//input[@id='dob']").click() #open the date picker.
datePicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datePicker_month.select_by_visible_text("Feb")
datePicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datePicker_year.select_by_visible_text("1994")
date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dt in date:
    if dt.text == "21":
        dt.click()
        break
time.sleep(5)