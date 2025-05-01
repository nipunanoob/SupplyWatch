import requests,bs4,os

pages = 5
products_dict = {}

if os.path.exists("items"):
    os.remove("items")

for page_index in range(1,6):
    res = requests.get(f"https://web-scraping.dev/products", params={"page": page_index})
    print(res.url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    products_soup = soup.select(".row.product")

    for product in products_soup:
        item_name = product.select_one("h3.mb-0 a").getText()
        item_price= product.select_one("div.price").getText()
        products_dict[item_name] = item_price

with open("items", "a") as f:
    for name, value in products_dict.items():
        f.write(f"{name} {value}\n")
