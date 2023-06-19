import requests
import bs4
from totalpage_calculator import totalpage_calculator
import random

def all_from_genre(output_url):

    totalpages = totalpage_calculator(output_url)

    page = 1
    book_counter = 0
    all_genre_books = dict()
    while page <= totalpages:
        if page == 1:
            genre_url = output_url
        else:
            genre_url = output_url[:-10]
            genre_url += f"page-{page}.html"

        page_destination = requests.get(genre_url)

        page_soup = bs4.BeautifulSoup(page_destination.text, "lxml")
        page_component = page_soup.select(".product_pod")

        for book in page_component:
            book_counter += 1
            book_title = (book.select("a")[1]["title"])
            book_url = book.select('a')[0]['href']
            url_pruned = False
            while url_pruned == False:
                if book_url[:3] == '../':
                    book_url = book_url[3:]
                else:
                    url_pruned = True
            book_url = f"https://books.toscrape.com/catalogue/{book_url}"
            all_genre_books[book_counter] = [(book_title),(book_url)]

        page += 1

    for book_num in all_genre_books:
        print(f"{book_num}. {all_genre_books.get(book_num)[0]}")

    print("")

    acceptable_input = False
    while acceptable_input == False:
        user_input = input(f"Choose a book from the list (1-{len(all_genre_books)}), or type 'random' to choose a random book from the list: ")
        if user_input == 'random':
            random_selection = random.choice(all_genre_books)
            book_url = random_selection[1]
            acceptable_input = True
            return book_url
        else:
            try:
                user_input = int(user_input)
                book_url = all_genre_books.get(user_input)[1]
                acceptable_input = True
                return book_url
            except ValueError:
                print("Invalid input!")