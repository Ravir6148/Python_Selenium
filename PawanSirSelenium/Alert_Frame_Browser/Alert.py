import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()


alertPopup = driver.switch_to.alert
print(alertPopup.text)
alertPopup.send_keys("Welcome to Dholakpur")

# This will accept/click on ok button
alertPopup.accept()
# This will Dismiss/click on cancel button
# alertPopup.dismiss()
time.sleep(5)
driver.close()