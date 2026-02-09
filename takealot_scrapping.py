from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
driver.get("https://www.takealot.com/all?_sb=1&_r=1&qsearch=phones%20on%20special&via=suggestions&_si=c3b4aedb77af16c512992f1a16b02e2b")
time.sleep(5)  # wait for products to load
soup = BeautifulSoup(driver.page_source, "html.parser")
#print(soup.prettify())
# Find all product containers
product_items = soup.find_all("div", class_="search-product grid")

for item in product_items:
    name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
    price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
    if name_tag and price_tag:
        name = name_tag.text.strip()
        price = price_tag.text.strip()
        print(f"{name} - {price}")
        myfile=open('myfile.csv','a')
        myfile.write(f"{name}-{price}\n") 
       

driver.quit()
#class="product-card-module_product-title_16xh8"







