import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
svj = Service("")
driver = webdriver.Chrome(service=svj, options=opt)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(10)

act = ActionChains(driver)

source_element = driver.find_element(By.ID, "box1")
target_element = driver.find_element(By.ID, "box101")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box2")
target_element = driver.find_element(By.ID, "box102")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box3")
target_element = driver.find_element(By.ID, "box103")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box4")
target_element = driver.find_element(By.ID, "box104")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box5")
target_element = driver.find_element(By.ID, "box105")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box6")
target_element = driver.find_element(By.ID, "box106")
act.drag_and_drop(source_element, target_element).perform()

source_element = driver.find_element(By.ID, "box7")
target_element = driver.find_element(By.ID, "box107")
act.drag_and_drop(source_element, target_element).perform()

time.sleep(5)


