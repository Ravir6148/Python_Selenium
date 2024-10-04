import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

# 1. Scrolling page by pixel

# value_of_Pixel = driver.execute_script("return window.pageYOffset;") # Thi will help you to get pixel till where you want to scroll
# print(value_of_Pixel)
# driver.execute_script("window.scrollBy(0,1752)","")
# value_of_Pixel = driver.execute_script("return window.pageYOffset;") # Thi will help you to get pixel till where you want to scroll
# print("Pixel value after scrolling ",value_of_Pixel)
# time.sleep(10)

# 2. Scrolling page till element is visible.

ele = driver.find_element(By.XPATH, "//img[@alt='Holothuria fuscogilva']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(10)