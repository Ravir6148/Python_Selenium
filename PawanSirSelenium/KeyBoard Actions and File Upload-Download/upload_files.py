import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://tus.io/demo")
driver.maximize_window()

uploadButton = driver.find_element(By.ID, "P0-0").send_keys("C:\\Users\\ravir\\Downloads\\samplefile.pdf")
time.sleep(5)