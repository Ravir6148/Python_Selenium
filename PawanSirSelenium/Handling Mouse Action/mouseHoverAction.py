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
driver.implicitly_wait(30)
act = ActionChains(driver)

fashion = driver.find_element(By.XPATH, "//span[contains(text(),'Fashion')]")
act.move_to_element(fashion).perform()
time.sleep(5)
mens_Bottom_Wear = driver.find_element(By.XPATH, '//a[contains(text(),"Bottom")]')
act.move_to_element(mens_Bottom_Wear).perform()
time.sleep(5)
mens_Dhoti = driver.find_element(By.XPATH, '//a[contains(text(),"Dhoti")]')
act.move_to_element(mens_Dhoti).click().perform()
time.sleep(12)