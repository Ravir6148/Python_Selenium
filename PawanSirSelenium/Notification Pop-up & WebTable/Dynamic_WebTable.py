import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(12)

# Login to the Application.

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

# Going to admin >>>>>>
driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()

# Interacting with table getting all details.
rows = len(driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']/div[1]/div[2]/div"))
# column = driver.find_elements(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[1]")
count1 = 0
for r in range(1, rows+1):
    status = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div["+str(r)+"]/div[1]/div[5]/div[1]").text
    if status == "Enabled":
        count1 += 1
print("Total no of users ", rows)
print("Total no of Enabled users ", count1)
print("Total no of Disabled users ", (rows-count1))