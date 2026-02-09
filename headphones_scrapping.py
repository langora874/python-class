from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

def electronic(url):#A parameter
    driver.get(url)
    time.sleep(5)  # wait for the page to fully load

    soup = BeautifulSoup(driver.page_source, "html.parser")

   
    product_items = soup.find_all("div", class_="search-product grid")

    # Create a list to store data
    products = []

    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            products.append({"Name": name, "Price": price})

    

    driver.quit()

    # Save to CSV
    df = pd.DataFrame(products)
    df.to_csv("myLaptops.csv", index=False, encoding="utf-8")
    print("Data saved to myLaptops.csv")
    print(df.head())  # Display first few rows for verification

  

       
def clean_data():
    print("\nCleaning data...")
    df = pd.read_csv("myLaptops.csv")

    # Remove "R", commas, and spaces – convert to numeric
    df["clean_price"] = (
        df["Price"]
        .str.replace("R", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )

    # Extract brand name from the first word
    df["brand"] = df["Name"].str.split().str[0]

    # Create category based on price
    df["category"] = df["clean_price"].apply(
        lambda x: "Budget" if x < 4000 else "Mid-Range" if x <= 8000 else "Premium"
    )

    df.to_csv("takealot_clean.csv", index=False)
    print("Cleaned data saved as takealot_clean.csv")
    return df

# Run the scraper

def analyze_data(df):#parameter
    print("\n Starting analysis...")
    # 1. PRICE DISTRIBUTION
    plt.figure()
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of Phones")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.savefig("price_distribution.png")
    plt.close()
    # 2. BRAND COUNT
    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of Phones Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.savefig("brand_count.png")
    plt.close()
    print("Analysis complete! Plots saved as 'price_distribution.png' and 'brand_count.png'.")
    print("\n Starting analysis...")
    # 1. PRICE DISTRIBUTION
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of Phones")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.show()
    # 2. BRAND COUNT
    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of Phones Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.show()
    print(" Visualisations complete.")


    electronic("https://www.takealot.com/all?_sb=1&_r=1&_si=c6d9135a49bdef377840c6e9b647981b&qsearch=headphones")
clean_info = clean_data()
analyze_data(clean_info) #argument