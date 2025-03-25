import requests
from bs4 import BeautifulSoup as BS
# import fake_useragent
# import selenium


LINK = "https://stalenergo-96.ru/produkcia/"
response = requests.get(LINK).text
soup = BS(response, "lxml").find("div", class_="catalogue_content").find_all("div", class_="catalogue__item")

print(soup)