import time


import requests as request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo"
           "=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=17320825123597154649&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint"
           "=&hvlocphy=9062010&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
driver.maximize_window()

drpCountry = Select(driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']")) # Here we are using Select class to captures all the dropdown values.

# Select the option from drop-down.
# drpCountry.select_by_visible_text("Books")
# driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# time.sleep(5)

# drpCountry.select_by_index(9)
# driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# time.sleep(5)

# drpCountry.select_by_value("search-alias=alexa-skills")
# driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# time.sleep(5)


# Capture all the options and print them
totalNoOfOptions = drpCountry.options
count = 0
for i in totalNoOfOptions:
    print(i.text)
    count += 1
print("Total No of options is ", count)

driver.quit()