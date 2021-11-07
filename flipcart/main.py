import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

website_url = 'https://www.flipkart.com'


def format_laptop_name(laptop_name):
    return laptop_name[:min(len(laptop_name), 40)] + '...'


def format_more_info_url(url):
    return f'{website_url}{url}'


def format_previous_price(new_price, previous_price):
    return previous_price.text[1:] if previous_price else new_price


def format_discount(discount_class):
    if not discount_class: return "N/A"
    return discount_class.span.text.split()[0]


def write_file(data, filename="laptops.json"):
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=2))


def scrap_flipcart():
    content = requests.get(f"{website_url}/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops").text
    soup = BeautifulSoup(content, 'lxml')
    
    laptops = []
    
    data = soup.find('div', class_='_6t1WkM _3HqJxg')
    sections = data.find_all('div', class_='_1AtVbE col-12-12')
    for section in sections:
        print("please wait...")
        fram = section.find_all('div', class_='_3E8aIl Zic51i')
        if not fram: continue # invalid section
        fram = fram[0] # only one valid category in each section
        category_title = fram.div.div.h2.text
        new_laptops = []
        items = fram.find_all('div', class_='_4ddWXP _3BCh3_')
        for item in items:
            laptop_name = format_laptop_name(item.a["title"])
            more_info = format_more_info_url(item.a["href"])
            rating = item.find('div', class_='_3LWZlK').text
            new_price = item.find('div', class_='_30jeq3').text[1:]
            previous_price = format_previous_price(new_price, item.find('div', class_='_3I9_wc'))
            discount = format_discount(item.find('div', class_='_3Ay6Sb'))
            new_laptops.append({
                "laptop_name": laptop_name,
                "rating": rating,
                "new_price": new_price,
                "previous_price": previous_price,
                "discount": discount,
                "more_info": more_info
            })
        laptops.append({
            category_title: new_laptops
        })
    return {"laptops": laptops}



if __name__ == '__main__':
    print("processing started. please wait...\n")
    laptops = scrap_flipcart()
    print("\nprocessing finished!")
    write_file(laptops, "laptops.json")
    print("data saved in \"laptops.json\" file")
