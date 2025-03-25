import requests
from bs4 import BeautifulSoup as BS
# import fake_useragent
# import selenium


LINK = "https://stalenergo-96.ru/produkcia/"
response = requests.get(LINK).text
soup = BS(response, "lxml").find("div", class_="catalogue_content").find_all("div", class_="catalogue__item")

def major_category(html):
    name = html.find("a", class_="catalogue__item_img").find("img").get("alt")
    link = html.find("a", class_="catalogue__item_img").get("href")
    return name, link

def minor_category(html):
    name = html.find("a").getText()
    link = html.find("a").get("href")
    return name, link

def get_all_minor(html):
    html_minor_categories = html.find("ul").find_all("li")
    list_minor_categories = []
    for cat in html_minor_categories:
        list_minor_categories.append(minor_category(cat))

    return list_minor_categories


id = 0
for i in soup:
    id += 1
    print(id)

    major = major_category(i)
    print(major[0])
    break_cats = ("Услуги и производство", "Мини АЗС", "Цементно-стружечная плита", "Шпунт Ларсена ГОСТ 4781-85")
    if major[0] not in break_cats:
        minor = get_all_minor(i)
        print(*major, sep="\n\t")
        print(*minor, sep='\n')