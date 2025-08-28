from bs4 import BeautifulSoup
import requests

url="https://books.toscrape.com/"

r=requests.get(url) # To send a GET request to the URL

soup=BeautifulSoup(r.text, 'html.parser') # To parse the HTML content of the page
# print(soup.prettify())

product_containers=soup.find_all("div",class_="image_container")
# for container in product_containers:
#     product_name=container.img["alt"]
    # print(product_name)

product_prices=soup.find_all("div", class_="product_price")

# for price in product_prices:
#     product_price=price.p.text
    # print(product_price)

for i in range(len(product_containers)):
    print(f"Product Name: {product_containers[i].img['alt']}, Price: {product_prices[i].p.text}")