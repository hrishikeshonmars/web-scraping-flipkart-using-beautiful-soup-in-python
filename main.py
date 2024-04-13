import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
prices = []
description = []
reviews = []

for i in range(3, 10):
    url = f"https://www.flipkart.com/search?q=phones+under+50k&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=RECENT&suggestionId=phones+under+50k%7CMobiles&requestId=05ce94a7-f10d-42ec-ba3e-76c68a16e2bc&as-backfill=on&page="+str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _2GoDe3")


    names = box.find_all("div", class_="_4rR01T")
    for name in names:
        product_name.append(name.text)

    prices_list = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for price in prices_list:
        prices.append(price.text)
    if len(prices) < len(product_name):
        prices.extend([None] * (len(product_name) - len(prices)))

    desc = box.find_all("ul", class_="_1xgFaf")
    for d in desc:
        description.append(d.text)
    if len(description) < len(product_name):
        description.extend([None] * (len(product_name) - len(description)))

    review_list = box.find_all("div", class_="_3LWZlK")
    for review in review_list:
        reviews.append(review.text)
    if len(reviews) < len(product_name):
        reviews.extend([None] * (len(product_name) - len(reviews)))


max_length = max(len(product_name), len(prices), len(description), len(reviews))
product_name += [None] * (max_length - len(product_name))
prices += [None] * (max_length - len(prices))
description += [None] * (max_length - len(description))
reviews += [None] * (max_length - len(reviews))


df = pd.DataFrame({
    "Product Name": product_name,
    "Price": prices,
    "Description": description,
    "Reviews": reviews
})
print(df)

# Assuming you want to save the DataFrame to a CSV file named flipkart_mobile_under_50000.csv
# df.to_csv("C:/Users/Lenovo/OneDrive/ドキュメント/Need for Speed(TM) Payback/flipkart_mobile_under_50000.csv", index=False)
