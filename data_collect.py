from bs4 import BeautifulSoup
import os

for file in os.listdir("data"):
    with open(f"data/{file}") as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(soup.prettify())

# Next steps: 
# 1. Extract specific data from the HTML using BeautifulSoup methods
# 2. Store data in dictionaries
# 3. Store dictionaries into dataframe using pandas
# 4. Export dataframe to CSV