from bs4 import BeautifulSoup
import requests

url="https://www.amazon.in/s?k=iphone&crid=379QTXVWDOLLR&sprefix=iphone%2Caps%2C328&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r=requests.get(url, headers=headers)

soup=BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# product_name=soup.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
# product_price=soup.find("span", class_="a-price-whole")

# print(product_name, product_price)