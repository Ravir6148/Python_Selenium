import time
from filecmp import clear_cache

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()

# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     svj = Service("")
#     preferences = {"download.default_directory": location}
#     opt = webdriver.ChromeOptions()
#     opt.add_argument("--disable-notifications")
#     opt.add_experimental_option("prefs",preferences)
#     my_driver = webdriver.Chrome(service=svj, options=opt)
#     return my_driver

# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     svj = Service("")
#     preferences = {"download.default_directory": location}
#     opt = webdriver.EdgeOptions()
#     opt.add_argument("--disable-notifications")
#     opt.add_experimental_option("prefs",preferences)
#     my_driver = webdriver.Edge(service=svj, options=opt)
#     return my_driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    svj = Service("")
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--disable-notifications")
    opt.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    opt.set_preference("browser.download.manager.showWhenStarting", False)
    opt.set_preference("browser.download.folderList", 2)
    opt.set_preference("browser.download.dir", location)
    my_driver = webdriver.Firefox(service=svj, options=opt)
    return my_driver

# driver = chrome_setup()
# clear_cache()
# driver.implicitly_wait(10)
# driver.get("https://demo.automationtesting.in/FileDownload.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[@type='button']").click()
# driver.quit()

# driver = edge_setup()
# clear_cache()
# driver.implicitly_wait(10)
# driver.get("https://demo.automationtesting.in/FileDownload.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[@type='button']").click()
# driver.quit()

driver = firefox_setup()
clear_cache()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@type='button']").click()
driver.quit()

