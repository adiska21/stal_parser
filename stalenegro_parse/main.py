import requests
from bs4 import BeautifulSoup as BS
import minor_category as MC
# import fake_useragent
# import selenium
import chardet

def do_soup(link):
    response = requests.get(link).text
    soup = BS(response, "lxml")
    return soup

def found_catalogue__item_block(soup):
    catalogue__item_block = soup.find("div", class_="catalogue_content").find_all("div", class_="catalogue__item")
    return catalogue__item_block

def found_catalogue__item_img(soup):
    catalogue__item_img = soup.find("a", class_="catalogue__item_img")
    return  catalogue__item_img

def found_ul(soup):
    try:
        ul = soup.find("ul").find_all("a")
    except AttributeError:
        return None
    return ul

def get_one_category_html_block(soup_one_block):
    catalogue__item_img = found_catalogue__item_img(soup_one_block)
    return catalogue__item_img, found_ul(soup_one_block)

def get_all_category_html_block(soup):
    catalogue__item_block = found_catalogue__item_block(soup)
    all_category_html_block = []
    for i in catalogue__item_block:
        all_category_html_block.append(get_one_category_html_block(i))
    return all_category_html_block

def get_major_category_data(category_html_block_0):
    link = category_html_block_0.get("href")
    name = category_html_block_0.find("img").get("alt")
    return name, link

def get_subcategory_data(category_html_block_1):
    sub_categories = []
    try:
        for sub in category_html_block_1[1]:
            link = sub.get("href")
            name = sub.getText()
            sub_categories.append((name, link))
    except TypeError:
        sub_categories.append(category_html_block_1[0].get("href"))
    return sub_categories

def get_all_data(soup):
    all_category_html_block = get_all_category_html_block(soup)
    major_category_data = []
    subcategory_data = []
    for category_html_block in all_category_html_block:
        major_category_data.append(get_major_category_data(category_html_block[0]))
        subcategory_data.append(get_subcategory_data(category_html_block))
    return major_category_data, subcategory_data

def beautiful_output(cats_data_list):
    for i in range(len(cats_data_list[0])):
        print(*cats_data_list[0][i], end="\n\t")
        print(*cats_data_list[1][i], sep="\n\t")
        # break

def subcategory_parse(all_data):
    ban_links = "".join(open("special_pages.txt", "r").readlines())
    # print(ban_links)

    all_sub_sub_categories_links = []

    for cat_num in range(len(all_data[0])):
        print(cat_num)
        for subcat in all_data[1][cat_num]:
                print(subcat)
                if isinstance(subcat, str) and subcat in ban_links:
                    pass
                else:
                    # print(subcat[0]+"\n    "+subcat[1])
                    # print("\t\t", end=" ")
                    all_sub_sub_categories_links.append(MC.main(subcat))
                break
        # break
    return all_sub_sub_categories_links



def main():
    LINK = "https://stalenergo-96.ru/produkcia/"
    soup = do_soup(LINK)

    all_data = get_all_data(soup)
    with open("subsubcategories_links.txt", "a", encoding='utf-8-sig') as file:
        file.write(str(subcategory_parse(all_data)))
    # beautiful_output(all_data)


if __name__ == "__main__":
    main()