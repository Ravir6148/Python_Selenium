import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Here we are disabling the notification popup
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)

driver.get("https://webengage.com/blog/web-push-notification-guide/")
driver.maximize_window()
time.sleep(5)