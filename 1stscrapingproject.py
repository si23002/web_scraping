#importing modules and their packages
import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#setting up a variable to be associated with the URL in use
my_url = 'https://www.newegg.com/p/pl?d=graphic+cards'

#opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing (to analyze the html page)
page_soup = soup(page_html, "html.parser")

#grabs each product from the page
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = 'brand, product_name, shipping \n'

f.write(headers)

#for loop to grab info on each product on page
for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "\n")

f.close()
