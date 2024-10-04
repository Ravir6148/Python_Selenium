import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container' and @class='select2-selection__rendered']").click()

country_list = driver.find_elements(By.XPATH, "//*[@class='select2-results__options']/li")

for country in country_list:
    if country.text == "Israel":
        country.click()
        break
time.sleep(5)