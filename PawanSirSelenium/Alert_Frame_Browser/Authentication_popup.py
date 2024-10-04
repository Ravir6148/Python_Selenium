import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)
# Syntax = driver.get("https://UserName:Password@url")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
driver.close()
