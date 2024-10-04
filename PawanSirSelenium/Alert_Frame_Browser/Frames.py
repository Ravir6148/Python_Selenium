import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Hi Ravi")
time.sleep(5)
driver.switch_to.default_content()

# Now we are switching to the inner Frame.
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
# When we don't have id or name of the frame then we need to use find element and store in var like below.
outerFrameElement = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrameElement)
innerFrameElement = driver.find_element(By.XPATH, "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driver.switch_to.frame(innerFrameElement)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Hello Ravi")
time.sleep(5)
# To witch to the parent frame we need below command.
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[normalize-space()='Single Iframe']").click()
time.sleep(5)
driver.close()