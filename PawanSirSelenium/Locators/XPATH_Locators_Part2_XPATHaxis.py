from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

svj = Service("")
driver = webdriver.Chrome(service=svj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# Self Xpath axis
text_message = driver.find_element(By.XPATH, '//a[contains(text(),"ICICI Lombard Gen.")]/self::a').text
print("Using Self axis xpath = ", text_message)

# Parent Xpath axis
text_message = driver.find_element(By.XPATH, '//a[contains(text(),"General Ins. Corp.")]/parent::td').text
print("Using Parent axis xpath = ", text_message)

# Child Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/child::td')
# l = len(text_message)
print("Using Child axis xpath are ")
for i in text_message:
    print(i.text, end=" ")
print()

# Ancestor Xpath axis
text_message = driver.find_element(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr').text
print("Using Ancestor axis xpath = ", text_message)

# Descendant Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/descendant::*')
print("Using Descendant axis xpath = ", len(text_message))

# Following Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/following::*')
print("Using Following axis xpath = ", len(text_message))

# Following-sibling Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/following-sibling::*')
print("Using Following-sibling axis xpath = ", len(text_message))

# Preceding Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/preceding::*')
print("Using Preceding axis xpath = ", len(text_message))

# Preceding-sibling Xpath axis
text_message = driver.find_elements(By.XPATH, '//a[contains(text(),"IDFC First Bank")]/ancestor::tr/preceding-sibling::*')
print("Using Preceding-sibling axis xpath = ", len(text_message))