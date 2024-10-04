import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.get("https://www.flipkart.com/")
driver.maximize_window()


act = ActionChains(driver)

driver.find_element(By.XPATH, "//img[@alt='Mobiles']").click()
min_slider = driver.find_element(By.CSS_SELECTOR, "div[class='iToJ4v Kaqq1s'] div[class='PYKUdo']")
max_slider = driver.find_element(By.CSS_SELECTOR, "div[class='iToJ4v D0puJn'] div[class='PYKUdo']")
print("Location of sliders before changing the position -----------------")
print(min_slider.location) # {'x': 18, 'y': 487}
print(max_slider.location) # {'x': 219, 'y': 487}

act.drag_and_drop_by_offset(min_slider, 90, 0).perform()
time.sleep(5)
act.drag_and_drop_by_offset(max_slider, 150, 0).perform()
print("Location of sliders After changing the position -----------------")
print(min_slider.location) #
print(max_slider.location) #

time.sleep(5)