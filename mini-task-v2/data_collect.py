from bs4 import BeautifulSoup
import os
import pandas as pd

d={'title':[],'price':[],'link':[]}

for file in os.listdir("productData"):
    try:
        with open(f"productData/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        # print(soup.prettify())

        # Next steps: 
        # 1. Extract specific data from the HTML using BeautifulSoup methods
        # 2. Store data in dictionaries
        # 3. Store dictionaries into dataframe using pandas
        # 4. Export dataframe to CSV
        
        t=soup.find("div",attrs={"class":"s-card__title"})
        title=t.get_text()
        # print(title)

        p=soup.find("span",attrs={"class":"s-card__price"})
        price=p.get_text()
        # print(price)
        
        l=soup.find("a",attrs={"class":"su-link"})
        link=l['href']
        # print(link)

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
     
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        continue

pd.DataFrame(data=d).to_csv("data.csv",index=False)