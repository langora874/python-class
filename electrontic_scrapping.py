from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()

#print(soup.prettify())
# Find all product containers
def electronic(url):
    driver.get(url)
    time.sleep(5)  # wait for products to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_items = soup.find_all("div", class_="search-product grid")

    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            print(f"{name} - {price}")
            myfile=open('myelectronic.csv','a')
            myfile.write(f"{name}-{price}\n") 
        
    driver.quit()
electronic("https://www.takealot.com/all?_sb=1&_r=1&_si=c6d9135a49bdef377840c6e9b647981b&qsearch=headphones")





