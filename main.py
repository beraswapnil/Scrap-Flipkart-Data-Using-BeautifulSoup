import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Reviews = []
for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=phone+under+30000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_2_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_2_0_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=phone+under+30000&requestId=052c32ee-444f-4404-8d3f-6db5f262b00b&page=" + \
        str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    # print(Prices)

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)
    # print(Description)

    review = box.find_all("div", class_="_3LWZlK")
    for i in review:
        name = i.text
        Reviews.append(name)
    # print(Reviews)


if (len(Reviews) < len(Product_name)):
    Reviews.extend(['']*(len(Product_name)-len(Reviews)))

df = pd.DataFrame({"Product Name": Product_name, "Price": Prices,
                  "Description": Description, "Review": Reviews})
# print(df)

df.to_csv("phone_under_30000.csv")
