from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

query="iPhone"

driver.get(f"https://www.amazon.com/s?k={query}&crid=2BRB3UHEA7RIC&sprefix=ip%2Caps%2C1335&ref=nb_sb_noss_2")

elem = driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
print("Found with new selector!")
print(elem.text)
# elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
# print(elem.text)
time.sleep(5)
driver.close()