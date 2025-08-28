from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.ebay.com/sch/i.html?_nkw={query}&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313")

elems = driver.find_elements(By.CLASS_NAME, "su-card-container")
print(f"Total elements found: {len(elems)}")
for elem in elems:
    print(elem.text)

time.sleep(5)
driver.close() 