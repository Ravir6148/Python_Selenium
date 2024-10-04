import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.implicitly_wait(10)

act = ActionChains(driver)

driver.switch_to.frame("iframeResult")
field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("Hellow Ravi")
dblclkButton = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(dblclkButton).perform()
time.sleep(5)