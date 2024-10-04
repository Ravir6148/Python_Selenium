import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()


act = ActionChains(driver)

inputBox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
inputBox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

inputBox1.send_keys("Welcome to my Killa")

# Press CTRL + A

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Press CTRL + C

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press TAB

act.send_keys(Keys.TAB).perform()

# Press CTRL + V

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)

