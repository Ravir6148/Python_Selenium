######################## Static Web Table ###########################

# 1. Count No. of rows and column.
# 2. Read specific row & column data.
# 3. Read all the rows & column data.
# 4. Read data based on condition(List books name whose author is mukesh)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Count No. of rows and column.

noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
print(noOfRows)
noOfColumn = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
print(noOfColumn)

# 2. Read specific row & column data. ---Master In Selenium---

specificCellData = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(specificCellData)

# 3. Read all the rows & column data.
print("Printing all the data from table-------------------------------------")

for r in range(2, noOfRows+1):
    for c in range(1, noOfColumn+1):
        tableData = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(tableData, end="    ")
    print()

# 4. Read data based on condition(List books name whose author is mukesh)
print("Printing Auther Mukesh and His all book along with book price from table-------------------------------------")

for r in range(2, noOfRows+1):
    autherName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if autherName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName,"    ",autherName,"    ",price, end="    ")
    print()
