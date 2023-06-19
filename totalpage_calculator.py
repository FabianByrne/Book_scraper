import requests
import bs4

def totalpage_calculator(url = "https://books.toscrape.com/catalogue/category/books_1/index.html"):

    # This function calculates the totalpages for the topic of the url given, and assumes 'all books' is intended is nothing entered into the function

    home_destination = requests.get(url)
    soup = bs4.BeautifulSoup(home_destination.text, "lxml")

    # Page calculator -----------------------------------------

    pages_num = soup.select(".current")

    if bool(pages_num):
        pages_num_text = pages_num[0].getText().strip()
        pages_num_list = pages_num_text.split(" ")
        totalpages = int(pages_num_list[-1])
    else:
        totalpages = 1

    return totalpages