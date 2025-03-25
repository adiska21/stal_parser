import requests
from bs4 import BeautifulSoup


# import fake_useragent
# import selenium


def do_soup(link):
    response = requests.get("https://stalenergo-96.ru"+link).text
    soup = BeautifulSoup(response, "lxml")
    return soup

def found_catalogue_content_block(soup):
    catalogue_content = soup.find("div", class_="catalogue_content").find_all("div", class_="catalogue__item")
    return catalogue_content

def found_catalogue__item_img(soup):
    catalogue__item_img = soup.find("a", class_="catalogue__item_img")
    return  catalogue__item_img

def get_major_name_and_link(soup):
    link = soup.find("a", class_="catalogue__item_img").get("href")
    name = soup.find("img").get("alt")
    return name, link

def get_all_major_name_and_link(soup):
    all_major_name_and_link = []
    for i in soup:
        all_major_name_and_link.append(get_major_name_and_link(i))
    return all_major_name_and_link

def main(link):
    soup = do_soup(link[1])
    try:
        catalogue_content = found_catalogue_content_block(soup)
    except AttributeError:
        # print("#####################There is not any subcategories")
        return link[0], link[1]

    all_major_name_and_link = get_all_major_name_and_link(catalogue_content)
    # print(*all_major_name_and_link, sep="\n\t\t")
    return all_major_name_and_link


if __name__ == "__main__":
    main("/produkcia/spetsstali_i_chyornyi_prokat/lenta-stalnaya/")