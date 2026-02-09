from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt

def scrapping_Products(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(7)  # wait for products to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_items = soup.find_all("div", class_="search-product grid")

    # Array to store TV names
    tv_names = ["Telefunken","Omega","Samsung ","Lexuco ","Toshiba ","JVC ","Hisense"]

    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            tv_names.append(name)  # Add name to array

    driver.quit()

    # Use an if statement to check if any TVs were found
    if len(tv_names) == 0:
        print("No TVs found on the page.")
        return pd.DataFrame()  # Return empty DataFrame

    print("All Available TVs:\n", tv_names)

    # Convert to DataFrame and save
    df = pd.DataFrame({"Product Name and specs": tv_names})
    df.to_csv("mytelevision.csv", index=False)
    return df


def clean_data():
    print("\nCleaning data...")
    df = pd.read_csv("mytelevision.csv")

    # Add placeholder price column if it doesn't exist (for demonstration)
    if 'Price' not in df.columns:
        df['Price'] = "0"

    # Remove R, commas, spaces - convert to number
    df['clean_price'] = (
        df['Price']
        .str.replace("R", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )
    # Extract brand name from the first word
    df['brand'] = df['Product Name and specs'].str.split().str[0]
    df['category'] = df['clean_price'].apply(
        lambda x: "budget friendly" if x < 4000 else "Mid-Range" if x <= 8000 else "premium"
    )
    df.to_csv("takealot_clean.csv", index=False)
    print("Cleaned data saved as takealot_clean.csv")
    return df


def analyze_data(df):
    if df.empty:
        print("No data available for analysis.")
        return

    print("\nStarting analysis...")
    # 1. PRICE DISTRIBUTION
    plt.figure()
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of TVs")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.savefig("price_distribution.png")
    plt.close()

    # 2. BRAND COUNT
    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of TVs Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.savefig("brand_count.png")
    plt.close()

    print("Analysis complete! Plots saved as 'price_distribution.png' and 'brand_count.png'.")
    print("\nDisplaying visualizations...")

    # Show plots
    plt.figure()
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of TVs")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of TVs Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.show()
    print("Visualizations complete.")


# Run the scraper
tv_data = scrapping_Products(
    "https://www.takealot.com/all?_sb=1&_r=1&qsearch=television&via=suggestions&_si=c60259fbac8b1729703b1a7ccd2bc536"
)

if not tv_data.empty:
    # Dynamically find all brands from TV names
    tv_array = tv_data["Product Name and specs"].to_list()
    brands_found = set([name.split()[0] for name in tv_array])  # Extract first word as brand

    if len(brands_found) > 0:
        print("\nBrands found on the page:")
        for brand in brands_found:
            print("-", brand)
    else:
        print("No brands detected.")

    clean_info = clean_data()
    analyze_data(clean_info)
