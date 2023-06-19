import requests
import bs4

def book_details(book_url):

    book_url_scrape = requests.get(book_url)

    book_soup = bs4.BeautifulSoup(book_url_scrape.text, "lxml")

    book_soup_component = book_soup.select(".col-sm-6.product_main")[0]

    print("-------------------------------------")

    # Isolating the title
    book_title = book_soup_component.select('h1')
    book_title = (book_title[0].text)
    print(book_title)

    #Isolating the price
    book_price = book_soup_component.select(".price_color")
    book_price = book_price[0].text
    if book_price[0] == "Â":
        book_price = book_price[1:]
    print(f"Price       : {book_price}")

    #Isolating the stock
    book_stock = book_soup_component.select(".instock.availability")
    book_stock = book_stock[0].text.strip()
    print(f"Availability: {book_stock}")

    # Isolating the rating

    if len(book_soup_component.select(".star-rating.One")) != 0:
        book_rating = "1 out of 5 stars"
    elif len(book_soup_component.select(".star-rating.Two")) != 0:
        book_rating = "2 out of 5 stars"
    elif len(book_soup_component.select(".star-rating.Three")) != 0:
        book_rating = "3 out of 5 stars"
    elif len(book_soup_component.select(".star-rating.Four")) != 0:
        book_rating = "4 out of 5 stars"
    elif len(book_soup_component.select(".star-rating.Five")) != 0:
        book_rating = "5 out of 5 stars"
    print(f"Rating      : {book_rating}")

    # Isolating the description. This is found within the class "product_page", thus a new soup component is needed.

    book_soup_component_description = book_soup.select(".product_page")[0]

    book_description = book_soup_component_description.select('p')[3].text# The paragraph of interest is the 4th paragraph of the product page class, thus the index of [3]
    print(f"Description : {book_description}")
    print("")
    user_proceed = input("Press any key to return to homepage...")

