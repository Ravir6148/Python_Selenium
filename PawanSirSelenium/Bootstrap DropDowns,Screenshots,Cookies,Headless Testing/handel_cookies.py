import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

cookies = driver.get_cookies()
print("Total no. of cookies are: ", len(cookies))

# Printing all cookies
# for c in cookies:
#     print(c)

# Add Cookies
driver.add_cookie({"name":"Ravi", "value":"Aaram"})
cookies = driver.get_cookies()
print("Total no. of cookies after adding cookies are: ", len(cookies))

# Deleting specific cookies.
driver.delete_cookie("Ravi")
cookies = driver.get_cookies()
print("Total no. of cookies after deleting cookies are: ", len(cookies))

# Deleting all cookies.
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Total no. of cookies after deleting all cookies are: ", len(cookies))

