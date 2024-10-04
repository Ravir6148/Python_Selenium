import time
import requests as request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)
# When ever the response will come more 400 or equal to 400.
# To handel broken links we need to install requests package.
# Find all links from page
links = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in links:
    url = link.get_attribute("href")
    try:
        res = request.head(url) # This will hit the url to the server and get the response.
    except:
        None
    if res.status_code>=400: # Thi will give the status code only.
        print(url, "This is a broken link")
        count += 1
    else:
        print(url, "This is a valid link")
print("The total no. of broken links is ", count)
driver.quit()