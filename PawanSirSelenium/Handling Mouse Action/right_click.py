import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

act = ActionChains(driver)
rightClickButton = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act.context_click(rightClickButton).perform()
time.sleep(5)