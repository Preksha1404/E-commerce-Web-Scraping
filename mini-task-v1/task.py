from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
file=0
for i in range(1,10):
    driver.get(f"https://www.ebay.com/sch/i.html?_nkw={query}&_sacat=0&_from=R40&_pgn={i}")

    elems = driver.find_elements(By.CLASS_NAME, "su-card-container")
    print(f"Total elements found: {len(elems)}")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1 
    time.sleep(5)
driver.close() 